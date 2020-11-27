import socket
import platform
import boto3
from flask import Flask, request, render_template
import logging
import telegram
import random

application = Flask(__name__)
logging.basicConfig(filename='demo.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')




class AwsS3:                                                                                                   
    def __init__(self):   
        ACCESS_KEY_ID = "AKIA365FFYHDA6VIQIIU"
        ACCESS_KEY_SECRET = "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"                                                                                     
        self._s3 = boto3.client(                                                                               
            "s3",                                                                                              
            aws_access_key_id=ACCESS_KEY_ID,                       
            aws_secret_access_key=ACCESS_KEY_SECRET,               
        )                                                                                                      
                                                                                                            
    def upload_file(self, bucket, name, file_obj) -> str:                       
        """Upload File to AWS S3 and return image url"""                        
        try:                                                                                                   
            self._s3.upload_fileobj(file_obj, bucket, name)                     
            url = f"https://{bucket}.s3.amazonaws.com/{name}"                   
            return url                                                                                         
        except ClientError as err:                                                                             
            _logger.error(err)                                                                                 
            raise err                                                                                          
                                                                                                            
    def get_object_with_key(self, key):                                                                        
        return self._s3.get_object(Bucket=settings.AWS_S3_PRIVATE_BUCKET, Key=key).get(
            "Body"                                                                                             
    )
    def list_objects(self, bucket):
        return self._s3.list_objects(Bucket=bucket)


def send_test_message(message: str):
    try:
        random_number = random.randint(0, 1000)
        telegram_notify = telegram.Bot("1428355101:AAFT5w9__0qMerkTuv1cxELusGo-nNRXgaA")
        telegram_notify.send_message(
            chat_id="-416651771", 
            text=message
        )
    except Exception as ex:
        print(ex)


@application.route("/", methods=["GET", "POST"])
def hello():
    title = "INDEX"
    user = {"username": "Thanh"}
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
        message = (
            f"remote_addr: {request.remote_addr} \n "
            f"REMOTE_ADDR: {client_ip} \n "
            f"HTTP_X_FORWARDED_FOR: {ip}"
        )
        send_test_message(message)

    if request.method == "POST":
        print(f"{request.form}")
    
    return render_template("index.html", title=title, user=user)


@application.route("/coto", methods=["GET", "POST"])
def coto():
    s3 = AwsS3()
    list_objects_s3 = s3.list_objects("private-keypair")["content"]
    list_image = []
    for i in list_objects_s3:
        image_content = s3.get_object_with_key(i["Key"])
        list_image.append(image_content)
    title = "COTO"
    user = {"username": "Thanh"}
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
    
    return render_template("coto-image.html", title=title, user=user, list_image=list_image)



@application.route("/tamdao", methods=["GET", "POST"])
def tamdao():
    title = "COTO"
    user = {"username": "Thanh"}
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
    
    return render_template("tamdao-image.html", title=title, user=user)



@application.route("/khac", methods=["GET", "POST"])
def khac():
    title = "COTO"
    user = {"username": "Thanh"}
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
    
    return render_template("khac-image.html", title=title, user=user)



if __name__ == "__main__":
    application.run(host='0.0.0.0')

