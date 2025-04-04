from flask import Flask

app = Flask(__name__)

@app.route('/<path:subpath>')
def hello():
  page = f"You requested /{subpath}\n\nThank you for querying the flaskhello app."

  return page

if __name__ == '__main__':
  app.run(debug=True)

