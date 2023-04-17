from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True )
    price = db.Column(db.Integer)
    description = db.Column(db.String)
    image = db.Column(db.String)

    def __init__(self, title, price, description, image):
        self.title = title
        self.price = price
        self.description = description
        self.image = image

    
    def saveProduct(self):
        db.session.add(self)
        db.session.commit()

  
    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'price' : self.price,
            'description' : self.description,
            'image' : self.image,      
        }
