from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile_data = {
        "name": "Pravin Raj",
        "bio": "Content Creator | Tech Enthusiast",
        "insta_url": "https://instagram.com/pravin_official14",
        "yt_url": "https://youtube.com/@UNGA_YOUTUBE_CHANNEL"
    }
    return render_template('index.html', data=profile_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)