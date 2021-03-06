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
- Set the username and password used for Social Catfish.
- Apply DB migrations: `$ alembic upgrade head`.


## Usage

Run the flask application defined in `app.py`. See [Flask deployment options](http://flask.pocoo.org/docs/1.0/deploying/).

Note: Dates and times are displayed in UTC.


## Using a proxy

All the requests sent by this application are made through the `requests` module.
You can configure proxies by setting some environment variables.
See [Requests Documentation > Advanced Usage > Proxies](http://docs.python-requests.org/en/master/user/advanced/#proxies).


## API endpoints

- `/api/search/<param>[/rescrap]`

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
        "name": "John Doe",
        "gender": "Male",
        "location": "Buenos Aires, Argentina",
        "possible_names": [
          "John Doe One",
          "John Doe Two"
        ],
        "photos": [
          "http://imagehost.com/1.jpg",
          "http://imagehost.com/1.jpg"
        ],
        "phone_numbers": [
          "+54 9 11 1111-1111",
          "+54 9 11 2222-2222"
        ],
        "locations": [
          "Buenos Aires, Argentina",
          "Cabudare, Venezuela"
        ],
        "urls": [
          "http://twitter.com/johndoe",
          "http://facebook.com/johndoe"
        ],
        "relationships": [
          "Jane Doe",
          "Joe Blow"
        ],
        "usernames": [
          "john_doe_one",
          "john_doe_two"
        ]
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
