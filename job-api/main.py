from flask import Flask, request, jsonify
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
    return jsonify("pong")


# If title is recieved, filter by title. If any tags are given filter by tags.
# Title should be in the link itself
@app.route("/getJobs", methods=["GET"])
def getJobs():

    title = request.args.get("title")

    if title:
        jobs = JobPosition.query.filter_by(title=title).all()
    else:
        jobs = JobPosition.query.all()

    positions = [
        {
            "id": j.id,
            "title": j.title,
            "description": j.description,
            "city": j.city,
            "tags": j.tags,
        }
        for j in jobs
    ]

    return jsonify(positions)




@app.route("/addJobListing", methods=["POST"])
def addJobListing():
    pass


if __name__ == "__main__":
    create_db()
    app.run(port=5001, debug=True)
