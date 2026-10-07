import json

path = "data.json"

with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)


def tambah_data(nama, nim, mata_kuliah, nilai):
    data.append({
        "nama": nama,
        "nim": nim,
        "mata_kuliah": mata_kuliah,
        "nilai": nilai
    })


def simpan_data():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


while True:
    print("=== PENCATATAN NILAI MAHASISWA ===")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Keluar")

    pilihan = input("Pilih: ")

    if pilihan == "1":
        print("--- Data Nilai ---")
        for mahasiswa in data:
            print(mahasiswa)

    elif pilihan == "2":
        nama = input("Nama: ")
        nim = input("NIM: ")
        mata_kuliah = input("Mata Kuliah: ")
        nilai = float(input("Nilai: "))

        tambah_data(nama, nim, mata_kuliah, nilai)
        simpan_data()
        print("Data berhasil ditambahkan!")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")