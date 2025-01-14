crawl_schema_examples = {
    'domains_example': {
        'summary': 'Use this body to submit a list of domains for crawling',
        'description': (
            '- `domains` is a required field and should be a list of domain names as strings.\n\n'
            '- Ensure the list contains valid domain names that you want to process.\n\n'
            '- The system will process each domain and return results based on the provided list.'
        ),
        'value': {
            "domains": ["goosegreaseshop.com", "books.toscrape.com", "www.cratejoy.com"]
        }
    }
}