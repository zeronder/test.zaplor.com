from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pending/<when>')
def pending(when):
    return render_template('pending.html', when=when)

@app.route('/status/<type>')
def status(type):
    return render_template('status.html', type=type)

@app.route('/reminder')
def reminder():
    return render_template('reminder.html')

if __name__ == '__main__':
    app.run()