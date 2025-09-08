# M-CCIA Introductory Course on Networks and Connectivity [IADE](https://www.iade.europeia.pt/) <!-- omit in toc -->

## Class 1 <!-- omit in toc -->
- [Sample API](#sample-api)

## Sample API

This repository contains a simple Python REST API using FastAPI. Test it with the following commands:

```bash
# Setup the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
fastapi dev src/sample_server.py
```

Endpoints:

- `GET /users`: Returns a list of users.
- `GET /users/{user_id}`: Returns details of a specific user.
- `POST /users`: Creates a new user.

Test with curl:

```bash
# Get all users
curl -X GET "http://localhost:8000/users"

# Get user with ID 1
curl -X GET "http://localhost:8000/users/1"

# Create a new user
curl -X POST "http://localhost:8000/users" -H "Content-Type: application/json" -d '{"id":3,"name":"Trudy","email":"trudy@example.com"}'
```

## Challenge 1: create your own API

Create a new FastAPI application that implements a simple CRUD (Create, Read, Update, Delete) API for managing a collection of items (e.g., books, movies, tasks). Implement the following endpoints:

- `GET /items`: Returns a list of all items.
- `GET /items/{item_id}`: Returns details of a specific item.
- `POST /items`: Creates a new item.
- `PUT /items/{item_id}`: Updates an existing item.
- `DELETE /items/{item_id}`: Deletes an item.

## Challenge 2: API client

Build a Python client that interacts with the API you created in Challenge 1. The client should provide functions to perform all CRUD operations and handle responses and errors appropriately.

## Challenge 3: Image Annotation API

Develop an application that allows users to draw images and see their AI generated captions using an image annotation model.

There's a couple of help files in this repo:

- `annotations.py`: A starting point for the image annotation API. You can modify this file to implement a REST API that processes image uploads and returns annotations.
- `drawing.py`: A utility to draw images. Try to upload the drawn images to your API and get annotations (say, during the save operation). Show the annotation as a caption on the label below the image.
