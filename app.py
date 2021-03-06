from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrapying

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Set up our scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scrapying.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

# Tell the Flask to run
if __name__ == "__main__":
   app.run()