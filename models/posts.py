# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-class-docstring
# pylint: disable=redefined-builtin



class Post():
    def __init__(self, id, user_id, category_id, title,
                 publication_date, image_url, content, approved):
        self.user_id = user_id
        self.id = id
        self.category_id = category_id
        self.title = title
        self.publication_date = publication_date
        self.image_url = image_url
        self.content = content
        self.approved = approved
