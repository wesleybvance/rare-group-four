import sqlite3
import json
from models import Comment

def get_comments_by_post(post_id):
    """METHOD FOR GETTING COMMENTS
    BY POST ID"""

    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        #SQL Query to database - select
        # comment data by post_id filter
        db_cursor.execute("""
        select
            c.id,
            c.author_id,
            c.post_id,
            c.content
        from Comment c
        WHERE c.post_id = ?
        """, (post_id, ))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['author_id'], row['post_id'],
                              row['content'])
            comments.append(comment.__dict__)

    return comments
