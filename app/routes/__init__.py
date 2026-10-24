from app.routes import budaya, kategori, media, provinsi, pulau


def register_routes(app):
    """Daftarkan semua blueprint ke aplikasi Flask."""
    for module in (budaya, pulau, provinsi, kategori, media):
        app.register_blueprint(module.bp)