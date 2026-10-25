# API Peta Budaya Indonesia

REST API untuk menyimpan dan menelusuri kekayaan budaya Indonesia berdasarkan asal daerah dengan kategori dan deskripsi budaya tersebut.

| Properti | Nilai |
|---|---|
| Deployment (Vercel) | https://archivebudayaindonesia.vercel.app |
| Format payload | JSON |
| Content-Type request | `application/json` |
| Format respons | JSON dengan properti `status`, dan lain sebagainya seperti `message`, `data`, `meta`, atau `errors` |

## Skema Database dan ERD

![ERD Peta Budaya Indonesia](drawSQL-image-export-2026-10-25.webp)

### Relasi antar tabel

| Relasi | Jenis | Keterangan |
|---|---|---|
| `pulau` → `provinsi` | one-to-many | Satu pulau memiliki banyak provinsi |
| `provinsi` → `budaya` | one-to-many | Satu provinsi memiliki banyak budaya |
| `budaya` → `media` | one-to-many | Satu budaya memiliki banyak media |
| `budaya` ↔ `kategori` | **many-to-many** | Lewat tabel pivot `kategoribudaya`. Satu budaya bisa punya beberapa kategori, dan satu kategori dipakai banyak budaya |

## Daftar Endpoint

### 1. Daftar Budaya
```
- Method       : GET
- URL          : https://archivebudayaindonesia.vercel.app/budaya
- Deskripsi    : Mengambil daftar budaya (dengan pagination dan filter)
- Headers      : -
- Request Body : -
- Response Sukses (200):
  {
    "data": [
      {
  "data": [
    {
      "deskripsi_budaya": "Tarian tradisional yang berkembang di lingkungan budaya Jawa.",
      "id": 1,
      "id_provinsi": 1,
      "kategori": [
        "Pertunjukan",
        "Tari"
      ],
      "media": [
        "https://commons.wikimedia.org/wiki/File:Gambyong_Langenkusuma_Pj_DSC_1322.JPG#/media/Berkas:Gambyong_Langenkusuma_Pj_DSC_1322.JPG",
        "https://www.youtube.com/watch?v=BqWw4HPHq1o"
      ],
      "nama_budaya": "Tari Gambyong",
      "provinsi": "Jawa Tengah",
      "pulau": "Jawa"
    },
    {
      "deskripsi_budaya": "Seni pertunjukan wayang dengan tokoh yang dimainkan di balik layar.",
      "id": 2,
      "id_provinsi": 1,
      "kategori": [
        "Pertunjukan",
        "Kerajinan"
      ],
      "media": [
        "https://commons.wikimedia.org/wiki/File:Wayang_Performance.jpg#/media/Berkas:Wayang_Performance.jpg"
      ],
      "nama_budaya": "Wayang Kulit",
      "provinsi": "Jawa Tengah",
      "pulau": "Jawa"
    },
    {
      "deskripsi_budaya": "Alat musik tradisional yang dimainkan dengan cara digoyangkan.",
      "id": 3,
      "id_provinsi": 2,
      "kategori": [
        "Kerajinan",
        "Musik Tradisional"
      ],
      "media": [
        "https://commons.wikimedia.org/wiki/File:Angklung_(2315119130).jpg#/media/Berkas:Angklung_(2315119130).jpg"
      ],
      "nama_budaya": "Angklung",
      "provinsi": "Jawa Barat",
      "pulau": "Jawa"
    },
    {
      "deskripsi_budaya": "Busana tradisional yang dikenakan dalam berbagai acara adat.",
      "id": 4,
      "id_provinsi": 2,
      "kategori": [
        "Pakaian",
        "Kerajinan"
      ],
      "media": [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbSh9hWnQMhHDmVTj9st9V40vu7t96wFYI4Lna_BNN1ztfqZwrCaXTljk&s=10"
      ],
      "nama_budaya": "Kebaya Sunda",
      "provinsi": "Jawa Barat",
      "pulau": "Jawa"
    },
    {
      "deskripsi_budaya": "Seni pertunjukan tradisional yang terkenal dengan dadak merak.",
      "id": 5,
      "id_provinsi": 3,
      "kategori": [
        "Pertunjukan",
        "Tari"
      ],
      "media": [
        "https://commons.wikimedia.org/wiki/File:Reog_ponorogo_dalam_event_eksotika_bromo.jpg#/media/Berkas:Reog_ponorogo_dalam_event_eksotika_bromo.jpg"
      ],
      "nama_budaya": "Reog Ponorogo",
      "provinsi": "Jawa Timur",
      "pulau": "Jawa"
    },
    {
      "deskripsi_budaya": "Pertunjukan tari yang menggunakan paduan suara penari sebagai pengiring.",
      "id": 6,
      "id_provinsi": 4,
      "kategori": [
        "Pertunjukan",
        "Tari"
      ],
      "media": [
        "https://asset.kompas.com/crops/gdNDwiSsNMPkNbgaB2v5m8Q6l1k=/2x0:1000x665/1200x800/data/photo/2023/02/23/63f753ada95a3.jpg"
      ],
      "nama_budaya": "Tari Kecak",
      "provinsi": "Bali",
      "pulau": "Bali"
    },
    {
      "deskripsi_budaya": "Tarian tradisional yang menggunakan piring sebagai properti tari.",
      "id": 7,
      "id_provinsi": 5,
      "kategori": [
        "Pertunjukan",
        "Tari"
      ],
      "media": [
        "https://commons.wikimedia.org/wiki/File:Tari_Piring_dan_Pecahan_Kaca.jpg#/media/Berkas:Tari_Piring_dan_Pecahan_Kaca.jpg"
      ],
      "nama_budaya": "Tari Piring",
      "provinsi": "Sumatera Barat",
      "pulau": "Sumatera"
    },
    {
      "deskripsi_budaya": "Kain tradisional dengan hiasan benang emas atau perak.",
      "id": 8,
      "id_provinsi": 5,
      "kategori": [
        "Pakaian",
        "Kerajinan"
      ],
      "media": [
        "https://commons.wikimedia.org/wiki/File:Tenunan_songket_khas_Minangkabau.jpg#/media/Berkas:Tenunan_songket_khas_Minangkabau.jpg"
      ],
      "nama_budaya": "Songket Minangkabau",
      "provinsi": "Sumatera Barat",
      "pulau": "Sumatera"
    },
    {
      "deskripsi_budaya": "Motif batik klasik.",
      "id": 10,
      "id_provinsi": 1,
      "kategori": [
        "Pakaian",
        "Kerajinan"
      ],
      "media": [],
      "nama_budaya": "Batik Parang",
      "provinsi": "Jawa Tengah",
      "pulau": "Jawa"
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 10,
    "total": 9,
    "total_pages": 1
  }
}
Response Error (400):
  {
    "error": "Kategori tidak valid. Pilihan: Tari, Pakaian, Kerajinan, Pertunjukan, Musik Tradisional"
  }
```

### 2. Detail Budaya
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/budaya/1
Deskripsi    : Mengambil satu budaya beserta provinsi, pulau, kategori, dan media
Headers      : -
Request Body : -
Response Sukses (200):
  {
  "data": {
    "deskripsi_budaya": "Tarian tradisional yang berkembang di lingkungan budaya Jawa.",
    "id": 1,
    "id_provinsi": 1,
    "kategori": [
      "Pertunjukan",
      "Tari"
    ],
    "media": [
      "https://commons.wikimedia.org/wiki/File:Gambyong_Langenkusuma_Pj_DSC_1322.JPG#/media/Berkas:Gambyong_Langenkusuma_Pj_DSC_1322.JPG",
      "https://www.youtube.com/watch?v=BqWw4HPHq1o"
    ],
    "nama_budaya": "Tari Gambyong",
    "provinsi": "Jawa Tengah",
    "pulau": "Jawa"
  }
}
Response Error (404):
  {
    "error": "Budaya tidak ditemukan"
  }
```

### 3. Tambah Budaya
```
Method       : POST
URL          : https://archivebudayaindonesia.vercel.app/budaya
Deskripsi    : Menambahkan budaya baru
Headers      : Content-Type: application/json
Request Body :
  {
    "nama_budaya": "Batik Parang",
    "deskripsi_budaya": "Motif batik klasik dari Jawa.",
    "id_provinsi": 1,
    "id_kategori": [
      2,
      3
    ]
  }
Response Sukses (201):
  {
    "data": {
      "deskripsi_budaya": "Motif batik klasik dari Jawa.",
      "id": 11,
      "id_provinsi": 1,
      "kategori": [
        "Pakaian",
        "Kerajinan"
      ],
      "media": [],
      "nama_budaya": "Batik Parang",
      "provinsi": "Jawa Tengah",
      "pulau": "Jawa"
    },
    "message": "Budaya berhasil ditambahkan"
  }
Response Error (400):
  {
    "error": "Field nama_budaya wajib diisi"
  }
```

### 4. Ubah Seluruh Data Budaya (PUT)
```
Method       : PUT
URL          : https://archivebudayaindonesia.vercel.app/budaya/9
Deskripsi    : Mengubah seluruh data budaya. Field wajib harus lengkap
Headers      : Content-Type: application/json
Request Body :
  {
    "nama_budaya": "Batik Kawung",
    "deskripsi_budaya": "Motif kawung dari Jawa Tengah.",
    "id_provinsi": 1
    "id_kategori": [
      1,
      4
  }
Response Sukses (200):
  {
  "data": {
    "deskripsi_budaya": "Motif batik klasik dari",
    "id": 11,
    "id_provinsi": 2,
    "kategori": [
      "Pertunjukan",
      "Tari"
    ],
    "media": [],
    "nama_budaya": "Batik S",
    "provinsi": "Jawa Barat",
    "pulau": "Jawa"
  },
  "message": "Budaya berhasil diperbarui"
}
Response Error (400):
  {
    "error": "Field deskripsi_budaya wajib diisi"
  }
```

### 5. Ubah Sebagian Data Budaya (PATCH)
```
Method       : PATCH
URL          : https://archivebudayaindonesia.vercel.app/budaya/9
Deskripsi    : Mengubah sebagian field budaya
Headers      : Content-Type: application/json
Request Body :
  {
    "deskripsi_budaya": "Deskripsi diperbarui lewat PATCH.",
    "id_kategori": [
      3
    ]
  }
Response Sukses (200):
 {
  "data": {
    "deskripsi_budaya": "Deskripsi diperbarui lewat PATCH.",
    "id": 11,
    "id_provinsi": 2,
    "kategori": [
      "Kerajinan"
    ],
    "media": [],
    "nama_budaya": "Batik S",
    "provinsi": "Jawa Barat",
    "pulau": "Jawa"
  },
  "message": "Budaya berhasil diperbarui"
}
Response Error (400):
  {
    "error": "Tidak ada field yang diubah"
  }
```

### 6. Hapus Budaya
```
Method       : DELETE
URL          : https://archivebudayaindonesia.vercel.app/budaya/9
Deskripsi    : Menghapus budaya
Headers      : -
Request Body : -
Response Sukses (200):
  {
    "message": "Budaya berhasil dihapus"
  }
Response Error (404):
  {
    "error": "Budaya tidak ditemukan"
  }
```

### 7. Daftar Pulau
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/pulau
Deskripsi    : Mengambil daftar pulau
Headers      : -
Request Body : -
Response Sukses (200):
  {
    "data": [
      {
        "id": 1,
        "nama_pulau": "Jawa"
      },
      {
        "id": 2,
        "nama_pulau": "Bali"
      },
      {
        "id": 3,
        "nama_pulau": "Sumatera"
      }
    ],
    "meta": {
      "page": 1,
      "per_page": 10,
      "total": 3,
      "total_pages": 1
    }
  }
Response Error (400):
  {
    "error": "Parameter page dan per_page harus berupa angka bulat positif"
  }
```

### 8. Detail Pulau
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/pulau/1
Deskripsi    : Mengambil satu pulau beserta daftar provinsinya
Headers      : -
Request Body : -
Response Sukses (200):
  {
    "data": {
      "id": 1,
      "nama_pulau": "Jawa",
      "provinsi": [
        "Jawa Tengah",
        "Jawa Barat",
        "Jawa Timur"
      ]
    }
  }
Response Error (404):
  {
    "error": "Pulau tidak ditemukan"
  }
```

### 9. Daftar Provinsi
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/provinsi
Deskripsi    : Mengambil daftar provinsi
Headers      : -
Request Body : -
Response Sukses (200):
  {
    "data": [
      {
        "ibu_kota": "Semarang",
        "id": 1,
        "id_pulau": 1,
        "nama_provinsi": "Jawa Tengah",
        "pulau": "Jawa"
      },
      {
        "ibu_kota": "Bandung",
        "id": 2,
        "id_pulau": 1,
        "nama_provinsi": "Jawa Barat",
        "pulau": "Jawa"
      },
      {
        "ibu_kota": "Surabaya",
        "id": 3,
        "id_pulau": 1,
        "nama_provinsi": "Jawa Timur",
        "pulau": "Jawa"
      }
    ],
    "meta": {
      "page": 1,
      "per_page": 10,
      "total": 3,
      "total_pages": 1
    }
  }
Response Error (400):
  {
    "error": "Parameter id_pulau harus berupa angka bulat"
  }
```

### 10. Detail Provinsi
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/provinsi/5
Deskripsi    : Mengambil satu provinsi beserta daftar budayanya
Headers      : -
Request Body : -
Response Sukses (200):
  {
    "data": {
      "budaya": [
        {
          "id": 7,
          "nama_budaya": "Tari Piring"
        },
        {
          "id": 8,
          "nama_budaya": "Songket Minangkabau"
        }
      ],
      "ibu_kota": "Padang",
      "id": 5,
      "id_pulau": 3,
      "nama_provinsi": "Sumatera Barat",
      "pulau": "Sumatera"
    }
  }
Response Error (404):
  {
    "error": "Provinsi tidak ditemukan"
  }
```

### 11. Daftar Kategori
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/kategori
Deskripsi    : Mengambil daftar kategori
Headers      : -
Request Body : -
Response Sukses (200):
  {
  "data": [
    {
      "id": 1,
      "nama_kategori": "Pertunjukan"
    },
    {
      "id": 2,
      "nama_kategori": "Pakaian"
    },
    {
      "id": 3,
      "nama_kategori": "Kerajinan"
    },
    {
      "id": 4,
      "nama_kategori": "Tari"
    },
    {
      "id": 5,
      "nama_kategori": "Musik Tradisional"
    }
  ],
  "meta": {
    "page": 1,
    "per_page": 10,
    "total": 5,
    "total_pages": 1
  }
}
Response Error (400):
  {
    "error": "Parameter page dan per_page harus berupa angka bulat positif"
  }
```

### 12. Detail Kategori
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/kategori/4
Deskripsi    : Mengambil satu kategori beserta daftar budayanya
Headers      : -
Request Body : -
Response Sukses (200):
  {
    "data": {
      "budaya": [
        {
          "id": 1,
          "nama_budaya": "Tari Gambyong"
        },
        {
          "id": 5,
          "nama_budaya": "Reog Ponorogo"
        },
        {
          "id": 6,
          "nama_budaya": "Tari Kecak"
        },
        {
          "id": 7,
          "nama_budaya": "Tari Piring"
        }
      ],
      "id": 4,
      "nama_kategori": "Tari"
    }
  }
Response Error (404):
  {
    "error": "Kategori tidak ditemukan"
  }
```

### 13. Daftar Media
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/media
Deskripsi    : Mengambil daftar media 
Headers      : -
Request Body : -
Response Sukses (200):
  {
    "data": [
      {
        "id": 1,
        "id_budaya": 1,
        "url_media": "https://example.com/tari-gambyong.jpg"
      },
      {
        "id": 2,
        "id_budaya": 1,
        "url_media": "https://example.com/tari-gambyong-2.jpg"
      }
    ],
    "meta": {
      "page": 1,
      "per_page": 10,
      "total": 2,
      "total_pages": 1
    }
  }
Response Error (400):
  {
    "error": "Parameter id_budaya harus berupa angka bulat"
  }
```

### 14. Detail Media
```
Method       : GET
URL          : https://archivebudayaindonesia.vercel.app/media/1
Deskripsi    : Mengambil satu media
Headers      : -
Request Body : -
Response Sukses (200):
  {
    "data": {
      "id": 1,
      "id_budaya": 1,
      "url_media": "https://example.com/tari-gambyong.jpg"
    }
  }
Response Error (404):
  {
    "error": "Media tidak ditemukan"
  }
```

---
## Format Error

Semua error dikembalikan dalam JSON dengan format `{"error": "pesan"}`.

| Status | Arti | Contoh pesan |
|---|---|---|
| `400` | Input tidak valid | `Field nama_budaya wajib diisi` |
| `404` | Data atau endpoint tidak ditemukan | `Budaya tidak ditemukan` |
| `405` | Method tidak diizinkan | `Method tidak diizinkan untuk endpoint ini` |
| `500` | Error server | `Terjadi kesalahan pada server` |

Detail teknis error server tidak dikirim ke client, hanya dicatat di log.

---
## Cara Menjalankan Secara Lokal

**Prasyarat:** Python 3.12 atau lebih baru, dan database PostgreSQL (Supabase atau PostgreSQL lokal).

**1. Clone repository**
```bash
git clone https://github.com/<username>/<nama-repo>.git
cd <nama-repo>
```

**2. Buat virtual environment dan install dependensi**
```bash
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

**3. Siapkan database**

Jalankan dua file SQL berikut **secara berurutan** di database kamu (Supabase: *SQL Editor → New query*):

1. `database/01_struktur.sql`
2. `database/02_data_dummy.sql`

> `01_struktur.sql` diawali `DROP SCHEMA IF EXISTS peta_budaya_indonesia CASCADE`, jadi schema lama akan dihapus dan dibuat ulang.

**4. Atur environment variables**

Salin `.env.example` menjadi `.env`, lalu isi nilainya:

```env
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/postgres
DB_SCHEMA=peta_budaya_indonesia
```

File `.env` sudah masuk `.gitignore` dan **tidak boleh** di-commit.

**5. Jalankan aplikasi**
```bash
python run.py
```

Aplikasi berjalan di `http://localhost:5000`. Cek koneksi database di `http://localhost:5000/db-check`, dan coba `http://localhost:5000/budaya`.

---

## 6. Deployment ke Vercel

Aplikasi di-deploy lewat integrasi GitHub di Vercel. Berkas yang dipakai:

| File | Fungsi |
|---|---|
| `index.py` | Entrypoint yang diekspos sebagai variabel `app` |
| `requirements.txt` | Daftar dependensi |
| `.python-version` | Versi Python di Vercel (3.13) |
| `vercel.json` | Konfigurasi function (mengecualikan file yang tidak perlu) |

**Environment Variables** (diatur di *Project Settings → Environment Variables*, bukan di kode):

| Name | Keterangan |
|---|---|
| `DATABASE_URL` | Connection string **Transaction pooler** Supabase (port 6543). Vercel tidak mendukung koneksi langsung (IPv6) |
| `DB_SCHEMA` | `peta_budaya_indonesia` |

Saat berjalan di Vercel, aplikasi memakai `NullPool` karena pooling koneksi ditangani oleh Supabase.

---

## 7. Pengujian

Seluruh endpoint diuji memakai **Thunder Client** dengan URL Vercel (bukan `localhost`).

- Screenshot bukti pengujian: folder [`dokumentasi`](pengujian/)

Collection berisi 14 endpoint.

---

## 8. Struktur Project

```
.
├── app/
│   ├── __init__.py          # create_app(): konfigurasi dan pendaftaran route
│   ├── errors.py            # penanganan error global (JSON)
│   ├── extensions.py        # instance SQLAlchemy dan schema
│   ├── models/              # satu file per tabel
│   ├── routes/              # blueprint per resource
│   └── utils/               # fungsi bantu (respons, validasi, pagination)
├── dokumentasi/             # screenshot pengujian
│   └── end1.png
│   └── end2.png
|    .....
├── pengujian/               
├── .env.example
├── requirements.txt
├── run.py                   # entrypoint lokal
├── vercel.json
├── struktur.sql
└── data_dummy.sql
```
