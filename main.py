from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("board-dynamic.html")

if __name__ == "__main__":
    app.run(debug=True)
# To run this application, ensure you have Flask installed and a 'templates' folder with 'board.html' inside it.