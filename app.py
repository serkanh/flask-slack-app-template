from flask import Flask, request

import logging
import os

import requests
from slackclient import SlackClient

logging.basicConfig(
    format="[%(asctime)-15s] %(levelname)-8s %(module)-15s l:%(lineno)-4d msg: %(message)s",
    level="INFO"
)

app = Flask(__name__)

slack_client = SlackClient(os.getenv("SLACK_API_USER_TOKEN"))


@app.route('/endpoint-1', methods=['POST'])
def endpoint_1():
    """ Description
    """
    return "OK"


if __name__ == '__main__':
    debug = True if 'prod' not in str(os.getenv('ENV')) else False
    app.run(host='0.0.0.0', port=80, debug=debug)
