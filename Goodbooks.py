from flask import Flask, render_template, jsonify, Response
import requests

app= Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/search/<keyword>', methods=['GET'])
def search(keyword=0):
   if keyword!=0:
         url="https://www.goodreads.com/search/index.xml?key=iLbLcwF5ca4oLVjiCdn4A&q=keyword"
         response= requests.get(url).content
         return Response(response)
   else:
       return jsonify("Could not find it check the spellings and try again")

if __name__== '__main__':
    app.run(host='localhost', port=5000, debug=True)