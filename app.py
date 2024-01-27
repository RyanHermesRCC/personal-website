from flask import Flask, render_template, Response

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def home():
    return render_template('index2.html')

@app.route("/redko")
def test():
    return render_template('redko.html')

if __name__ == '__main__':
    app.debug = True
    app.run()