from flask import Flask
from flask_cors import CORS
from model.user_model import mongo
from routes.user_routes import user_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB
mongo.init_app(app)
CORS(app)

# Register routes
app.register_blueprint(user_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
