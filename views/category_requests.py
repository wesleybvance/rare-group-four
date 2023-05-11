import sqlite3
import json
from models import Category


def get_all_categories():
    """Get all the categories"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        """)

        categories = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    return categories


def create_category(new_category):
    """Create a new category"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            ( label )
        VALUES
            ( ? );
        """, (new_category['label'], ))

        id = db_cursor.lastrowid
        new_category['id'] = id

    return new_category


def get_single_category(id):
    """Get a single category"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        WHERE c.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        category = Category(data['id'], data['label'])

    return category.__dict__
