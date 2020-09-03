from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

from view_counter import view_counter

BASE_PATH = "/counter"
RUN_HOST = "localhost"
RUN_PORT = "24409"

app = Flask(__name__)

app.register_blueprint(view_counter, url_prefix="/counter")

#utility function
def fix_werkzeug_logging():
    from werkzeug.serving import WSGIRequestHandler

    def address_string(self):
        forwarded_for = self.headers.get(
            'X-Forwarded-For', '').split(',')

        if forwarded_for and forwarded_for[0]:
            return forwarded_for[0]
        else:
            return self.client_address[0]

    WSGIRequestHandler.address_string = address_string

fix_werkzeug_logging()

if __name__ == "__main__":
    app.run(host = RUN_HOST, port = RUN_PORT)
