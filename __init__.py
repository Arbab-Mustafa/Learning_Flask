from flask import Flask
from flask_pymongo import PyMongo
from config import Config  # Import the config class

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB
mongo = PyMongo(app)
