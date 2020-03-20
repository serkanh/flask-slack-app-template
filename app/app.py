import logging
import os

from flask import Flask, request, make_response

import requests
from slackclient import SlackClient

from app.auth import SlackAuth

logging.basicConfig(
    format="[%(asctime)-15s] %(levelname)-8s %(module)-15s l:%(lineno)-4d msg: %(message)s",
    level=os.getenv('LOG_LEVEL', 'INFO')
)

app = Flask(__name__)

slack_client = SlackClient(os.getenv("SLACK_API_USER_TOKEN"))


def slack_verification(f):
    @wraps(f)
    def slack_verification_wrapper(*args, **kwargs):
        slack_auth = SlackAuth()
        if not slack_auth.verify_signature(request):
            return make_response("Request came from outside slack", 403)
        return f(*args, **kwargs)
    return slack_verification_wrapper


@app.route('/endpoint-1', methods=['POST'])
def endpoint_1():
    """ Description
    """
    return "OK"


if __name__ == '__main__':
    debug = True if 'prod' not in str(os.getenv('ENV')) else False
    app.run(host='0.0.0.0', port=80, debug=debug)
