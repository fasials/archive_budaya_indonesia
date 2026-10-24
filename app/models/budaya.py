from app.extensions import db
from app.models.kategori_budaya import KategoriBudaya


class Budaya(db.Model):
    __tablename__ = "budaya"

    id = db.Column(db.BigInteger, primary_key=True)
    id_provinsi = db.Column(db.BigInteger, db.ForeignKey("provinsi.id"), nullable=False)
    nama_budaya = db.Column(db.String(255), nullable=False)
    deskripsi_budaya = db.Column(db.Text, nullable=False)

    provinsi = db.relationship("Provinsi", back_populates="budaya")
    media = db.relationship("Media", back_populates="budaya", passive_deletes=True)
    kategori = db.relationship("Kategori", secondary=KategoriBudaya.__table__)

    def to_dict(self, detail=True):
        data = {
            "id": self.id,
            "nama_budaya": self.nama_budaya,
            "deskripsi_budaya": self.deskripsi_budaya,
            "id_provinsi": self.id_provinsi,
        }
        if detail:
            data["provinsi"] = self.provinsi.nama_provinsi if self.provinsi else None
            data["pulau"] = self.provinsi.pulau.nama_pulau if self.provinsi else None
            data["kategori"] = [k.nama_kategori for k in self.kategori]
            data["media"] = [m.url_media for m in self.media]
        return data