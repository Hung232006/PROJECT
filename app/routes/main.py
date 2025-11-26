from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import db, CartItem, Product

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    return render_template('_index.html')

@main_bp.route('/cart')
@login_required
def view_cart():
    user_id = current_user.id

    cart_items = db.session.query(CartItem, Product)\
        .join(Product, CartItem.product_id == Product.id)\
        .filter(CartItem.user_id == user_id)\
        .all()

    return render_template('cart.html', cart_items=cart_items)
