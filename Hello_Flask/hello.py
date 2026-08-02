from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)

# @app.route("/")
# def index():
#     return "Hello World!"
#
# @app.route("/username/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello, {name}{number}!"

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
            '<p>This is a Paragraph</p>'\
            '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKRyzzog1DNrV7hpE6A8AZFb7yoyO3YMixsY9D_DZ9p3AfY2RKp4H9u8CL&s=10"  width=200>'
# Different routes using the app.route decorator
@app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
def bye():
    return "Ba Ba Bye"

#advanced Python Decorators Functions
class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

    def is_authenticated_decorator(function):
        def wrapper(*args, **kwargs):
            if args[0].is_logged_in == True:
                function(args[0])
        return wrapper
    @is_authenticated_decorator
    def create_blog_post(user):
        print(f"This is {user.name}'s new blog post")

new_user = User("Pradeep")
new_user.is_logged_in = True
# create_blog_post(new_user)

if __name__ == "__main__":
    app.run(debug=True)