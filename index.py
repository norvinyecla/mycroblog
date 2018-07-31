import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
def home():
    return "<h1>Welcome to Mycroblog</h1>"


@app.route('/entries', methods=["GET"])
def index():
    return "<h1>This is an index of entries<h1>"


@app.route('/entry', methods=["POST"])
def new():
    return "<h1>You added a new entry</h1>"


@app.route('/entry/<int:id>', methods=["PUT"])
def edit(id):
    return "You've edited %d" % id


@app.route('/entry/<int:id>', methods=["DELETE"])
def delete(id):
    return "You've just deleted %d" % id

app.run()

