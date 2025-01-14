import asyncio

from main import celery
from src.service.AsyncCrawler import start_crawling


@celery.task(name='main.crawl_entry', bind=True, autoretry_for=(Exception,))
def crawl_domain(self, url):
    try:
        return asyncio.run(start_crawling(url))
    except Exception as e:
        if self.request.retries >= self.max_retries:
            return e
        raise self.retry(exc=e, countdown=10)