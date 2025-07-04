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

    job_id = request.args.get("id")
    title = request.args.get("title")
    city = request.args.get("city")
    
    query = JobPosition.query

    if job_id:
        job = query.filter_by(id=job_id).first()
        return jsonify({
            "id": job.id,
            "title": job.title,
            "description": job.description,
            "city": job.city,
            "tags": job.tags
        })

    if title:
        query = query.filter_by(title=title)

    if city:
        query = query.filter_by(city=city)

    positions = [
        {
            "id": j.id,
            "title": j.title,
            "description": j.description,
            "city": j.city,
            "tags": j.tags,
        }
        for j in query
    ]

    return jsonify(positions)

@app.route("/addJobListing", methods=["POST"])
def addJobListing():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_job = JobPosition(
        title=data.get("title"),
        description=data.get("description"),
        city=data.get("city"),
        tags=data.get("tags")
    )

    new_job.addToDB()

    return jsonify({"message": "Job added successfully to db!", "job_id": new_job.id}), 201


@app.route('/deleteJob/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = JobPosition.query.filter_by(id=job_id).first()

    if job:
        db.session.delete(job)
        db.session.commit()
        return jsonify({"message": f"Sucessfully removed job with id: {job.id}"}), 200
    
    return jsonify({"error": "job wasn't found"}), 404

if __name__ == "__main__":
    create_db()
    app.run(port=5001, debug=True)
