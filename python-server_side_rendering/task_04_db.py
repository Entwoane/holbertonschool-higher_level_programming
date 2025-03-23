from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)
DATABASE = 'products.db'

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

def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

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
    products = []

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source.')
    try:
        if source == 'json':
            products = read_json_file('products.json')
        elif source == 'csv':
            products = read_csv_file('products.csv')
        elif source == 'sql':
            conn = connect_db()
            cursor = conn.cursor()
            
            query = "SELECT id, name, category, price FROM Products"
            params = ()
            
            if product_id:
                query += ' WHERE id = ?'
                params = (product_id,)
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            
            conn.close()
            products = [dict(row) for row in rows]
            
            for p in products:
                p['id'] = str(p['id'])
                p['price'] = str(p['price'])
            
            if source == 'sql' and product_id and not products:
                return render_template('product_display.html', error='Product not found')
            
    except FileNotFoundError:
        return render_template('product_display.html', error='Data file not found')
    except sqlite3.Error as e:
        return render_template('product_display.html', error=f'Database error: {e}')
    except Exception as e:
        return render_template('product_display.html', error=f'Unexpected error: {e}')

    if not products:
        return render_template('product_display.html', error='No products available')
    if any('id' not in p or not p['id'] for p in products):
        return render_template('product_display.html', error='Missing ID in some products')

    return render_template('product_display.html', products=products)
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)