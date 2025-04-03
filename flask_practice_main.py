#This writen code for understanding flask is exapmle. 
from flask import Flask 
app = Flask(__name__)

@app.route('/')
def merhaba():
    return "Hello World"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
