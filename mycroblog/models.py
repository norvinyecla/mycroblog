from mycroblog import db

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return '%s' % self.text

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Entry.query.all()
