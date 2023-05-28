import os
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_bcrypt import generate_password_hash, check_password_hash
# from database import Users, House
from os import path
from werkzeug.utils import secure_filename
import pandas
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

# Read data from CSV which will be
# loaded as a dataframe object
data = pandas.read_csv(r'C:/Users/user/PycharmProjects/HitSongPredictor/Kenya.csv')
data1 = pandas.read_csv(r'C:/Users/user/PycharmProjects/HitSongPredictor/Naija.csv')

# print the sample of a dataframe
print(data.head())
print(data1.head())


# Write data into the table in sqllite database
data.to_sql('Track_data', engine)
data1.to_sql('Track_data1', engine)


with engine.connect() as conn:
# let's select the column credit_history
# from the data table
    result = conn.execute(text("SELECT track_id FROM Track_data"))
    result1 = conn.execute(text("SELECT album FROM Track_data1"))

# print the result
for row in result:
    print(row.track_id)
for row in result1:
    print(row.album)

# engine = create_engine('sqlite:////tmp/test.db')
metadata = MetaData(bind=engine)
users = Table('Track_data', metadata, autoload=True)
con = engine.connect()
# con.execute(users.insert(), name='admin', email='admin@localhost')


with engine.connect() as conn:
# let's select the column credit_history
# from the data table
#     result3 = engine.execute('select * from Track_data where artist =="Nyashinski"').first()
    result3 = engine.execute('select energy from Track_data where track_id =="2EISZ7FY6AkSP8ObzenBcB"').first()
    result4 = engine.execute('select liveness from Track_data where track_id =="2EISZ7FY6AkSP8ObzenBcB"').first()
    result5 = engine.execute('select danceability from Track_data where track_id =="2EISZ7FY6AkSP8ObzenBcB"').first()
    result6 = engine.execute('select speechiness from Track_data where track_id =="2EISZ7FY6AkSP8ObzenBcB"').first()
    # result7 = engine.execute('select speechiness from Track_data where speechiness >= 0.5').first()
    print("The liveness is", result4)
    print("The energy is", result3)
    print("The danceability is", result5)
    print("The speechiness is", result6)
# /////////////////////////////
    result8 = engine.execute('select track_id =="2EISZ7FY6AkSP8ObzenBcB"  from Track_data where danceability >= 0.4').first()
    result7 = engine.execute('select track_id =="2EISZ7FY6AkSP8ObzenBcB"  from Track_data where liveness >= 0.4').first()
    result9 = engine.execute('select track_id =="2EISZ7FY6AkSP8ObzenBcB"  from Track_data where energy >= 0.4').first()
    result10 = engine.execute('select track_id =="2EISZ7FY6AkSP8ObzenBcB"  from Track_data where speechiness >= 0.4').first()
    # print the result
    print(result8)
    print(result7)
    print(result9)
    print(result10)
# variables = ["result7", "result3", "result5", "result6"]
    for danceability in result8:
        if danceability==1:
            print("danceability is good")
        else:
            print("danceability is bad")
    for liveness in result7:
        if liveness == 1:
            print("liveness is good")
        else:
            print("liveness is bad")
    for energy in result9:
        if energy == 1:
            print("energy is good")
        else:
            print("energy is bad")
    for speechiness in result10:
        if speechiness == 1:
            print("speechiness is good")
        else:
            print("speechiness is bad")
sum = danceability + liveness + energy + speechiness
if sum==2:
    print("possibly")
elif sum>2:
    print("hit")
else:
    print("flop")



# print the result




comp = 0.5







app = Flask(__name__)

app.debug = True

@app.route('/', methods=["POST", "GET"])
def url(DECLARE=None):
    if request.method == "POST":
        run = request.form["url"]
        # sqllite database\
        engine = create_engine("sqlite+pysqlite:///:memory:")

        # Read data from CSV which will be
        # loaded as a dataframe object
        data = pandas.read_csv(r'C:/Users/user/PycharmProjects/HitSongPredictor/Kenya.csv')
        data1 = pandas.read_csv(r'C:/Users/user/PycharmProjects/HitSongPredictor/Naija.csv')

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
        # To test print the result
        # for row in result:
        #     print(row.track_id)
        # for row in result1:
        #     print(row.album)


        # /////////////////////////////////////

        # engine = create_engine('sqlite:////tmp/test.db')
        metadata = MetaData(bind=engine)
        users = Table('Track_data', metadata, autoload=True)
        con = engine.connect()
        # con.execute(users.insert(), name='admin', email='admin@localhost')

        with engine.connect() as conn:
            # let's select the column credit_history
            # from the data table
            #     result3 = engine.execute('select * from Track_data where artist =="Nyashinski"').first()
            result3 = engine.execute('select energy from Track_data where track_id =="2EISZ7FY6AkSP8ObzenBcB"').first()
            result4 = engine.execute('select liveness from Track_data where track_id =="2EISZ7FY6AkSP8ObzenBcB"').first()
            result5 = engine.execute('select danceability from Track_data where track_id =="2EISZ7FY6AkSP8ObzenBcB"').first()
            result6 = engine.execute('select speechiness from Track_data where track_id =="2EISZ7FY6AkSP8ObzenBcB"').first()
            # result7 = engine.execute('select speechiness from Track_data where speechiness >= 0.5').first()
            print("The liveness is", result4)
            print("The energy is", result3)
            print("The danceability is", result5)
            print("The speechiness is", result6)
        # /////////////////////////////

            result8 = engine.execute('select track_id ==run from Track_data where danceability >= 0.5').first()
            result7 = engine.execute('select track_id ==run  from Track_data where liveness >= 0.4').first()
            result9 = engine.execute('select track_id ==run  from Track_data where energy >= 0.4').first()
            result10 = engine.execute('select track_id ==run  from Track_data where speechiness >= 0.4').first()
            # result11 = engine.execute('SELECT @runs := run FROM Track_data WHERE track_id == runs  AND speechiness >0.4').first()


            # print the result
            print(result8)
            print(result7)
            print(result9)
            print(result10)
        # variables = ["result7", "result3", "result5", "result6"]
            for danceability in result8:
                if danceability==1:
                    print("danceability is good")
                else:
                    print("danceability is bad")
            for liveness in result7:
                if liveness == 1:
                    print("liveness is good")
                else:
                    print("liveness is bad")
            for energy in result9:
                if energy == 1:
                    print("energy is good")
                else:
                    print("energy is bad")
            for speechiness in result10:
                if speechiness == 1:
                    print("speechiness is good")
                else:
                    print("speechiness is bad")
        sum = danceability + liveness + energy + speechiness
        if sum==2:
            print("possibly")
            return redirect(url_for('possibly'))
        elif sum>2:
            print("hit")
            return redirect(url_for('hit'))
        else:
            print("flop")
            return redirect(url_for('flop'))


    return render_template("predictor.html")

@app.route('/table', methods=["POST", "GET"])
def table():


    return render_template("table.html")

@app.route('/feedback', methods=["POST", "GET"])
def feedback():


    return render_template("feedback.html")


if __name__ == '__main__':
    # app.config['SESSION_TYPE'] = 'memcached'
    # app.config['SECRET_KEY'] = 'super secret key'
    # sess = Session()
    app.debug = True
    app.run()