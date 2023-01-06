from flask import Flask 

app= Flask(__name__)

@app.route("/")
def main():
    return "succes on miniube "


if __name__=="__main__":
    app.run(debug=True,port=5000)