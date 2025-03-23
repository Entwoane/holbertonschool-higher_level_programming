from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_file(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
        return [{
            'id': str(product.get('id', '')),
            'name': product.get('name', 'Unknown'),
            'category': product.get('category', 'Uncategorized'),
            'price': product.get('price', 'N/A')
        } for product in data]

def read_csv_file(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        return [{
            'id': str(row.get('id', '')),
            'name': row.get('name', 'Unknown'),
            'category': row.get('category', 'Uncategorized'),
            'price': row.get('price', 'N/A')
        } for row in reader]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    items = data.get('items', [])
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', default=None)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source.')
    try:
        if source == 'json':
            products = read_json_file('products.json')
        else:
            products = read_csv_file('products.csv')
    except FileNotFoundError:
        return render_template('product_display.html', error='Data file not found')

    if not products:
        return render_template('product_display.html', error='No products available')
    if any('id' not in p or not p['id'] for p in products):
        return render_template('product_display.html', error='Missing ID in some products')
    
    if product_id:
        target_id = str(product_id)
        filtered_products = [
            p for p in products 
            if str(p.get('id')) == target_id
        ]
        
        if not filtered_products:
            return render_template('product_display.html', error='Product not found')
            
        return render_template('product_display.html', products=filtered_products)

    return render_template('product_display.html', products=products)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)