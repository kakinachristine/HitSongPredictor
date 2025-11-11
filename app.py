import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, text, MetaData, Table

# Initialize Flask app
app = Flask(__name__)
app.debug = True

# Create in-memory SQLite engine
engine = create_engine("sqlite+pysqlite:///:memory:")

# Load CSV data into DataFrames
data_kenya = pd.read_csv(r'C:/Users/ChristineKakina/PycharmProjects/HitSongPredictor/Kenya.csv')
data_naija = pd.read_csv(r'C:/Users/ChristineKakina/PycharmProjects/HitSongPredictor/Naija.csv')

# Write data into SQLite tables
data_kenya.to_sql('Track_data', engine, index=False, if_exists='replace')
data_naija.to_sql('Track_data1', engine, index=False, if_exists='replace')


# Function to get track features
def get_track_features(track_id: str):
    with engine.connect() as conn:
        query = text("""
            SELECT energy, liveness, danceability, speechiness
            FROM Track_data
            WHERE track_id = :track_id
        """)
        result = conn.execute(query, {"track_id": track_id}).first()
        if result:
            return dict(zip(["energy", "liveness", "danceability", "speechiness"], result))
        else:
            return None


@app.route('/', methods=["POST", "GET"])
def predictor():
    if request.method == "POST":
        track_id = request.form.get("url")  # assuming track_id is passed in form

        features = get_track_features(track_id)
        if not features:
            return "Track not found", 404

        print(f"Features for {track_id}: {features}")

        # Score analysis
        score = sum([1 if v >= 0.4 else 0 for v in features.values()])
        print("Score:", score)

        if score == 2:
            return redirect(url_for('possibly'))
        elif score > 2:
            return redirect(url_for('hit'))
        else:
            return redirect(url_for('flop'))

    return render_template("predictor.html")


@app.route('/table', methods=["POST", "GET"])
def table():
    return render_template("table.html")


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    return render_template("feedback.html")


@app.route('/possibly')
def possibly():
    return "Possibly a hit!"


@app.route('/hit')
def hit():
    return "This is a hit!"


@app.route('/flop')
def flop():
    return "This is a flop!"


if __name__ == '__main__':
    app.run()
