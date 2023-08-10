from flask import Flask, render_template, Response

app = Flask(__name__, static_folder='static', template_folder='html')

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)