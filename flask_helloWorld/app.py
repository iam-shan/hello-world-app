from pickle import GLOBAL

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

string1 = ""
string2 = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getHello', methods=['POST'])
def getHello():

    api_url = 'http://34.94.35.116/hello'
    response = requests.get(api_url)
    temp = response.json()
    string1 = temp['message']
    print(string1)
    return render_template('index.html', response1=temp, api_url1=api_url, string1=string1, string2=string2)

@app.route('/getWorld', methods=['POST'])
def getWorld():

    api_url = 'http://34.94.193.46/world'
    response = requests.get(api_url)
    temp = response.json()
    string2 = temp['message']
    print(string2)
    return render_template('index.html', response2=temp, string1=string1, api_url2 = api_url, string2=string2)

@app.route('/getHelloWorld', methods=['POST'])
def getHelloWorld():
    api_url1 = 'http://34.94.35.116/hello'
    api_url2 = 'http://34.94.193.46/world'
    temp1 = requests.get(api_url1).json()['message']
    temp2 = requests.get(api_url2).json()['message']
    temp = temp1 + " " +temp2
    print(string2)
    return render_template('index.html', response3=temp, string1=string1, api_url1=api_url1, api_url2 = api_url2, string2=string2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)