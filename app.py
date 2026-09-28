from flask import Flask

app = Flask(__name__)

# Static route
@app.route("/")
def home():
    return "home page"

@app.route("/about")
def about():
    return "Welcome to about page"


# url mapping



@app.route("/contact")
def contact():
    return "Welcome to contact page"

# Dynamic Route
@app.route("/users/<name>")
def users(name):
    return f"hello {name}"


# Multiple dynamic parameters
@app.route("/student/<name>/<course>")
def student(name, course):
    return f"{name} is learning {course}"

if __name__ == "__main__":
    app.run(debug=True)