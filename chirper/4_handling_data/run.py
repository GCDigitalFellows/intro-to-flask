# Handling data

from flask import Flask, render_template

from app import app

# Now that we set up our app folder, we don't need
# to explicitly delcare a static folder
app.config["DEBUG"] = True


@app.route("/")
@app.route("/index.html")
def index():
    # This data is fake in the sense that we're just adding it here
    # Later we'll use a database for this

    # This is a list of dictionaries, they will be our chirp data
    chirps = [
        {"time": "1:30 PM",
         "user": "b_marley_fan",
         "text": "I <3 legend best album ever!!!!!! #omg"},
        {"time": "3:30 PM",
         "user": "moxy_marleyspike",
         "text": "Love talking about B Marley on Chirper! #chirperlife"}
        ]

    # now we give our chirps data to the template so that it can be displayed
    return render_template('index.html', chirps=chirps)

    
@app.route("/signup")
def signup():
    return render_template('signup.html')


app.run()
