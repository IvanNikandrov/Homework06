from os import getenv
from flask import Flask, render_template, request, redirect
from flask_migrate import Migrate
from models import db, Post

app = Flask(__name__)

config_name = 'config.%s' % getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(config_name)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)




@app.route("/")
def index_page():
    posts = Post.query.all()
    return render_template('index.html', posts=posts, title='Статьи: ')


@app.route("/add_post", methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        post = Post(name=request.form["name"])
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    return render_template('add_post.html', title='Добавить статью')


if __name__ == '__main__':
    app.run()
