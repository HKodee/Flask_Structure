from app import db

class Product(db.models):
    id = db.Column(db.Integer, primary_key=True)

    pcm = db.Column(
        db.String(100),
        nullable=False
    ) # Product Customer Model

    pam = db.Column(
        db.String(100),
        nullable=False
    ) # Product Admin Model

    cp = db.Column(
        db.Integer,
        nullable=False
    ) # Cost price

    sp = db.Column(
        db.Integer,
        nullable=False
    ) # Sell price

    size = db.Column(
        db.Integer,
        nullable=False
    ) 

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

