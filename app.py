from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For session management

# Sample product data
products = [
    {'id': 1, 'name': 'Product 1', 'price': 100, 'image': 'product1.jpg'},
    {'id': 2, 'name': 'Product 2', 'price': 150, 'image': 'product1.jpg'},
    {'id': 3, 'name': 'Product 3', 'price': 200, 'image': 'product1.jpg'}
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    prod = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=prod)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []

    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        session['cart'].append(product)
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    return render_template('cart.html', cart=session.get('cart', []))

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
