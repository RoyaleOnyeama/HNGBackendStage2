# HNGBackendStage2
Stage 2 Task: CRUD RESTful API - Backend Track - HNG Internship 2023
# HNG Internship 2023 - Stage 2 Backend Task

This README will guide you through setting up and using our simple RESTful API for managing a persons record.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Using the API](#using-the-api)
- [Sample Usage](#sample-usage)
- [API Endpoints](#api-endpoints)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- A code editor (e.g., Visual Studio Code) for editing code.
- A terminal or command prompt for running commands.

## Getting Started


# Clone this repository to your local machine
git clone https://github.com/your-username/hng-backend-stage2.git
cd hng-backend-stage2

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (macOS and Linux)
source venv/bin/activate

# Install the required Python packages
pip install ### Running the Application

Now that you have the project set up, follow these steps to run the API:


# Run the Flask application
python app.py
-r requirements.txt

You should see a message indicating that the app is running. The API is
now accessible at **http://royaleonyeama.pythonanywhere.com/**.

**Using the API**

The API allows you to perform CRUD operations on person records. Here\'s
how you can use it:

**Create a New Person**

To create a new person, make a POST request with JSON data containing
the person\'s name:

bashCopy code

curl -X POST -H \"Content-Type: application/json\" -d \'{\"name\":
\"John Doe\"}\' http://royaleonyeama.pythonanywhere.com/people

If successful, you\'ll receive a response indicating that the person was
added.

**Retrieve, Update, or Delete a Person by ID**

You can retrieve, update, or delete a person by their ID. Replace
**\<id\>** with the person\'s ID in the URL.

To retrieve a person by ID:

bashCopy code

curl http://royaleonyeama.pythonanywhere.com/people/\<id\>

To update a person by ID:

bashCopy code

curl -X PUT -H \"Content-Type: application/json\" -d \'{\"name\": \"Jane
Smith\"}\' http://royaleonyeama.pythonanywhere.com/people/\<id\>

To delete a person by ID:

bashCopy code

curl -X DELETE http://royaleonyeama.pythonanywhere.com/people/\<id\>

**Get Names of All People**

To retrieve the names of all people in the database:

bashCopy code

curl http://royaleonyeama.pythonanywhere.com/people/all


**API Endpoints**

For a complete list of API endpoints and their descriptions, see the
[API
Endpoints](https://chat.openai.com/c/71e37f09-b09d-484c-a6be-50289528dc0d#api-endpoints)
section in the
[Documentation](https://chat.openai.com/c/71e37f09-b09d-484c-a6be-50289528dc0d#documentation).

**Documentation**

You can find comprehensive documentation in the
[Documentation.md](https://chat.openai.com/c/Documentation.md) file in
this repository. It includes detailed information about each API
endpoint, request/response formats, and more.


