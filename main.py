from flask import Flask, render_template, url_for
from werkzeug.utils import redirect
import sqlalchemy
from data.jobs import Jobs
from data.users import User
from data import db_session
from data.db_session import create_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/users.db")


@app.route("/")
def work_log():
    db_sess = create_session()
    return render_template("work_logs.html", jobs=db_sess.query(Jobs).all(), users=db_sess.query(User).all())


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
