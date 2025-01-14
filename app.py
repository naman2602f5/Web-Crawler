from apiflask import APIFlask


def create_app():
    app = APIFlask(__name__, title='Web Crawler', docs_path='/webCrawler/doc')
    return app

