from flask import Blueprint, jsonify
from sqlalchemy import select

from app.extensions import db
from app.models import Budaya, Kategori
from app.utils import error, get_by_id, paginate_query

bp = Blueprint("kategori", __name__, url_prefix="/kategori")


@bp.get("")
def list_kategori():
    return paginate_query(select(Kategori).order_by(Kategori.id), lambda k: k.to_dict())


@bp.get("/<int:kategori_id>")
def get_kategori(kategori_id):
    kategori = get_by_id(Kategori, kategori_id)
    if kategori is None:
        return error("Kategori tidak ditemukan", 404)
    data = kategori.to_dict()
    budaya = db.session.scalars(
        select(Budaya).where(Budaya.kategori.any(Kategori.id == kategori.id)).order_by(Budaya.id)
    ).all()
    data["budaya"] = [{"id": b.id, "nama_budaya": b.nama_budaya} for b in budaya]
    return jsonify({"data": data}), 200