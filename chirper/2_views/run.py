# Playing with view functions

from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["STATIC_FOLDER"] = 'static'

# The "/" and "index.html" are the URLs that will be handled
@app.route("/")
@app.route("/index.html")
def index():
    return '''<h1>Chirper</h1>
    <p>The newest highly original social media sensation.</p
    <p>Go <a href="/signup">here</a> to get started!</p>'''

    
# Here's another view for our signup page
@app.route("/signup")
def signup():
    return "Under construction! Come back in twenty minutes."


# Here's a third view with an image of the legendary Bob Marley
# To find it, when the server is running, go to:
# http://127.0.0.1:5000/bobmarley
@app.route("/bobmarley")
def bob():
    return '''<img src="static/bobmarley.jpg">'''

# This runs the server.
# After running this script, open your browser andgo to:
# http://127.0.0.1:5000/
app.run()
