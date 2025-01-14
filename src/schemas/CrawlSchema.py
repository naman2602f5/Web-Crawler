from marshmallow import Schema, fields


class CrawlSchema(Schema):
    domains = fields.List(fields.String, required=True)

crawl_schema = CrawlSchema()