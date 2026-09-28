from flask import Flask
from uuid import UUID

app = Flask(__name__)



@app.route("/")
def home():
    return "home page"

# Integer Converter
@app.route("/user/<int:id>")
def user(id):
    return f"User ID: {id}"

# Float Converter
@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

# String Converter (Default Converter)
@app.route("/users/<string:name>")
def users(name):
    return f"Name is : {name}"

# Path Converter
@app.route("/files/<path:file_path>")
def files(file_path):
    return file_path

@app.route("/student/<uuid:user_id>")
def student(user_id):
    return str(user_id)


if __name__ == "__main__":
    app.run(debug=True)