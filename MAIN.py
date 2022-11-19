import os
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_bcrypt import generate_password_hash, check_password_hash
# from database import Users, House
from os import path

from sqlalchemy.testing import db
from werkzeug.utils import secure_filename
import pandas as pd
# from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Table

# from flask import Flask, Session
# from flask.ext.session import Session
#
# SESSION_TYPE = 'memcache'
#
# app = Flask(__name__)
# sess = Session()
#
# app = Flask(__name__)
# app.secret_key = "bnvsdnvsfvdvkvnjvdvdkbvdsc"

#
# establish the connection with the engine object
# with engine.connect() as conn:
# Create the engine to connect to the inbuilt
# sqllite database\
engine = create_engine("sqlite+pysqlite:///:memory:")

# # Read data from CSV which will be
# # loaded as a dataframe object
# data = pandas.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Kenya.csv')
# data1 = pandas.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Naija.csv')
#
# # print the sample of a dataframe
# print(data.head())
# print(data1.head())
#
# # Write data into the table in sqllite database
# data.to_sql('Track_data', engine)
# data1.to_sql('Track_data1', engine)
#
# with engine.connect() as conn:
#     # let's select the column credit_history
#     # from the data table
#     result = conn.execute(text("SELECT track_id FROM Track_data"))
#     result1 = conn.execute(text("SELECT album FROM Track_data1"))

# print the result
# for row in result:
#     print(row.track_id)
# for row in result1:
#     print(row.album)

# engine = create_engine('sqlite:////tmp/test.db')

# TESTER
# metadata = MetaData(bind=engine)
# users = Table('Track_data', metadata, autoload=True)
# con = engine.connect()
# # con.execute(users.insert(), name='admin', email='admin@localhost')
# #
# #
# with engine.connect() as conn:
#     # let's select the column credit_history
#     # from the data table
#     result3 = engine.execute('select energy from Track_data where track_id =="4B9Rhu9Xdq3Vo1hfLJQh9p"').first()
#     result4 = engine.execute('select liveness from Track_data where track_id =="4B9Rhu9Xdq3Vo1hfLJQh9p"').first()
#     result5 = engine.execute('select danceability from Track_data where track_id =="4B9Rhu9Xdq3Vo1hfLJQh9p"').first()
#     result6 = engine.execute('select speechiness from Track_data where track_id =="4B9Rhu9Xdq3Vo1hfLJQh9p"').first()
#     # result7 = engine.execute('select speechiness from Track_data where speechiness >= 0.5').first()
#     # user = engine.execute(db('Track_data').filter_by(track_id="1QgM3SejXDyHkqt0guA4TX")).one()
#     # s2 = engine.execute(users.query.filter(users.track_id == '1QgM3SejXDyHkqt0guA4TX')).all()
#     # print(user)
#     print("The liveness is", result4)
#     print("The energy is", result3)
#     print("The danceability is", result5)
#     print("The speechiness is", result6)
#
#     for danceability in result5:
#         if danceability >= 0.6 :
#             print(1)
#         else:
#             print(0)
#     for liveness in result4:
#         if liveness >= 0.5 :
#             print(1)
#         else:
#             print(0)
#     for energy in result3:
#         if energy >= 0.4:
#             print(1)
#         else:
#             print(0)
#     for speechiness in result6:
#         if speechiness >= 0.4:
#             print(1)
#         else:
#             print(0)
#     sumation = danceability + liveness + energy + speechiness
#     print(sumation)
#     if sumation < 0.7:
#         print("flop")
#     elif sumation > 1.5:
#         print("hit")
#     else:
#         print("possibly")

# print the result


app = Flask(__name__)

app.debug = True


@app.route('/', methods=["POST", "GET"])
def url():
    if request.method == "POST":
        run = request.form["url"]

        # Read data from CSV which will be
        # loaded as a dataframe object
        data = pd.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Kenya.csv')
        data1 = pd.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Naija.csv')

        # print the sample of a dataframe
        # print(data.head())
        # print(data1.head())

        # Write data into the table in sqllite database
        data.to_sql('Track_data', engine)
        data1.to_sql('Track_data1', engine)

        with engine.connect() as conn:
            # let's select the column credit_history
            # from the data table
            result = conn.execute(text("SELECT track_id FROM Track_data"))
            result1 = conn.execute(text("SELECT album FROM Track_data1"))

        metadata = MetaData(bind=engine)
        users = Table('Track_data', metadata, autoload=True)
        con = engine.connect()
        # con.execute(users.insert(), name='admin', email='admin@localhost')
        #
        #
        with engine.connect() as conn:
            # let's select the column credit_history
            # from the data table
            # result3 = engine.execute(
            #     'select energy from Track_data where track_id =="4B9Rhu9Xdq3Vo1hfLJQh9p"').first()
            # result4 = engine.execute(
            #     'select liveness from Track_data where track_id =="4B9Rhu9Xdq3Vo1hfLJQh9p"').first()
            # result5 = engine.execute(
            #     'select danceability from Track_data where track_id =="4B9Rhu9Xdq3Vo1hfLJQh9p"').first()
            # result6 = engine.execute(
            #     'select speechiness from Track_data where track_id =="4B9Rhu9Xdq3Vo1hfLJQh9p"').first()

            # result7 = engine.execute('select speechiness from Track_data where speechiness >= 0.5').first()
            # user = engine.execute(db('Track_data').filter_by(track_id='run')).one()
            # # s2 = engine.execute(users.track_id.filter(users.track_id == '1QgM3SejXDyHkqt0guA4TX')).all()
            # # print(s2)
            # print(user)
            print(run)
            # ret = users.query(exists().where(track_id.Track_data == run)).scalar()
            # result5 = engine.execute(
                    # 'select danceability >= 0.5  from Track_data where  track_id  =={}'.format(run)).first()
            # result4 = engine.execute(
            #         'select liveness >= 0.3 from Track_data where track_id =="6JR3F5nXtkkHwiCHIeYqSC"').first()
            # result3 = engine.execute(
            #         'select energy >= 0.4  from Track_data where track_id =="6JR3F5nXtkkHwiCHIeYqSC" ').first()
            # result6 = engine.execute(
            #         'select speechiness >= 0.3 from Track_data where track_id =="6JR3F5nXtkkHwiCHIeYqSC"  ').first()

            result6 = pd.read_sql('Select danceability from Track_data where track_id=?', conn,
                              params=(run,))
            result7 = pd.read_sql('Select speechiness from Track_data where track_id=?', conn,
                                  params=(run,))
            result8 = pd.read_sql('Select liveness from Track_data where track_id=?', conn,
                                  params=(run,))
            result9 = pd.read_sql('Select energy from Track_data where track_id=?', conn,
                                  params=(run,))

            danceability = result6['danceability'][0]
            speechiness = result7['speechiness'][0]
            liveness = result8['liveness'][0]
            energy = result9['energy'][0]

            # print(run)
            # print("The liveness is", result4)
            # print("The energy is", result3)
            # print("The speechiness is", result6)

            if danceability >= 0.5:
                danceability = 1
                print(1)
            else:
                danceability = 0
                print(0)
            if liveness >= 0.3:
                liveness = 1
                print(1)
            else:
                liveness = 0
                print(0)

            if energy >= 0.3:
                energy = 1
                print(1)
            else:
                energy = 0
                print(0)

            if speechiness >= 0.3:
                speechiness = 1
                print(1)
            else:
                speechiness = 0
                print(0)

            # for liveness in result4:
            #     if liveness >= 0.5:
            #         print(1)
            #     else:
            #         print(0)
            # for energy in result3:
            #     if energy >= 0.4:
            #         print(1)
            #     else:
            #         print(0)
            # for speechiness in result6:
            #     if speechiness >= 0.4:
            #         print(1)
            #     else:
            #         print(0)
            sumation = danceability + liveness + energy + speechiness
            print(sumation)
            if sumation < 2:
                print("flop")
                return render_template("flop.html")
            elif sumation == 2:
                print("possibly a hit")
                return render_template("possibly.html")
            elif sumation == 4:
                print("HIT MAKER")
                return render_template("hitmaker.html")
            else:
                print("hit")
                return render_template("hit.html")
        # # sqllite database\
        # engine1 = create_engine("sqlite+pysqlite:///:memory:")
        #
        # # Read data from CSV which will be
        # # loaded as a dataframe object
        # data_kenya = pandas.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Kenya.csv')
        # data_naija = pandas.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Naija.csv')
        #
        # # print the sample of a dataframe
        # # print(data.head())
        # # print(data1.head())
        #
        # # Write data into the table in sqllite database
        # data_kenya.to_sql('Track_data', engine1)
        # data_naija.to_sql('Track_data1', engine1)
        #
        # with engine1.connect() as CONN:
        #
        #     # let's select the column credit_history
        #     # from the data table
        #     result = CONN.execute(text("SELECT track_id FROM Track_data"))
        #     result1 = CONN.execute(text("SELECT album FROM Track_data1"))
        # # To test print the result
        # # for row in result:
        # #     print(row.track_id)
        # # for row in result1:
        # #     print(row.album)
        #
        # # /////////////////////////////////////
        #
        # # engine = create_engine('sqlite:////tmp/test.db')
        # meta_data = MetaData(bind=engine1)
        # users = Table('Track_data', meta_data, autoload=True)
        # CONN = engine1.connect()
        # # con.execute(users.insert(), name='admin', email='admin@localhost')
        #
        # with engine1.connect() as CONN:
        #     # let's select the column credit_history
        #     # from the data table
        #     #     result3 = engine.execute('select * from Track_data where artist =="Nyashinski"').first()
        #     result3 = engine1.execute('select energy from Track_data where track_id =="1QgM3SejXDyHkqt0guA4TX"').first()
        #     result4 = engine1.execute(
        #         'select liveness from Track_data where track_id =="1QgM3SejXDyHkqt0guA4TX"').first()
        #     result5 = engine1.execute(
        #         'select danceability from Track_data where track_id =="1QgM3SejXDyHkqt0guA4TX"').first()
        #     result6 = engine1.execute(
        #         'select speechiness from Track_data where track_id =="1QgM3SejXDyHkqt0guA4TX"').first()
        #     # result7 = engine.execute('select speechiness from Track_data where speechiness >= 0.5').first()
        #     print("The liveness is", result4)
        #     print("The energy is", result3)
        #     print("The danceability is", result5)
        #     print("The speechiness is", result6)
        #     # /////////////////////////////
        #     with engine1.connect() as CONN:
        #         dancing = engine1.execute(
        #             'select track_id =="1QgM3SejXDyHkqt0guA4TX" from Track_data where danceability >= 0.5').first()
        #
        #         live = engine1.execute(
        #             'select track_id =="1QgM3SejXDyHkqt0guA4TX"  from Track_data where liveness >= 0.4').first()
        #         energyopor = engine1.execute(
        #             'select track_id =="1QgM3SejXDyHkqt0guA4TX"  from Track_data where energy >= 0.4').first()
        #         speech = engine1.execute(
        #             'select track_id =="1QgM3SejXDyHkqt0guA4TX"  from Track_data where speechiness >= 0.4').first()
        #     # result11 = engine.execute(
        #     # 'SELECT @runs := run FROM Track_data WHERE track_id == runs  AND speechiness >0.4').first()
        #
        #     # print the result
        #         print(dancing)
        #         print(live)
        #         print(energyopor)
        #         print(speech)
        #     # variables = ["result7", "result3", "result5", "result6"]
        #         for danceability in dancing:
        #             if danceability == 1:
        #                 print("danceability is good")
        #             else:
        #                 print("danceability is bad")
        #         for liveness in live:
        #             if liveness == 1:
        #                 print("liveness is good")
        #             else:
        #                 print("liveness is bad")
        #         for energy in energyopor:
        #             if energy == 1:
        #                 print("energy is good")
        #             else:
        #                 print("energy is bad")
        #         for speechiness in speech:
        #             if speechiness == 1:
        #                 print("speechiness is good")
        #             else:
        #                 print("speechiness is bad")
        #         total = danceability + liveness + energy + speechiness
        #         if total == 2:
        #             print("possibly")
        #         elif total > 2:
        #             print("hit")
        #         else:
        #             print("flop")

    return render_template("predictor.html")
@app.route('/flop')
def flop():

    return render_template('flop.html')
@app.route('/possibly')
def possibly():

    return render_template('possibly.html')
@app.route('/hit')
def hit():

    return render_template('hit.html')


@app.route('/hitmaker')
def hitmaker():

    return render_template('hitmaker.html')
@app.route('/feedback')
def feedback():

    return render_template('feedback.html')
@app.route('/table')
def table():
    data = pd.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Kenya.csv')
    data1 = pd.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Naija.csv')
    data.to_sql('Track_data', engine)
    data1.to_sql('Track_data1', engine)

    with engine.connect() as conn:
        # let's select the column credit_history
        # from the data table
        result = conn.execute(text("SELECT track_id FROM Track_data"))
        result1 = conn.execute(text("SELECT album FROM Track_data1"))

    metadata = MetaData(bind=engine)
    users = Table('Track_data', metadata, autoload=True)
    con = engine.connect()

    return render_template('table.html', query= engine.execute('select * from Track_data').all())


if __name__ == '__main__':
    # app.config['SESSION_TYPE'] = 'memcached'
    # app.config['SECRET_KEY'] = 'super secret key'
    # sess = Session()
    app.debug = True
    app.run()
