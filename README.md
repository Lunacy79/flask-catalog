# Catalog Project

## A web application that provides a list of items within a variety of categories and integrate third party user registration and authentication

The project runs on a virtual machine

This project uses Python version 2

The web app uses an SQL database server

To run the project you need to install VirtualBox and Vagrant, download the udacity-fullstack-vm (https://github.com/udacity/fullstack-nanodegree-vm) and start the virtual machine

After that you can ssh into the virtual machine and cd into /vagrant/catalog

Then run the application with python application.py

You can access the JSON API at:

* /catalog/items/JSON:

    * result: all items

    * {
        "Items": [
            {
            "category_id": 1, 
            "description": "Cute mamal with paws", 
            "id": 1, 
            "name": "Cat"
            }, 
            ...
        }


* /catalog/item/[item-id]/JSON:

    * result: one item

    * {
        "item": {
            "category_id": 1, 
            "description": "Cute mamal with paws", 
            "id": 1, 
            "name": "Cat"
        }
    }

* /catalog/[category-id]/JSON:

    * result: all items of one category

    * {
        "Items": [
            {
            "category_id": 1, 
            "description": "Cute mamal with paws", 
            "id": 1, 
            "name": "Cat"
            }, 
            ...
        }
