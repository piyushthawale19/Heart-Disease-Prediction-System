import os
import logging
from flask import Flask

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-for-heart-prediction")

# Import routes after app creation to avoid circular imports
from routes import *

if __name__ == "__main__":
    # Render (and other cloud hosts) provide PORT via environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
