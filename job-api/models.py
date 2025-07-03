from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class JobPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    city = db.Column(db.String)
    tags = db.Column(db.String) # Yes all tags are stored inside one String seperated by columns.

    def __init__(self):
        pass


    def get_tags_list(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(",")]
        return []

    def set_tags_list(self, tags_list):
        self.tags = ",".join(tags_list)


    def addToDB(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        """Return all job positions."""
        return JobPosition.query.all()
    
# So appearently sqlalchemy auto closes db. so db.close() not necessary.