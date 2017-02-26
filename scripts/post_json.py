import pprint
import json
import requests
import base64
import os

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
img_dir = project_dir + "/data/test/front/a106ccb0.jpg"
img = open(img_dir, "rb").read()
enc_img = base64.b64encode(img)
# print(enc_img)
enc_img_base64_str = enc_img.decode("utf-8")

url = "https://anicap-collector-mn-chrome.c9users.io/pictures.json"
data = {"picture": {"name": "alice", "tag_list": "きんもざ,きらら", "photo": "data:image/jpg;base64,"+enc_img_base64_str}}
files = {'file': ("a106ccb0.jpg", open(img_dir, 'rb'), 'image/jpg', {'Expires': '0'})}
headers_data = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers_data)
# pprint.pprint(response.json())


