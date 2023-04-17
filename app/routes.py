from app.models import db, Product
from flask import render_template
from app import app
from app.api import Products
from flask import Blueprint, render_template, request, redirect, url_for, flash



@app.route('/')
def gatherInfo():
    for y in range(10,21):
        x = Products(y)
        p = Product(title=x['title'],price=x['price'],description=x['description'],image=x['image'])
        p.saveProduct()
    return render_template('index.html')





@app.route('/shop')
def productDB():
    y = Product.query.all()
    prodlist = [p.to_dict() for p in y]
    return {
        'status': 'ok',
        'data' : prodlist,
        'item_count' : len(prodlist)
    }


    
# @app.route('/shop/<int:product_id>')
# def indPost(product_id):
#     product = Product.query.get(product_id)
#     if product:
#         return render_template('shop.html', p=product)
#     else:
#         return redirect(url_for('index.html'))

@app.route('/shop/<int:product_id>')
def indPost(product_id):
    product = Product.query.get(product_id)
    if product:
        p = product.to_dict() 
        return {
            'status': 'ok',
            'data': p,
            'item_count': 1 
        }
    else:
        return {
            'status': 'error',
            'message': 'Product not found'
        }, 404 