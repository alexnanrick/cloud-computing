from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Index File"

@app.route("/hello")
def helloworld():
    return "Hello World!"

@app.route("/user/paul")
def userpaul():
    return "User Paul"

@app.route("/post/80")
def port80():
    return "Port 80"

if __name__ == "__main__":
	app.run(host='0.0.0.0',	port=5000,debug=True)	