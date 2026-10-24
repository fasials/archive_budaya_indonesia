from flask import Blueprint, jsonify
from sqlalchemy import select

from app.models import Media
from app.utils import error, get_by_id, paginate_query, parse_int_arg

bp = Blueprint("media", __name__, url_prefix="/media")


@bp.get("")
def list_media():
    query = select(Media).order_by(Media.id)

    id_budaya, err = parse_int_arg("id_budaya")
    if err:
        return error(err, 400)
    if id_budaya:
        query = query.where(Media.id_budaya == id_budaya)

    return paginate_query(query, lambda m: m.to_dict())


@bp.get("/<int:media_id>")
def get_media(media_id):
    media = get_by_id(Media, media_id)
    if media is None:
        return error("Media tidak ditemukan", 404)
    return jsonify({"data": media.to_dict()}), 200
