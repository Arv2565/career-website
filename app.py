from flask import Flask

app= Flask(__name__)
@app.route("/") # / refers to the empty route
def hello_world():
  return "hello world!"

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)#in order to make the local computer as a host and debug for dynamic rendering
