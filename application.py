#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

## import CRUD Operations 
from database_setup import Base, User, Category, Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

## Create session and connect to DB
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/')
@app.route('/catalog/')
def catalog():
        categories = session.query(Category).all()
        # lastItems = session.query(Item).order_by(Item.time)
        return render_template('catalog.html', categories=categories)

@app.route('/catalog/<category>/items')
def category(category):
        categories = session.query(Category).all()
        category = session.query(Item).filter_by(category = category).one()
        return render_template('category.html', categories=categories, category=category)

@app.route('/catalog/<itemname>/', methods=['GET', 'POST'])
def showItem(itemname):
    item = session.query(Item).filter_by(itemname = itemname).one()
    return render_template('item.html', item=item)
# Task 1: Create route for newMenuItem function here

@app.route('/catalog/item/new/', methods=['GET', 'POST'])
def newItem():
    categories = session.query(Category).all()
    if request.method == 'POST':
            newItem = Item(itemname = request.form['name'], description = request.form['description'], category = request.form['category'])
            session.add(newItem)
            session.commit()
            return redirect(url_for('catalog'))
    else:
            return render_template('newitem.html', categories=categories)
    return "page to create an item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here

@app.route('/catalog/<itemname>/edit/', methods=['GET', 'POST'])
def editItem(itemname):
    editItem = session.query(Item).filter_by(itemname = itemname).one()
    categories = session.query(Category).all()
    if request.method == 'POST':
            editItem = Item(itemname = request.form['name'], description = request.form['description'], category = request.form['category'])
            session.add(editItem)
            session.commit()
            flash("item was edited")
            return redirect(url_for('catalog'))
    else:
            return render_template('edititem.html', editItem = editItem)
    return "page to edit an item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/catalog/<itemname>/delete/', methods=['GET', 'POST'])
def deleteItem(itemname):
    deleteItem = session.query(Item).filter_by(itemname = itemname).one()
    if request.method == 'POST':
            session.delete(deleteItem)
            session.commit()
            flash("item was deleted")
            return redirect(url_for('catalog'))
    else:
            return render_template('deleteitem.html', itemname = itemname)
    return "page to delete an item. Task 3 complete!"



if __name__ == '__main__':
        app.secret_key = 'super_secret_key'
        app.debug = True
        app.run(host = '0.0.0.0', port = 5000)