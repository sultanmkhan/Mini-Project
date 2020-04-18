from flask import Flask, render_template, jsonify, Response, session
import xmltodict, json
from pprint import pprint
import xml.etree.ElementTree as ET
#from cassandra.cluster import Cluster
import requests
import hashlib

#cluster = Cluster(contact_points=['172.17.0.2'],port=9042)
#session = cluster.connect()

app= Flask(__name__)
app.secret_key='super'
@app.route('/')
def index():
   return "<h1> Wellcom to Goodreads</h1><b><h4> please login before perform any action"
   #return render_template('index.html')

@app.route('/login/<username>/<password>', methods=['GET', 'POST'])
def login(username, password):
    salt = '5gz'
    password = password+salt
    password = hashlib.md5(password.encode())
    password = password.hexdigest()
    if(password=='24e2a20dcb8d414d13a21209ad26624e'):
        session['user_name']='admin'
        pprint(session)
        return "<h2>Login was successful</h2>"
    else:
        return "<h2>This is invalid credentials try again </h2>"
    #rows = session.execute("""SELECT * FROM user.usernamesANDpassword WHERE username='{}' AND password='{}'""".format(username, password))
    #if i in rows:
       # return {username:'welcome'}
   # else:
     #   return {password: 'Wrong'}

@app.route('/search/<keyword>', methods=['GET'])
def search(keyword):
    url="https://www.goodreads.com/search/index.xml?key=iLbLcwF5ca4oLVjiCdn4A&q={keyword}"    #key included
    response= requests.get(url)
    response= response.content
    #pprint(response)
    #tree = ET.parse(response)
    #root = ET.fromstring(response)


    #content = xmltodict.parse(response)  # converting Xml date to a dictionary
    #json_content= json.dumps(content)   # converting dictionary  to Json
    #print(content['GoodreadsResponse']['search']['results']['work'][])

    return jsonify({keyword :"cannot find anything"})

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user_name', None)
    return "<h2>Logout was successful </h2>"


if __name__== '__main__':
    app.run(host='localhost', port=5000, debug=True)