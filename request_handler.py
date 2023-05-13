from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from views.user import create_user, login_user
from views import get_all_users, get_single_user, update_user, delete_user, get_user_by_email
from views import (
    get_all_posts,
    get_single_post,
    update_post,
    delete_post,
    create_post,
    get_post_by_category
)
from views import (
    get_all_categories,
    create_category,
    get_single_category,
    delete_category,
    update_category
)
from views import create_comment, get_all_comments, get_single_comment, delete_comment
from views import update_comment


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle GET requests to the server"""
        self._set_headers(200)
        response = {}
        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            (resource, id) = parsed
            if resource == "categories":
                if id is not None:
                    response = get_single_category(id)

                else:
                    response = get_all_categories()

            if resource == "users":
                if id is not None:
                    response = get_single_user(id)
                else:
                    response = get_all_users()

            if resource == "posts":
                if id is not None:
                    response = get_single_post(id)
                else:
                    response = get_all_posts()

            if resource == "comments":
                if id is not None:
                    response = get_single_comment(id)
                else:
                    response = get_all_comments()

        else:
            (resource, query) = parsed

            if query.get('category_id') and resource == 'posts':
                response = get_post_by_category(query['category_id'][0])

            if query.get('email') and resource == 'users':
                response = get_user_by_email(query['email'][0])

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = {}
        resource, _ = self.parse_url(self.path)

        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'categories':
            response = create_category(post_body)
        if resource == 'posts':
            response = create_post(post_body)
        if resource == 'comments':
            response = create_comment(post_body)

        # self.wfile.write(f"{response}".encode())
        # self.wfile.write(response.encode())
        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        success = False

        if resource == "users":
            success = update_user(id, post_body)

        if resource == "posts":
            success = update_post(id, post_body)

        if resource == "comments":
            success = update_comment(id, post_body)

        if resource == "categories":
            success = update_category(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)

        if resource == "users":
            delete_user(id)

        if resource == "posts":
            delete_post(id)

        if resource == "comments":
            delete_comment(id)

        if resource == "categories":
            delete_category(id)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
