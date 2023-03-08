
# communication-layer

this is communication layer of [user](https://github.com/Zahra-Nasiri/user-service) and [book](https://github.com/Zahra-Nasiri/book-service) services of library microservice project.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`user_service_url`

`book_service_url`


## Tech Stack

* python
* fastapi
* mongodb




## Installation

Install my-project with pip

```bash
  python -m venv venv
  venv\scripts\avtivate
  pip install -r requirements.txt
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/Zahra-Nasiri/communication-layer
```

Go to the project directory

```bash
  cd communication-layer
```

Install dependencies

```bash
  pip install requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

## API Reference

#### Register a user

```http
  POST /register
```

#### Login a user

```http
  POST /login
```


#### Update a user

```http
  PATCH /{uid}
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. Your token |


#### Get all books

```http
  GET /
```

#### Create a book by admin

```http
  POST /
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. Admin token |


#### Get a single book by id

```http
  GET /{book_id}
```


#### Delete a book by admin

```http
  DELETE /{bok_id}
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. Admin token |


#### Update a book by admin

```http
  PATCH /{bok_id}
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. Admin token |


#### Rent a book by user

```http
  POST /{bok_id}
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. your token |


## Authors

- [Zahra-Nasiri](https://github.com/Zahra-Nasiri)


## 🚀 About Me
I'm a  back-end developer...

you can read more about me on my [linkedin account](https://www.linkedin.com/in/zahra-nasirmohammadi-73584b241/)
