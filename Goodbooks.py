from flask import Flask, render_template, jsonify, Response
import xml.etree.ElementTree as ET
import requests
import hashlib

app= Flask(__name__)
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/<username>/<password>', methods=['GET', 'POST'])
def login(username, password):
    salt='5gz'
    password =password+salt
    password= hashlib.md5(password.encode())
    password= password.hexdigest()
    if password=='24e2a20dcb8d414d13a21209ad26624e':
        print('hi sultan')
        return {username:'welcome'}
    else:
        print('wrong password')
        return {password: 'hi there'}

@app.route('/search/<keyword>', methods=['GET'])
def search(keyword=0):
   if keyword!=0:
         url="https://www.goodreads.com/search/index.xml?key=iLbLcwF5ca4oLVjiCdn4A&q=keyword"
         response= requests.get(url).content
         root= ET.fromstring(response)
         for i in root.iter('title'):
             print(i.attrib)
         return root[1][3].text
   else:
       return jsonify("Could not find it check the spellings and try again")

if __name__== '__main__':
    app.run(host='localhost', port=5000, debug=True)