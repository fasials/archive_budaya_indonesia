from flask import current_app, jsonify
from werkzeug.exceptions import HTTPException

from app.extensions import db

# Pesan error berbahasa Indonesia untuk status code yang umum
PESAN = {
    400: "Permintaan tidak valid",
    404: "Endpoint tidak ditemukan",
    405: "Method tidak diizinkan untuk endpoint ini",
    415: "Content-Type harus application/json",
    500: "Terjadi kesalahan pada server",
}


def register_error_handlers(app):
    """Semua error dikembalikan sebagai JSON: {"error": "..."}"""

    @app.errorhandler(HTTPException)
    def handle_http_error(e):
        response = jsonify({"error": PESAN.get(e.code, e.description)})
        response.status_code = e.code
        # 405: beri tahu method apa yang diperbolehkan lewat header Allow
        if e.code == 405 and getattr(e, "valid_methods", None):
            response.headers["Allow"] = ", ".join(e.valid_methods)
        return response

    @app.errorhandler(Exception)
    def handle_unexpected_error(e):
        # Detail error hanya masuk log server, TIDAK dikirim ke client
        current_app.logger.exception("Error tak terduga: %s", e)
        db.session.rollback()
        return jsonify({"error": PESAN[500]}), 500