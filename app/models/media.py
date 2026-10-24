from app.extensions import db


class Media(db.Model):
    __tablename__ = "media"

    id = db.Column(db.BigInteger, primary_key=True)
    id_budaya = db.Column(db.BigInteger, db.ForeignKey("budaya.id"), nullable=False)
    url_media = db.Column(db.String(255), nullable=False)

    budaya = db.relationship("Budaya", back_populates="media")

    def to_dict(self):
        return {"id": self.id, "id_budaya": self.id_budaya, "url_media": self.url_media}