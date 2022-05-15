from flask import Flask, render_template

# creating our flask app
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("index.html")


# run our app in debug mode
if __name__ == "__main__":
    app.run(debug=True)