from ... import database


class User(db.Model):  # ToDo
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.string(256), unique=False, nullable=False)

    def __str__(self):
        return self.username
