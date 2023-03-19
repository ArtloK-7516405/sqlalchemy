from flask import Flask, render_template, url_for
from werkzeug.utils import redirect

from data.jobs import Jobs
from data.users import User
from data import db_session
from forms.user import RegisterForm
from data.db_session import create_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/users.db")

@app.route('/')
def title():
    return '''Миссия Колонизация Марса'''


@app.route("/work")
def work_log():
    db_sess = create_session()
    return render_template("work_logs.html", jobs=db_sess.query(Jobs).all(), users=db_sess.query(User).all())

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)




if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
