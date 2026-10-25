CREATE DATABASE budaya;
CREATE SCHEMA peta_budaya_indonesia;
set search_path to peta_budaya_indonesia;

ALTER TYPE enum_kategori ADD VALUE 'Musik Tradisional';
CREATE TYPE enum_kategori AS ENUM ('Tari',
'Pakaian', 'Kerajinan', 'Pertunjukan', 'Musik Tradisional');


CREATE TABLE "pulau"(
    "id" BIGINT primary key NOT NULL,
    "nama_pulau" VARCHAR(255) NOT NULL
);

CREATE TABLE "provinsi"(
    "id" BIGINT primary key NOT NULL,
    "nama_provinsi" VARCHAR(255) NOT NULL,
    "ibu_kota" VARCHAR(255) NOT NULL,
    "id_pulau" BIGINT NOT null,
    
    CONSTRAINT fk_provinsi_pulau FOREIGN KEY (id_pulau) REFERENCES pulau(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "budaya"(
    "id" BIGINT primary key NOT NULL,
    "id_provinsi" BIGINT NOT NULL,
    "nama_budaya" VARCHAR(255) NOT NULL,
    "deskripsi_budaya" VARCHAR(255) NOT null,
    
    CONSTRAINT fk_budaya_provinsi FOREIGN KEY (id_provinsi) REFERENCES provinsi(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "kategori"(
    "id" BIGINT primary key NOT NULL,
    "nama_kategori" enum_kategori NOT NULL DEFAULT 'Pertunjukan'
);

CREATE TABLE "kategoribudaya"(
    "id" BIGINT primary key NOT NULL,
    "id_budaya" BIGINT NOT NULL,
    "id_kategori" BIGINT NOT null,
    
    CONSTRAINT fk_kategoribudaya_budaya FOREIGN KEY (id_budaya) REFERENCES budaya(id)
        ON DELETE CASCADE ON UPDATE cascade,
   	CONSTRAINT fk_kategoribudaya_kategori FOREIGN KEY (id_kategori) REFERENCES kategori(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE "media"(
    "id" BIGINT primary key NOT NULL,
    "id_budaya" BIGINT NOT NULL,
    "url_media" VARCHAR(255) NOT null,
    
     CONSTRAINT fk_media_budaya FOREIGN KEY (id_budaya) REFERENCES budaya(id)
        ON DELETE CASCADE ON UPDATE CASCADE
    
);

CREATE INDEX idx_provinsi_pulau ON provinsi(id_pulau);
CREATE INDEX idx_budaya_provinsi ON budaya(id_provinsi);
CREATE INDEX idx_kategoribudaya_budaya_kategori ON kategoribudaya(id_budaya, id_kategori);
CREATE INDEX idx_media_budaya ON media(id_budaya);
