from app import db

#Class product,csid(customer_show_id),asid(admin_show_id),csp,asp,image,head,instock(T/F),size,
#class user
#class admin
#class cashier
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )