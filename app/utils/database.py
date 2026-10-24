from flask import current_app
from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db

MAX_ID = 2**63 - 1  # batas BIGINT PostgreSQL


def get_by_id(model, obj_id):
    """db.session.get yang aman dari id di luar jangkauan BIGINT."""
    if obj_id < 1 or obj_id > MAX_ID:
        return None
    return db.session.get(model, obj_id)


def safe_commit():
    """Commit; kalau gagal rollback dan kembalikan False."""
    try:
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        current_app.logger.exception("Gagal commit ke database")
        return False