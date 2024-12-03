from flask import Flask
from flask import request

app = Flask(__name__)

# Personnel dictionary
personnel = {
    "rachel": "Executive Vice President of Managerial Functions",
    "wallace": "Senior Vice President of Managerial Functions",
    "rosie": "Staff Vice President of Managerial Functions",
    "james": "Vice Vice President of Managerial Functions",
    "henri": "Junior Vice President of Managerial Functions"
}

@app.route('/')
def home():
    return "Welcome to the Flask Lab!"

# http://127.0.0.1:5000/greet/rachel
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"


# http://127.0.0.1:5000/personnel/unknown
# http://127.0.0.1:5000/personnel/Henri
@app.route('/personnel/<name>')
def get_personnel(name):
    name = name.lower()  
    if name in personnel:
        return f"{personnel[name]}"
    else:
        return "Employee not found"

# http://127.0.0.1:5000/library?title=1984&author=George%20Orwell
# http://127.0.0.1:5000/library?title=Harry%20Potter
@app.route('/library')
def library():
    title = request.args.get('title', 'Unknown')
    author = request.args.get('author', 'Unknown')
    return f"Searching for books titled '{title}' by {author}"

if __name__ == '__main__':
    app.run(debug=True)
