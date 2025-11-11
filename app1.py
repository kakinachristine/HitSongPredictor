import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine, text, MetaData, Table

# Initialize Flask app
app = Flask(__name__)
app.debug = True

# Create in-memory SQLite engine
engine = create_engine("sqlite:///songs.db", echo=True)

# Load CSV data once at startup
data_kenya = pd.read_csv(r'C:/Users/ChristineKakina/PycharmProjects/HitSongPredictor/Kenya.csv')
data_naija = pd.read_csv(r'C:/Users/ChristineKakina/PycharmProjects/HitSongPredictor/Naija.csv')

# Write data into SQLite tables
data_kenya.to_sql('Track_data', engine, index=False, if_exists='replace')
data_naija.to_sql('Track_data1', engine, index=False, if_exists='replace')


def get_track_features(track_id: str):
    """Fetch features of a track from the database"""
    with engine.connect() as conn:
        query = text("""
            SELECT danceability, liveness, energy, speechiness
            FROM Track_data
            WHERE track_id = :track_id
        """)
        result = conn.execute(query, {"track_id": track_id}).first()
        if result:
            return dict(zip(["danceability", "liveness", "energy", "speechiness"], result))
        return None


@app.route('/', methods=["POST", "GET"])
def predictor():
    if request.method == "POST":
        track_id = request.form.get("url")  # Get track_id from form
        features = get_track_features(track_id)

        if not features:
            return "Track not found", 404

        print(f"Features for {track_id}: {features}")

        # Convert features to binary scores
        score = 0
        score += 1 if features["danceability"] >= 0.5 else 0
        score += 1 if features["liveness"] >= 0.3 else 0
        score += 1 if features["energy"] >= 0.3 else 0
        score += 1 if features["speechiness"] >= 0.4 else 0

        print("Total score:", score)

        # Determine hit status
        if score == 2:
            return redirect(url_for('possibly'))
        elif score > 2:
            return redirect(url_for('hit'))
        else:
            return redirect(url_for('flop'))

    return render_template("predictor.html")


@app.route('/hit')
def hit():
    return render_template("hit.html")


@app.route('/possibly')
def possibly():
    return render_template("possibly.html")


@app.route('/flop')
def flop():
    return render_template("flop.html")


@app.route('/table', methods=["POST", "GET"])
def table():
    # Convert CSV to list of dicts
    csv_data = data_kenya.to_dict('records')
    return render_template("table.html", query=csv_data)


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    return render_template("feedback.html")


if __name__ == '__main__':
    app.run()
