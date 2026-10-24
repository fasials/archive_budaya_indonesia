from flask import Blueprint, jsonify
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.models import Provinsi
from app.utils import error, get_by_id, paginate_query, parse_int_arg

bp = Blueprint("provinsi", __name__, url_prefix="/provinsi")


@bp.get("")
def list_provinsi():
    query = select(Provinsi).options(joinedload(Provinsi.pulau)).order_by(Provinsi.id)

    id_pulau, err = parse_int_arg("id_pulau")
    if err:
        return error(err, 400)
    if id_pulau:
        query = query.where(Provinsi.id_pulau == id_pulau)

    return paginate_query(query, lambda p: p.to_dict())


@bp.get("/<int:provinsi_id>")
def get_provinsi(provinsi_id):
    provinsi = get_by_id(Provinsi, provinsi_id)
    if provinsi is None:
        return error("Provinsi tidak ditemukan", 404)
    data = provinsi.to_dict()
    data["budaya"] = [{"id": b.id, "nama_budaya": b.nama_budaya} for b in provinsi.budaya]
    return jsonify({"data": data}), 200