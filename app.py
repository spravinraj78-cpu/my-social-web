import os
from flask import Flask, render_template

# Absolute path set panroam so Vercel templates-a correct-a edukkum
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('index.html') # Unga html file name dhaan index.html

if __name__ == '__main__':
    app.run(debug=True)
