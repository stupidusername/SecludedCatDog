# SecludedCatDog

![CatDog](catdog.png)


## Requirements

- Python >= 3.7 (Tested on 3.7.2).
- Pip packages listed on `requirements.txt`.
- A RDBMS supported by SQLAlchemy. See [SQLAlchemy 1.2 Documentation > Dialects](https://docs.sqlalchemy.org/en/latest/dialects/index.html).


## Installation

- Create a `config.ini`. Use `config-example.ini` as reference.
- Change the database DSN.
- Change the secret key used for cookies.
- Set the user and password used for Social Catfish.
- Apply DB migrations: `$ alembic upgrade head`.


## Usage

Run the flask application defined in `app.py`. See [Flask deployment options](http://flask.pocoo.org/docs/1.0/deploying/).

Note: Dates and times are displayed in UTC.


## API endpoints

- `/search/<param>[/rescrap]`

  Search an identity by its email or phone number. If the identity is already stored in the database the result will be retrieved from it.
  Adding `/rescrap` at the end of the request path the information will queried again and the new results will be saved in the database.

  - Params:

    - `param`: Email or phone number of the identity to be searched. If this parameter contains `"@"` it will be treated as an email.

  - Response example of a successful query.

    ```
    {
      "success": true,
      "create_datetime": "2019-01-22 20:21:33",
      "identity": {
        "email": "johndoe@mail.com",
        "phone_number": "1111111111",
        ...
      }
    }
    ```

  - Response example of a unsuccessful query.

    ```
    {
      "success": false,
      "error": "Error message",
    }
    ```
