import os

SQLALCHEMY_DATABASE_URI : str

try:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
except KeyError:
    print("DATABASE_URL not configured, defaulting to sqlite database in memory.")
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"