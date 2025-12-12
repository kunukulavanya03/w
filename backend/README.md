# Backend API for w

## Installation

1. Clone the repository
2. Install the dependencies using `pip install -r requirements.txt`
3. Create a new file named `.env` and add the environment variables
4. Run the application using `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Documentation

### Register

* **URL:** `/api/register`
* **Method:** `POST`
* **Request Body:** `username`, `email`, `password`
* **Response:** `id`, `username`, `email`

### Login

* **URL:** `/api/login`
* **Method:** `POST`
* **Request Body:** `username`, `password`
* **Response:** `id`, `token`

### Get Data

* **URL:** `/api/data`
* **Method:** `GET`
* **Response:** `data`

### Create Data

* **URL:** `/api/data`
* **Method:** `POST`
* **Request Body:** `name`
* **Response:** `id`, `name`

### Get Data by ID

* **URL:** `/api/data/{id}`
* **Method:** `GET`
* **Response:** `id`, `name`

### Update Data

* **URL:** `/api/data/{id}`
* **Method:** `PUT`
* **Request Body:** `name`
* **Response:** `id`, `name`

### Delete Data

* **URL:** `/api/data/{id}`
* **Method:** `DELETE`
* **Response:** `message`
