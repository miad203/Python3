from __main__ import db
from datetime import timedelta, datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(70), nullable=False)
    # notes = db.relationship('Note', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey(
    #     'user.id'), nullable=False)

    def __repr__(self):
        return f"Note('{self.content}', '{self.date}')"


if __name__ == "__main__":
    with app.app_context():

        db.create_all()
        print('Database created!')
        try:
            user = User.query.filter_by(username='acmiad').first()
            # note_1 = Note(content='I love you saima', user_id=user.id)
            # db.session.add(note_1)
            # db.session.commit()
            print(user.notes)
        except Exception as error:
            print(error)
