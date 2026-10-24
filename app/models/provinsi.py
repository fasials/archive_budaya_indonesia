from app.extensions import db


class Provinsi(db.Model):
    __tablename__ = "provinsi"

    id = db.Column(db.BigInteger, primary_key=True)
    nama_provinsi = db.Column(db.String(255), nullable=False)
    ibu_kota = db.Column(db.String(255), nullable=False)
    id_pulau = db.Column(db.BigInteger, db.ForeignKey("pulau.id"), nullable=False)

    pulau = db.relationship("Pulau", back_populates="provinsi")
    budaya = db.relationship("Budaya", back_populates="provinsi", passive_deletes=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nama_provinsi": self.nama_provinsi,
            "ibu_kota": self.ibu_kota,
            "id_pulau": self.id_pulau,
            "pulau": self.pulau.nama_pulau if self.pulau else None,
        }