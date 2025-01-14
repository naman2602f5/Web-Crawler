import asyncio
import json
import os
from urllib.parse import urljoin, urlparse, urldefrag
from aiohttp import ClientSession, ClientError
from html import escape
from bs4 import BeautifulSoup

from src.utils.ProductPatterns import ProductPatterns


class Link:
    def __init__(self, src, dst, link_type):
        self.src = src
        self.dst = dst
        self.link_type = link_type

    def __hash__(self):
        return hash((self.src, self.dst, self.link_type))

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.link_type == other.link_type
        )

    def __str__(self):
        return f"{self.src} -> {self.dst}"


class AsyncCrawler:
    def __init__(self, root, depth_limit, confine=None, exclude=None, locked=True, filter_seen=True):
        self.root = root
        self.host = urlparse(root).hostname
        self.depth_limit = depth_limit
        self.locked = locked
        self.confine_prefix = confine
        self.exclude_prefixes = exclude or []
        self.urls_seen = set()
        self.visited_links = set()
        self.links_remembered = set()
        self.domain_products = {}
        self.num_links = 0
        self.num_followed = 0
        self.product_pattern = ProductPatterns()

        self.pre_visit_filters = [
            self._prefix_ok,
            self._exclude_ok,
            self._not_visited,
            self._same_host,
        ]

        self.out_url_filters = [self._prefix_ok, self._same_host] if filter_seen else []

    def _prefix_ok(self, url):
        return self.confine_prefix is None or url.startswith(self.confine_prefix)

    def _exclude_ok(self, url):
        return not any(url.startswith(p) for p in self.exclude_prefixes)

    def _not_visited(self, url):
        return url not in self.visited_links

    def _same_host(self, url):
        try:
            return urlparse(url).hostname == self.host
        except Exception as e:
            print(f"ERROR: Can't process URL '{url}' ({e})")
            return False

    def _pre_visit_url_condense(self, url):
        base, _ = urldefrag(url)
        return base

    async def crawl(self):
        async with ClientSession() as session:
            queue = asyncio.Queue()
            await queue.put((self.root, 0))

            while not queue.empty():
                this_url, depth = await queue.get()

                if depth > self.depth_limit:
                    continue

                if not all(f(this_url) for f in self.pre_visit_filters):
                    continue
                self.visited_links.add(this_url)
                self.num_followed += 1

                try:
                    links = await self._fetch(session, this_url)
                    for link_url in map(self._pre_visit_url_condense, links):
                        if link_url not in self.urls_seen:
                            print(link_url)
                            await queue.put((link_url, depth + 1))
                            self.urls_seen.add(link_url)

                            if all(f(link_url) for f in self.out_url_filters):
                                self.num_links += 1
                                self.links_remembered.add(Link(this_url, link_url, "href"))
                except Exception as e:
                    print(f"ERROR: Can't process URL '{this_url}' ({e})")

    async def _fetch(self, session, url):
        try:
            async with session.get(url) as response:
                if response.content_type != "text/html":
                    raise Exception(f"Not interested in files of type {response.content_type}")

                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")

                links = [
                    urljoin(url, escape(tag.get("href")))
                    for tag in soup.find_all("a", href=True)
                    if urljoin(url, escape(tag.get("href"))).startswith(url)
                ]

                product_links = [link for link in links if self.product_pattern.is_product_page(link)]

                for link in product_links:
                    domain = urlparse(link).hostname
                    if domain not in self.domain_products:
                        self.domain_products[domain] = set()
                    self.domain_products[domain].add(link)
                return links
        except ClientError as e:
            print(f"ERROR: {e}")
            return []


async def start_crawling(url):

    crawler = AsyncCrawler(
        url, int(os.getenv('CRAWLING_DEPTH',3)), exclude=[], confine=url
    )
    await crawler.crawl()
    print("\nCrawling completed.")
    print(f"Links followed: {crawler.num_followed}")
    print(f"Total links found: {crawler.num_links}")
    for link in crawler.links_remembered:
        print(link)

    unique_urls = {link for domain_links in crawler.domain_products.values() for link in domain_links}

    output_file = "product_urls_by_domain.txt"
    output_data = [{url: list(unique_urls)}]

    with open(output_file, "a") as file:
        json.dump(output_data, file, indent=4)
        file.write("\n,")

    return {
        "Links Followed": crawler.num_followed,
        "Total Links Found": crawler.num_links
    }
