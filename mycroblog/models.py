from mycroblog import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100))

    def __repr__(self):
        return '%s' % self.text
