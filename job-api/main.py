from flask import Flask
from models import db, JobPosition


app = Flask(__name__)


def create_db():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize db with app
    db.init_app(app)

    with app.app_context():
        db.create_all()


@app.route("/ping")
def hello():
    return "pong"


# /getJobs
@app.route("/getJobs", methods=["GET", "POST"])
def getJobs():
    pass


@app.route("/addJobListing", methods=["POST"])
def addJobListing():
    pass


if __name__ == "__main__":
    create_db()
    app.run(debug=True)
