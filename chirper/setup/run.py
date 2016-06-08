# import Flask
from flask import Flask

# Create the "app" object that handles views,
# starts the server, handles configuration,
# and a bunch of other things
app = Flask(__name__)

# Allows us to see debug output in the browser
app.config["DEBUG"] = True


# This is a "view." These are Python functions that
# activate when particular URLs are visited.
# They return text or HTML that will be displayed.
@app.route("/")
def greetings():
    return "This is my first Flask program"

# This runs the server.
# After running this script, open your browser andgo to:
# http://127.0.0.1:5000/
app.run()
