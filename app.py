from flask import Flask, render_template,send_from_directory,request, jsonify, make_response
from flask_cors import CORS, cross_origin
import matplotlib.pyplot as plt
import boto3
import os
import numpy as np

app = Flask(__name__ 
    ,static_folder='client/build',static_url_path='')
cors = CORS(app)

@app.route('/api')
@cross_origin()
def Welcome():
    return "Welcome to the API!!!"

@app.route('/api/justpie/')
@cross_origin()
def GeneratePie():
    return "<h1>we love html</h1>"


@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')


