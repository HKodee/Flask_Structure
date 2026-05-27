from app import db
from app.models import product
from flask import Blueprint, render_template, redirect, request, url_for, flash, session

products_bp = Blueprint('products', __name__)

@products_bp.route('/')
def view_products():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    products = product.query.all()
    