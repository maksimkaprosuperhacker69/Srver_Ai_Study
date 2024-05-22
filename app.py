import os

import AI
from flask import Flask
import urllib.request
import file_reader_text

app = Flask(__name__)

@app.route("/")
def home():

    return 'hello'

@app.route("/ans/")
def read_item(promt_response: str, course_id: str, file_path: str, que_count: int = 10, ):
    name = f'{course_id}.png'
    urllib.request.urlretrieve(file_path, name)

    text = file_reader_text.text_reader(name)
    os.remove(name)

    return AI.main_gpt_ask(promt = AI.promt_create(promt_type = promt_response, que_count = que_count), text = text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

