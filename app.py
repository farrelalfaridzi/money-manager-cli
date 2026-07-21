from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Money Manager Web"

if __name__=="__main__":
    app.run(debug=True)