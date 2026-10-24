from flask import jsonify

from app.extensions import db
from app.utils.params import parse_int_arg
from app.utils.responses import error


def paginate_query(query, serialize):
    """Jalankan query dengan pagination (?page=1&per_page=10, maks 100)."""
    page, err1 = parse_int_arg("page")
    per_page, err2 = parse_int_arg("per_page")
    if err1 or err2:
        return error("Parameter page dan per_page harus berupa angka bulat positif", 400)
    page = page or 1
    per_page = min(per_page or 10, 100)

    result = db.paginate(query, page=page, per_page=per_page, error_out=False)
    return jsonify({
        "data": [serialize(item) for item in result.items],
        "meta": {
            "page": result.page,
            "per_page": result.per_page,
            "total": result.total,
            "total_pages": result.pages,
        },
    }), 200