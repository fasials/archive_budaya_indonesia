from app.extensions import db


class Pulau(db.Model):
    __tablename__ = "pulau"

    id = db.Column(db.BigInteger, primary_key=True)
    nama_pulau = db.Column(db.String(255), nullable=False)

    provinsi = db.relationship("Provinsi", back_populates="pulau", passive_deletes=True)

    def to_dict(self):
        return {"id": self.id, "nama_pulau": self.nama_pulau}