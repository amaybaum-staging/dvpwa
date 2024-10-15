import sys
import logging
from yaml import Loader, Dumper
from jinja2 import Template
from aiohttp.web import run_app
from sqli.app import init as init_app

data = load(stream, Loader=Loader)
template = Template('Hello {{ name }}!')
template.render(name='John Doe')

log = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app = init_app(sys.argv[1:])
    host = app['config']['app']['host']
    port = app['config']['app']['port']
    log.info(f'App is listening at http://{host}:{port}')
    run_app(app, host=host, port=port)
