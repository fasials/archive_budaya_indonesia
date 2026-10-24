from flask import request

from app.utils.database import MAX_ID


def get_json_body():
    """Ambil body JSON. Kembalikan None kalau bukan JSON object yang valid."""
    data = request.get_json(silent=True)
    return data if isinstance(data, dict) else None


def parse_int_arg(name):
    """Baca query param integer opsional. Return (nilai, pesan_error)."""
    raw = request.args.get(name)
    if raw is None or raw == "":
        return None, None
    try:
        value = int(raw)
    except ValueError:
        return None, f"Parameter {name} harus berupa angka bulat"
    if value < 1 or value > MAX_ID:
        return None, f"Parameter {name} tidak valid"
    return value, None