# RESTful API Documentation

Documentation for a RESTful API powered by Flask and SQLite. This API allows you to perform CRUD (Create, Read, Update, Delete) operations on a "person" resource. 
This API is a submission for the 2nd Stage of the Backend Track of HNG Internship 2023.

## Table of Contents
- [Endpoints](#endpoints)
- [Request/Response Formats](#requestresponse-formats)
- [Sample Usage](#sample-usage)

## Endpoints

### 1. Introduction
- **URL**: `/`
- **Method**: `GET`
- **Description**: Get a welcome message.

### 2. Create New Person
- **URL**: `/api`
- **Method**: `POST`
- **Description**: Create a new person.
- **Request Body**:
  - JSON data with a "name" field (e.g., `{"name": "Mark Essien"}`)
- **Response**:
  - Successful Response (HTTP Status Code: 201 Created):
    ```json
    {
        "message": "'Mark Essien' was added successfully"
    }
    ```
  - Error Response (HTTP Status Code: 400 Bad Request):
    ```json
    {
        "message": "Name is required"
    }
    ```

### 3. Get, Update, or Delete a Single Person by ID
- **URL**: `/api/<int:id>`
- **Methods**: `GET`, `PUT`, `DELETE`
- **Description**: Retrieve, update, or delete a person by their ID.
- **GET Response**:
  - Successful Response (HTTP Status Code: 200 OK):
    ```json
    {
        "id": 1,
        "name": "Mark Essien"
    }
    ```
  - Error Response (HTTP Status Code: 404 Not Found):
    ```json
    {
        "message": "Person not found"
    }
    ```
- **PUT Request Body**:
  - JSON data with a "name" field for updating (e.g., `{"name": "Peter Obi"}`)
- **PUT Response**:
  - Successful Response (HTTP Status Code: 200 OK):
    ```json
    {
        "message": "Person updated successfully"
    }
    ```
  - Error Response (HTTP Status Code: 400 Bad Request):
    ```json
    {
        "message": "Name is required"
    }
    ```
- **DELETE Response**:
  - Successful Response (HTTP Status Code: 200 OK):
    ```json
    {
        "message": "Person deleted successfully"
    }
    ```

### 4. Get Names of All People
- **URL**: `/api/all`
- **Method**: `GET`
- **Description**: Retrieve the names of all people in the database.
- **Response**:
  - Successful Response (HTTP Status Code: 200 OK):
    ```json
    [
        {
            "id": 1,
            "name": "Mark Essien"
        },
        {
            "id": 2,
            "name": "Gojo Satoru"
        },
        {
            "id": 3,
            "name": "Peter Obi"
        }
        ...
    ]
    ```
  - Error Response (HTTP Status Code: 500 Internal Server Error):
    ```json
    {
        "error": "Internal Server Error Message"
    }
    ```

## Request/Response Formats

- **Request Format**: All requests to this API should use the `application/json` content type with JSON-formatted data in the request body.

- **Response Format**: All responses from this API are in JSON format.

## Sample Usage

Here are some sample API usage scenarios using `curl` commands:

- **Create a New Person**:
  ```shell
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Mark Essien"}' http://royaleonyeama.pythonanywhere.com/pi

- **Retrieve a Person by ID**:
curl http://royaleonyeama.pythonanywhere.com/api/1

- **Update a Person by ID**:
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Jane Smith"}' http://royaleonyeama.pythonanywhere.com/api/1

- **Delete a Person by ID**:
curl -X DELETE http://royaleonyeama.pythonanywhere.com/api/1
