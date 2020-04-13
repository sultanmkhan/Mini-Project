from flask import Flask, render_template, jsonify
app= Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/search/<keyword>', methods=['GET'])
def search(keyword):
    response= {keyword: "Cound not find it check the spellings and try again"}
    if keyword=="hi":
        response="hi"
        
    return jsonify(response)


if __name__== '__main__':
    app.run(host='localhost', port=5000, debug=True)