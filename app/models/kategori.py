from sqlalchemy.dialects.postgresql import ENUM
from app.extensions import db

KATEGORI_ENUM = ENUM(
    "Tari", "Pakaian", "Kerajinan", "Pertunjukan", "Musik Tradisional",
    name="enum_kategori",
    create_type=False,
    inherit_schema=True,
)


class Kategori(db.Model):
    __tablename__ = "kategori"

    id = db.Column(db.BigInteger, primary_key=True)
    nama_kategori = db.Column(KATEGORI_ENUM, nullable=False, default="Pertunjukan")

    def to_dict(self):
        return {"id": self.id, "nama_kategori": self.nama_kategori}