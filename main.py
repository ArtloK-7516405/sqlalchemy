from flask import Flask, render_template
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
    # app.run()
    # 1-------------------------------------------------
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    # 2-------------------------------------------------
    user = User()
    user.surname = "Betsy"
    user.name = "Garven"
    user.age = 23
    user.position = "medic"
    user.speciality = "biologist"
    user.address = "module_2"
    user.email = "med_garv@mars.org"
    user.hashed_password = "gyppokrat"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = 'collection and verification of analyses'
    job.work_size = 12
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    # 3-------------------------------------------------
    user = User()
    user.surname = "Henry"
    user.name = "Sourdly"
    user.age = 24
    user.position = "navigator"
    user.speciality = "mechanic"
    user.address = "module_3"
    user.email = "kiborg_mach@mars.org"
    user.hashed_password = "legnevdie"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = 'repair of the life support system №1'
    job.work_size = 18
    job.collaborators = '1, 3'
    job.is_finished = True
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()

    # 4-------------------------------------------------
    user = User()
    user.surname = "ArtloK"
    user.name = "Mercenari"
    user.age = 22
    user.position = "cooker"
    user.speciality = "progromist"
    user.address = "module_0"
    user.email = "an7516405@gmail.com"
    user.hashed_password = "qwerty"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = 'cooking the daily diet'
    job.work_size = 13
    job.collaborators = '4'
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()
