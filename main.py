from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = ['1', '2', '3', '4', '5', '6', '7', '8']
    return render_template('homepage.html', movies=movies)


if __name__ == "__main__":
    app.run()