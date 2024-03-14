from . import db

class PropertyInfo(db.Model):
    __tablename__ = 'property_info'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    type = db.Column(db.String(80))
    filename = db.Column(db.String(255))
    bedroom_no = db.Column(db.Integer())
    bathroom_no = db.Column(db.Integer())
    price = db.Column(db.Integer())
    location = db.Column(db.String(80))
    description = db.Column(db.String(80))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)