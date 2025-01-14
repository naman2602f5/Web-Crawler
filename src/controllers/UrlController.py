from apiflask import APIBlueprint
from flask import make_response
from src.schemas.CrawlSchema import crawl_schema
from src.swaggerRequestBodyExamples.CrawlSchemaExamples import crawl_schema_examples

crawl_bp = APIBlueprint("Crawl", __name__)

@crawl_bp.post('/crawl')
@crawl_bp.input(crawl_schema, examples=crawl_schema_examples)
def start_crawl(json_data):
    from main import celery
    data = json_data
    domains = data.get("domains")
    if not domains:
        return make_response({"error": "Domains list is required"}), 400

    for domain in domains:
        start_url = f"https://{domain}/"
        celery.send_task('main.crawl_entry', args=[start_url])

    return make_response({"message": "Crawling started for all domains"}), 200