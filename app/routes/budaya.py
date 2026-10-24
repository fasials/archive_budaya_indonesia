from flask import Blueprint, jsonify, request
from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from app.extensions import db
from app.models import Budaya, Kategori, Provinsi
from app.models.kategori import KATEGORI_ENUM
from app.utils import (MAX_ID, error, get_by_id, get_json_body, paginate_query,
                       parse_int_arg, safe_commit)

bp = Blueprint("budaya", __name__, url_prefix="/budaya")

REQUIRED_FIELDS = ("nama_budaya", "deskripsi_budaya", "id_provinsi")


def _eager_options():
    """Muat relasi sekaligus agar tidak query berulang (N+1)."""
    return (
        joinedload(Budaya.provinsi).joinedload(Provinsi.pulau),
        selectinload(Budaya.kategori),
        selectinload(Budaya.media),
    )


def _is_int(value):
    return isinstance(value, int) and not isinstance(value, bool)


def _clean(data, partial=False):
    """Validasi body. Return (data_bersih, pesan_error)."""
    clean = {}

    if not partial:  # POST & PUT: field wajib harus lengkap
        for field in REQUIRED_FIELDS:
            if field not in data or data[field] in (None, ""):
                return None, f"Field {field} wajib diisi"

    for field in ("nama_budaya", "deskripsi_budaya"):
        if field in data:
            value = data[field]
            if not isinstance(value, str) or not value.strip():
                return None, f"Field {field} harus berupa teks dan tidak boleh kosong"
            value = value.strip()
            if field == "nama_budaya" and len(value) > 255:
                return None, "Field nama_budaya maksimal 255 karakter"
            clean[field] = value

    if "id_provinsi" in data:
        value = data["id_provinsi"]
        if not _is_int(value):
            return None, "Field id_provinsi harus berupa angka bulat"
        if get_by_id(Provinsi, value) is None:
            return None, f"Provinsi dengan id {value} tidak ditemukan"
        clean["id_provinsi"] = value

    if "id_kategori" in data:  # opsional: isi tabel pivot kategoribudaya
        ids = data["id_kategori"]
        if not isinstance(ids, list) or not all(_is_int(i) for i in ids):
            return None, "Field id_kategori harus berupa list angka, contoh [1, 4]"
        valid_ids = [i for i in ids if 0 < i <= MAX_ID]
        found = db.session.scalars(
            select(Kategori).where(Kategori.id.in_(valid_ids))
        ).all()
        missing = sorted(set(ids) - {k.id for k in found})
        if missing:
            return None, f"Kategori dengan id {missing} tidak ditemukan"
        clean["kategori"] = found

    return clean, None


# ---------- READ ----------
@bp.get("")
def list_budaya():
    query = select(Budaya).options(*_eager_options()).order_by(Budaya.id)

    q = request.args.get("q", "").strip()
    if q:
        query = query.where(Budaya.nama_budaya.ilike(f"%{q}%"))

    id_provinsi, err = parse_int_arg("id_provinsi")
    if err:
        return error(err, 400)
    if id_provinsi:
        query = query.where(Budaya.id_provinsi == id_provinsi)

    kategori = request.args.get("kategori", "").strip()
    if kategori:
        if kategori not in KATEGORI_ENUM.enums:
            return error(
                "Kategori tidak valid. Pilihan: " + ", ".join(KATEGORI_ENUM.enums), 400
            )
        query = query.where(Budaya.kategori.any(Kategori.nama_kategori == kategori))

    return paginate_query(query, lambda b: b.to_dict())


@bp.get("/<int:budaya_id>")
def get_budaya(budaya_id):
    budaya = None
    if 0 < budaya_id <= MAX_ID:
        budaya = db.session.scalars(
            select(Budaya).options(*_eager_options()).where(Budaya.id == budaya_id)
        ).first()
    if budaya is None:
        return error("Budaya tidak ditemukan", 404)
    return jsonify({"data": budaya.to_dict()}), 200


# ---------- CREATE ----------
@bp.post("")
def create_budaya():
    data = get_json_body()
    if data is None:
        return error("Body request harus berupa JSON object", 400)

    clean, err = _clean(data)
    if err:
        return error(err, 400)

    budaya = Budaya(**clean)
    db.session.add(budaya)
    if not safe_commit():
        return error("Terjadi kesalahan pada server", 500)
    return jsonify({"message": "Budaya berhasil ditambahkan",
                    "data": budaya.to_dict()}), 201


# ---------- UPDATE (PUT = seluruh data, PATCH = sebagian) ----------
def _update(budaya_id, partial):
    budaya = get_by_id(Budaya, budaya_id)
    if budaya is None:
        return error("Budaya tidak ditemukan", 404)

    data = get_json_body()
    if data is None:
        return error("Body request harus berupa JSON object", 400)

    clean, err = _clean(data, partial=partial)
    if err:
        return error(err, 400)
    if not clean:
        return error("Tidak ada field yang diubah", 400)

    for key, value in clean.items():
        setattr(budaya, key, value)
    if not safe_commit():
        return error("Terjadi kesalahan pada server", 500)
    return jsonify({"message": "Budaya berhasil diperbarui",
                    "data": budaya.to_dict()}), 200


@bp.put("/<int:budaya_id>")
def put_budaya(budaya_id):
    return _update(budaya_id, partial=False)


@bp.patch("/<int:budaya_id>")
def patch_budaya(budaya_id):
    return _update(budaya_id, partial=True)


# ---------- DELETE ----------
@bp.delete("/<int:budaya_id>")
def delete_budaya(budaya_id):
    budaya = get_by_id(Budaya, budaya_id)
    if budaya is None:
        return error("Budaya tidak ditemukan", 404)

    db.session.delete(budaya)
    if not safe_commit():
        return error("Terjadi kesalahan pada server", 500)
    return jsonify({"message": "Budaya berhasil dihapus"}), 200