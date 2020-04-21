from flask import Flask, jsonify, Response, session
import hashlib
import requests
import xml.etree.ElementTree as ET
from cassandra.cluster import Cluster

cluster = Cluster(contact_points=['172.17.0.2'], port=9042)
session = cluster.connect()

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Wellcom to Goodbooks</h1><b><h4> please login"

@app.route('/login/<username>/<password>', methods=['GET', 'POST'])
def login(username, password):
    salt = '5gz'
    password = password + salt
    password = hashlib.md5(password.encode())
    password = password.hexdigest()
    rows = session.execute(
        """SELECT * FROM user.usernamesandpassword  WHERE username='{}' AND password='{}'""".format(username, password))
    result = rows.all()
    if (len(result) > 0):
        return {username: 'welcome'}
    else:
        return {username: '! You have  entered wrong credentials try again'}

"""The search methods returns first 20 titles from Goodreads by title"""
@app.route('/search/<keyword>', methods=['GET'])
def search(keyword):
    url = "https://www.goodreads.com/search/index.xml?key=iLbLcwF5ca4oLVjiCdn4A&q={}".format(keyword)  # key included
    r = requests.get(url)
    root = ET.fromstring(r.content)
    titles = []
    for name in root.iter('title'):
        titles.append(name.text)  # appending retrieved results
    return jsonify({'Titles ': titles})

@app.route('/logout', methods=['GET'])
def logout():
    cluster.shutdown()
    return "<h2>Logout was successful </h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
