from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/check/<check>')
def show_check(check):
    if check == 'new':
        pass
    return render_template('check.html')

if __name__ == "__main__":
    app.run(
        host = '0.0.0.0',
        debug = True,
    )
