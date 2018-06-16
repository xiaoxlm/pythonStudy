from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('./test/test.html', message = '123yoyoheiheihei')

app.run(host='172.16.20.176', port=8334)