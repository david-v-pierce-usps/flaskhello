from flask import Flask

app = Flask(__name__)

def response(value = None):
  if not value:
    value = ""
  return f"You requested /{value}<br><br>Thank you for querying the flaskhello app."

@app.route('/')
def nothing():
  return response()

@app.route('/<subpath>')
def hello(subpath):
  return response(subpath)

if __name__ == '__main__':
  app.run(debug=True)

