from flask import Flask, render_template

app= Flask(__name__)

JOBS=[
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengauluru',
    'salary': 'Rs 100000'
  },
  {
    'id': 2,
    'title': 'Data scientist',
    'location': 'Mumbai',
    'salary': 'Rs 100000'
  },
  {
     'id': 3,
    'title': 'FrontEnd Engineer',
    'location': 'Trivandrum',
    
  },
  {
     'id': 4,
    'title': 'Backend Engineer',
    'location': 'Kochi',
    'salary': 'Rs 1000000'
  }
]


@app.route("/") # / refers to the empty route
def hello_world():
  return render_template('home.html', jobs=JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)#in order to make the local computer as a host and debug for dynamic rendering
