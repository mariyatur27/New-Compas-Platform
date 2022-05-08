import os
import secrets

SQLALCHEMY_DATABASE_URI : str
SECRET_KEY : str
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
except KeyError:
    print("DATABASE_URL not configured, defaulting to a sqlite3 database in memory.")
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

try:
    SECRET_KEY = os.environ["SECRET_KEY"]
except KeyError:
    print("SECRET_KEY not configured, generating one and saving it to .env.")
    SECRET_KEY = secrets.token_urlsafe()
    with open(".env", "a") as f:
        f.write("\nSECRET_KEY = '" + SECRET_KEY + "'\n")