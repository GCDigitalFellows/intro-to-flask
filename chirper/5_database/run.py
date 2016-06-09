# Add database support to the application
# The views are now pulled in app/views.py

from app import app
from app import views

app.config["DEBUG"] = True

app.run()
