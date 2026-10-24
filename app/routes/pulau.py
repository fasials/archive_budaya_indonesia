from flask import Blueprint, jsonify
from sqlalchemy import select

from app.models import Pulau
from app.utils import error, get_by_id, paginate_query

bp = Blueprint("pulau", __name__, url_prefix="/pulau")


@bp.get("")
def list_pulau():
    return paginate_query(select(Pulau).order_by(Pulau.id), lambda p: p.to_dict())


@bp.get("/<int:pulau_id>")
def get_pulau(pulau_id):
    pulau = get_by_id(Pulau, pulau_id)
    if pulau is None:
        return error("Pulau tidak ditemukan", 404)
    data = pulau.to_dict()
    data["provinsi"] = [p.nama_provinsi for p in pulau.provinsi]
    return jsonify({"data": data}), 200