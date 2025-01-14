import os
from dotenv import load_dotenv
from app import create_app
from celery_config import make_celery
from src.controllers.UrlController import crawl_bp
from src.utils.ExceptionHandler import handle_error

load_dotenv()
app = create_app()
celery = make_celery(app)
celery.conf.update(
    task_serializer='pickle',
    result_serializer='pickle',
    accept_content=['pickle', 'json'],
    worker_concurrency=int(os.getenv('CONCURRENCY', 10)),
    worker_pool=os.getenv('POOL', 'threads')
)

app.register_blueprint(crawl_bp, url_prefix='/api/v1')

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(415)
def handle_server_errors(e):
    return handle_error(e)

if __name__ == '__main__':
    app.run()