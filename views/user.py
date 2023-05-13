import sqlite3
import json
from datetime import date
from models import User


def login_user(user):
    """Checks for the user in the database

    Args:
        user (dict): Contains the username and password of the user trying to login

    Returns:
        json string: If the user was found will return valid boolean of True
                    and the user's id as the token
                     If the user was not found will return valid boolean False
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select id, username
            from Users
            where username = ?
            and password = ?
        """, (user['username'], user['password']))

        user_from_db = db_cursor.fetchone()

        if user_from_db is not None:
            response = {
                'valid': True,
                'token': user_from_db['id']
            }
        else:
            response = {
                'valid': False
            }

        return json.dumps(response)


def create_user(user):
    """Adds a user to the database when they register

    Args:
        user (dictionary): The dictionary passed to the register post request

    Returns:
        json string: Contains the token of the newly created user
    """
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Users (first_name, last_name, username, email, password, bio, created_on, active) values (?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            user['first_name'],
            user['last_name'],
            user['username'],
            user['email'],
            user['password'],
            user['bio'],
            date.today()
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })


def get_all_users():
    """gets all users in database
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT * FROM Users
        """)
        users = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(
                row["id"],
                row["first_name"],
                row["last_name"],
                row["email"],
                row["bio"],
                row["username"],
                row["password"],
                row["profile_image_url"],
                row["created_on"],
                row["active"]
            )

            users.append(user.serialized())

    return users


def get_single_user(id):
    """gets a single user by id
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT * FROM Users u
        WHERE u.id = ?
        """, (id, ))

        data = db_cursor.fetchone()
        user = User(
            data["id"],
            data["first_name"],
            data["last_name"],
            data["email"],
            data["bio"],
            data["username"],
            data["password"],
            data["profile_image_url"],
            data["created_on"],
            data["active"]
        )

        return user.serialized()


def update_user(id, new_user):
    """updates a user based off of the user id

    Args:
        id (integer): user.id
        new_user (object): new user information to update
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        UPDATE Users
            SET
                first_name = ?,
                last_name = ?,
                email = ?,
                bio = ?,
                username = ?,
                password = ?,
                profile_image_url = ?
        WHERE id = ?
        """, (new_user["first_name"], new_user["last_name"], new_user["email"],
              new_user["bio"], new_user["username"], new_user["password"],
              new_user["profile_image_url"], id, ))

        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        return False
    return True


def delete_user(id):
    """deletes a user based off of id
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE from Users WHERE id = ?
        """, (id, ))


def get_user_by_email(email):
    """get a user(s) by email address

    Args:
        email (str): email address
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        
        """)
