from app.extensions import db


class KategoriBudaya(db.Model):
    """Tabel pivot many-to-many antara budaya dan kategori."""
    __tablename__ = "kategoribudaya"

    id = db.Column(db.BigInteger, primary_key=True)
    id_budaya = db.Column(db.BigInteger, db.ForeignKey("budaya.id"), nullable=False)
    id_kategori = db.Column(db.BigInteger, db.ForeignKey("kategori.id"), nullable=False)