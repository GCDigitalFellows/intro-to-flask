# Using templates to render pages

from flask import Flask, render_template

from app import app

# Now that we set up our app folder, we don't need
# to explicitly delcare a static folder
app.config["DEBUG"] = True


@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

    
# Here's another view for our signup page
@app.route("/signup")
def signup():
    return render_template('signup.html')


app.run()
