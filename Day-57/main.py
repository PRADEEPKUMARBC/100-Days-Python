from flask import Flask, render_template, request
import random
import datetime
import requests

app = Flask(__name__)
@app.route('/')
def index():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    name = request.args.get('name')
    gender_response = requests.get('https://api.agify.io?name={name}'.format(name=random_number))
    gender_data = gender_response.json()
    # gender = gender_data['gender']
    age_url = f"https://api.agify.io?name={name}"
    age_response =  requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    return render_template('blog.html', person_name=name, gender=gender, age=age)

@app.route('/blog')
def blog():
    blog_url = "https://api.agify.io?name={name}"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)