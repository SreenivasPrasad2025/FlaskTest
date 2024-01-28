import flask
app = flask.Flask(__name__)
@app.route('/')
def home():
    return "It works"
if __name__ == '__main__':
    app.debug = True
    app.run(port=1232)
