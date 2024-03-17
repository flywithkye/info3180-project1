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
    description = db.Column(db.String(2500))

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
        
    def get_title(self):
        try:
            return unicode(self.title)  # python 2 support
        except NameError:
            return str(self.title)  # python 3 support
    
    def get_type(self):
        try:
            return unicode(self.type)  # python 2 support
        except NameError:
            return str(self.type)  # python 3 support
        
    def get_filename(self):
        try:
            return unicode(self.filename)  # python 2 support
        except NameError:
            return str(self.filename)  # python 3 support
        
    def get_bedroom_no(self):
        try:
            return unicode(self.bedroom_no)  # python 2 support
        except NameError:
            return self.bedroom_no  # python 3 support
        
    def get_bathroom_no(self):
        try:
            return unicode(self.bathroom_no)  # python 2 support
        except NameError:
            return self.bathroom_no  # python 3 support
        
    def get_price(self):
        try:
            return unicode(self.price)  # python 2 support
        except NameError:
            return self.price  # python 3 support
        
    def get_location(self):
        try:
            return unicode(self.location)  # python 2 support
        except NameError:
            return str(self.location)  # python 3 support
        
    def get_description(self):
        try:
            return unicode(self.description)  # python 2 support
        except NameError:
            return str(self.description)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)