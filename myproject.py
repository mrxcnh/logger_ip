import socket
import platform
from flask import Flask, request
import logging

application = Flask(__name__)
logging.basicConfig(filename='demo.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')


@application.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        re_addr = request.remote_addr
        print(f"{request.remote_addr}")
        client_ip = request.environ.get('REMOTE_ADDR')
        print(f"CL IP: {client_ip}")
        ip = request.environ.get('HTTP_X_FORWARDED_FOR')
        print(f"CL IP_X: {ip}")

        application.logger.info(f"request.remote_addr: {request.remote_addr}")
        application.logger.info(f"request.environ.get('REMOTE_ADDR'): {client_ip}")
        application.logger.info(f"request.environ.get('HTTP_X_FORWARDED_FOR'): {ip}")

    if request.method == "POST":
        print(f"{request.form}")
    
    return "<h1>ALO</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')

