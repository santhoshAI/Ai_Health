from flask import Flask, render_template, request, flash
from chatbot import gemi

gemi("You are a helpful health chatbot.Provide clear instructions and ask for information in a conversational way.")

app = Flask(__name__)
app.secret_key='123'

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET','POST'])
def chat():
    return render_template('chat.html')

@app.route('/report', methods=['GET','POST'])
def report():
    return render_template('report.html')

@app.route('/device', methods=['GET','POST'])
def device():
    return render_template('device.html')

@app.route('/get', methods=['GET','POST'])
def get():
    msg = request.form['msg']
    out=gemi(msg).replace('\n', '<br>')
    return out

@app.route('/undev', methods=['GET','POST'])
def undev():
    return render_template('development.html')

    


if __name__ == "__main__":
    app.run(debug=True)
