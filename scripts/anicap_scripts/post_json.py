import json
import requests
import base64
import os


class PostJson:
    @staticmethod
    def post(file_dir):
        ext = os.path.splitext(file_dir)[1].lstrip(".")
        if not os.path.isdir(file_dir):
            img = open(file_dir, "rb").read()
            enc_img = base64.b64encode(img)
            enc_img_base64_str = "data:image/"+ext+";base64,"+enc_img.decode("utf-8")

            url = "https://anicap-collector-mn-chrome.c9users.io/pictures.json"
            data = {"picture": {"name": "aqua", "tag_list": "このすば", "photo": enc_img_base64_str}}
            headers_data = {"Content-Type": "application/json"}

            # requests.post(url, data=json.dumps(data), headers=headers_data)
            print(file_dir)