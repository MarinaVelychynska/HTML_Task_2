
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def parent():
    return render_template('parent.html')


@app.route('/mypage/me')
def mypage_me():
    return render_template('mypage_me.html')


@app.route('/mypage/contact')
def mypage_contact():
    return render_template('mypage_contact.html')


if __name__ == '__main__':
    app.run(debug=True)