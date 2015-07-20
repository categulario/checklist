from flask import Flask
from flask import render_template
from flask import jsonify
from flask import redirect
from flask import url_for
from hashids import Hashids
from time import time

app = Flask(__name__)
hashids = Hashids(
    salt = 'y05VG4El4$4QdkNB0{IWXkmp<|Ba+yo6',
    min_length = 10,
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/c/<check>')
def show_check(check):
    if check == 'new':
        curtime = time()
        return redirect(url_for('show_check',
            check=hashids.encode(int(curtime), int((curtime%1)*10000000))
        ))
    return render_template('check.html')

if __name__ == "__main__":
    app.run(
        host = '0.0.0.0',
        debug = True,
    )
