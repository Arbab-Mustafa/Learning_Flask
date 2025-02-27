from flask import Flask
from flask_cors import CORS
from config import MONGO_Config, mongo  # ✅ Import mongo from config
from routes.user_routes import user_bp  # ✅ Only import routes

app = Flask(__name__)
app.config.from_object(MONGO_Config)  # ✅ Load MongoDB URI
mongo.init_app(app)  # ✅ Initialize MongoDB
CORS(app)

# Register routes
app.register_blueprint(user_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
