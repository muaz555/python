from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Salaam Un Alaykum, Dunya!"

if __name__ == "__main__":
    app.run()
