# Mount-Challenge

Coding Test: Simple Application for a Toy Store API

Backend: Django Framework, MySQL Database

## Installation

### Git clone

```bash
git clone https://github.com/Chihui8199/Mount-Challenge.git
```

# Backend Setup

## 1. Install Dependencies

- Python 3.9.0
- MYSQL Workbench

## 2. Setting Up the Virtual Environment

1. Set up a new virtual environment

```
python -m venv .venv
```

2. Activate the virtual environment

```
. .venv/bin/activate
```

3. Install required libraries

```
pip install -r requirements.txt
```

## 3. Set-up MySQL Workbench

1. Create new SQL connection (Remote)

   a. Connection Name:

   ```
   remote project_mount
   ```

   b. Hostname:

   ```
   remote-mount.cqrovybm8cek.us-east-1.rds.amazonaws.com
   ```

   c. Port:

   ```
   3306
   ```

   d. Username:

   ```
   admin
   ```

   e. Password:

   ```
   projectmount
   ```

   f. Default Schema:

   ```
   project_mount
   ```

## 4. Setting up Project

1. Migrate all the default Django tables to your MySQL schema.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

## 5. Running The Server

1. Start the Server

```
python manage.py runserver
```

2. Open http://localhost:8000

## 6. List of available API URLs

1. To view APIs available

   > http://127.0.0.1:8000/api/

2. To enter to admin dashboard

   > http://127.0.0.1:8000/admin

   - Username: admin
   - Password: admin

3. To view Toy API:

   > Get all toys: http://127.0.0.1:8000/api/toys

   > Get toy detail: http://127.0.0.1:8000/api/toys/Barbie

## 7. To run unit testing

```
python manage.py test
```

## 8. Testing API endpoints with Postman

1. Get Bearer token: You can either create a new superuser, log in to admin dashboard and get a new token. Else, you can
   use the one I have created

To create new superuser

```
python manage.py createsuperuser
```

Alternatively:
use this token:

```
Token 1a7c6c72cbd555127539919ba71ee58743ca12ea
```

2. Test API using Postman

   1. Get request for all toys

      - Change field to GET request: http://127.0.0.1:8000/api/toys/
      - Under the authorization tab, select API key under tab and update the Value field with the given bearer token
      ![](Guide%20Images/Get%20all%20Toys.png)

   2. Get request for a specfic toy
      - Change field to GET request: http://127.0.0.1:8000/api/toys/Bottle/
      - Under the authorization tab, select API key under tab and update the Value field with the given bearer token
      ![](Guide%20Images/Get%20Toy%20by%20name.png)
   3. Post request for a new toy
      - Change field to POST request: http://127.0.0.1:8000/api/toys/http://127.0.0.1:8000/api/toys/
      - Under the authorization tab, select API key under tab and update the Value field with the given bearer token
      - Populate the body field with the data given below
      ```
      {
      "toy_item": "Toy1000",
      "price": "2.10"
      }
      ```
      - ![](Guide%20Images/Post%20a%20new%20toy.png)
   4. Delete request for an existing toy
      - Change field to DELETE request: http://127.0.0.1:8000/api/toys/Toy1000/
      - Under the authorization tab, select API key under tab and update the Value field with the given bearer token
      ![](Guide%20Images/Delete%20toy%20by%20name.png)
