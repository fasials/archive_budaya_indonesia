begin;
set search_path to peta_budaya_indonesia;

insert into peta_budaya_indonesia.pulau
    (id, nama_pulau)
values
    (1, 'jawa'),
    (2, 'bali'),
    (3, 'sumatera');

INSERT INTO peta_budaya_indonesia.provinsi
    (id, nama_provinsi, ibu_kota, id_pulau)
VALUES
    (1, 'Jawa Tengah', 'Semarang', 1),
    (2, 'Jawa Barat', 'Bandung', 1),
    (3, 'Jawa Timur', 'Surabaya', 1),
    (4, 'Bali', 'Denpasar', 2),
    (5, 'Sumatera Barat', 'Padang', 3);

INSERT INTO peta_budaya_indonesia.budaya
    (id, id_provinsi, nama_budaya, deskripsi_budaya)
VALUES
    (1, 1, 'Tari Gambyong','Tarian tradisional yang berkembang di lingkungan budaya Jawa.'),
    (2, 1, 'Wayang Kulit','Seni pertunjukan wayang dengan tokoh yang dimainkan di balik layar.'),
    (3, 2, 'Angklung','Alat musik tradisional yang dimainkan dengan cara digoyangkan.'),
    (4, 2, 'Kebaya Sunda','Busana tradisional yang dikenakan dalam berbagai acara adat.'),
    (5, 3, 'Reog Ponorogo','Seni pertunjukan tradisional yang terkenal dengan dadak merak.'),
    (6, 4, 'Tari Kecak','Pertunjukan tari yang menggunakan paduan suara penari sebagai pengiring.'),
    (7, 5, 'Tari Piring','Tarian tradisional yang menggunakan piring sebagai properti tari.'),
    (8, 5, 'Songket Minangkabau','Kain tradisional dengan hiasan benang emas atau perak.');

INSERT INTO peta_budaya_indonesia.kategori
    (id, nama_kategori)
VALUES
    (1, 'Pertunjukan'),
    (2, 'Pakaian'),
    (3, 'Kerajinan'),
    (4, 'Tari'),
    (5, 'Musik Tradisional');

INSERT INTO peta_budaya_indonesia.kategoribudaya
    (id, id_budaya, id_kategori)
VALUES
    (1, 1, 1), -- tari gambyong
    (1, 1, 4), 

    (2, 2, 1), -- wayang kulit
    (2, 2, 3), 

    (3, 3, 3), -- angklung
    (3, 3, 5),

    (4, 4, 2), -- kebaya sunda
    (4, 4, 3), 

    (5, 5, 1), -- reog ponorogo
    (5, 5, 4), 

    (6, 6, 1), -- tari kecak
    (6, 6, 4), 

    (7, 7, 1), -- tari piring
    (7, 7, 4),

    (8, 8, 2), -- songket minang
    (8, 8, 3); 

INSERT INTO peta_budaya_indonesia.media
    (id, id_budaya, url_media)
VALUES
    (1, 1, 'https://example.com/tari-gambyong.jpg'),
    (2, 1, 'https://example.com/tari-gambyong-2.jpg'),
    (3, 2, 'https://example.com/wayang-kulit.jpg'),
    (4, 3, 'https://example.com/angklung.jpg'),
    (5, 4, 'https://example.com/kebaya-sunda.jpg'),
    (6, 5, 'https://example.com/reog-ponorogo.jpg'),
    (7, 6, 'https://example.com/tari-kecak.jpg'),
    (8, 7, 'https://example.com/tari-piring.jpg'),
    (9, 8, 'https://example.com/songket-minangkabau.jpg');

COMMIT;