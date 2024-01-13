from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId


def configure_routes(app):
    mongo_uri = 'mongodb://localhost:27017/'
    client = MongoClient(mongo_uri)
    db = client['mydatabase']

    # Routes
    @app.route('/')
    def index():
        return jsonify(message="Welcome to the Flask MongoDB app!")

    # Create
    @app.route('/post', methods=['POST'])
    def add_item():
        item = request.json
        db.mycollection.insert_one(item)  # Replace 'mycollection' with your collection name
        return jsonify(message="Item added successfully!"), 201

    # Read
    @app.route('/get', methods=['GET'])
    def get_items():
        items = list(db.mycollection.find())  # Replace 'mycollection' with your collection name
        for item in items:
            item["_id"] = str(item["_id"])
        return jsonify(items)

    # Update
    @app.route('/update/<id>', methods=['PUT'])
    def update_item(id):
        db.mycollection.update_one({"_id": ObjectId(id)}, {"$set": request.json})  # Replace 'mycollection'
        return jsonify(message="Item updated successfully!")

    # Delete
    @app.route('/delete/<id>', methods=['DELETE'])
    def delete_item(id):
        db.mycollection.delete_one({"_id": ObjectId(id)})  # Replace 'mycollection'
        return jsonify(message="Item deleted successfully!")

