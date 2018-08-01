import flask

request = flask.request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
def home():
    return "<h1>Welcome to Mycroblog</h1>"


@app.route('/entries', methods=["GET"])
def browse():
    return "<h1>This is an index of entries<h1>"


@app.route('/entry/<int:id>', methods=["GET"])
def read(id):
    return "<h1>This is entry #{id}".format(
        id=id
    )


@app.route('/entry', methods=["POST"])
def add():
    params = request.get_json()
    if "body" in params:
        return "<h1>You added a new entry:</h1> <p>{body}</p>".format(
            body=params["body"]
        ) 
    else: 
        return "No content provided"


@app.route('/entry/<int:id>', methods=["PUT"])
def edit(id):
    params = request.get_json()
    if "body" in params:
        return "<h1>You edited entry number {id} a new entry:</h1> <p>{body}</p>".format(
            id=id, 
            body=params["body"]
         )
    else: 
        return "No content provided"


@app.route('/entry/<int:id>', methods=["DELETE"])
def delete(id):
    return "You've just deleted entry #{id}".format(
        id=id
    )
    

app.run()

