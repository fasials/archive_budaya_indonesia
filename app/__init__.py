import os
from flask import Flask
from app.extensions import db


def create_app():
    app = Flask(__name__)

    # Konfigurasi Database dari .env
    database_url = os.getenv("DATABASE_URL")
    if database_url and database_url.startswith("postgresql://"):
        database_url = database_url.replace(
            "postgresql://", "postgresql+psycopg2://", 1
        )
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Hubungkan SQLAlchemy dengan app Flask
    db.init_app(app)

    # Daftarkan model (wajib di-import agar terbaca SQLAlchemy)
    from app import models  # noqa: F401

    # Daftarkan semua route (blueprint)
    from app.routes import register_routes
    register_routes(app)

    # Semua error (404, 405, 500, dll.) dibalas dalam format JSON
    from app.errors import register_error_handlers
    register_error_handlers(app)

    @app.route("/", methods=["GET"])
    def index():
        return {
            "status": "success",
            "message": "Selamat datang di API Peta Budaya Indonesia!"
        }, 200

    @app.route("/db-check", methods=["GET"])
    def check_db():
        try:
            db.session.execute(db.select(1))
            return {"status": "success", "database": "Terhubung ke Supabase!"}, 200
        except Exception:
            # Jangan kirim detail error ke client (bisa membocorkan info koneksi)
            app.logger.exception("Gagal terhubung ke database")
            return {"status": "error", "message": "Gagal terhubung ke database"}, 500

    return app