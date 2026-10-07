# study_kasus_6.
Nama  : soraya ghina
Nim   : 2609116081
Kelas : c

FILE JSON 

<img width="818" height="831" alt="Screenshot 2026-10-07 223143" src="https://github.com/user-attachments/assets/7c20ca2c-81ff-4101-ba6f-633fbfd7a686" />

File data.json digunakan untuk menyimpan data nilai mahasiswa. Di dalamnya terdapat informasi berupa nama, NIM, mata kuliah, dan nilai. Setiap mahasiswa disimpan dalam bentuk objek { }, sedangkan seluruh data mahasiswa disimpan dalam satu kumpulan [ ]. Data ini nantinya dapat dibaca dan ditambahkan melalui program Python, sehingga data tetap tersimpan meskipun program dijalankan kembali.


PENJELASAN KODING

import json
Kode ini digunakan untuk mengimpor library JSON agar Python dapat membaca dan menyimpan data dalam format JSON.

path = "data.json"
Kode ini digunakan untuk menentukan file yang akan digunakan untuk menyimpan data, yaitu data.json.

with open(path, "r", encoding="utf-8") as f: data = json.load(f)
Kode ini digunakan untuk membuka file data.json dan membaca data yang sudah tersimpan di dalam file tersebut.

def tambah_data(nama, nim, mata_kuliah, nilai): data.append({...})
Kode ini digunakan untuk membuat fungsi yang berfungsi menambahkan data mahasiswa berupa nama, NIM, mata kuliah, dan nilai.

def simpan_data(): with open(path, "w", encoding="utf-8") as f: json.dump(data, f, indent=4)
Kode ini digunakan untuk membuat fungsi yang berfungsi menyimpan data yang sudah ditambahkan ke dalam file data.json.

while True: print("=== PENCATATAN NILAI MAHASISWA ===") print("1. Tampilkan Data") print("2. Tambah Data") print("3. Keluar")
Kode ini digunakan untuk membuat menu utama program yang berisi pilihan menampilkan data, menambah data, dan keluar dari program.

pilihan = input("Pilih: ")
Kode ini digunakan untuk meminta pengguna memasukkan pilihan menu yang ingin dijalankan.

if pilihan == "1": print("--- Data Nilai ---") for mahasiswa in data: print(mahasiswa)
Kode ini digunakan untuk menampilkan seluruh data mahasiswa yang sudah tersimpan ketika pengguna memilih menu nomor 1.

elif pilihan == "2": nama = input("Nama: ") nim = input("NIM: ") mata_kuliah = input("Mata Kuliah: ") nilai = float(input("Nilai: "))
Kode ini digunakan untuk meminta pengguna memasukkan nama, NIM, mata kuliah, dan nilai mahasiswa ketika memilih menu nomor 2.


tambah_data(nama, nim, mata_kuliah, nilai) simpan_data() print("Data berhasil ditambahkan!")
Kode ini digunakan untuk menambahkan data yang sudah dimasukkan dan menyimpannya ke dalam file data.json.

elif pilihan == "3": print("Program selesai.") break else: print("Pilihan tidak tersedia.")
Kode ini digunakan untuk menghentikan program ketika pengguna memilih menu nomor 3 dan menampilkan pesan jika pengguna memasukkan pilihan yang tidak tersedia.

<img width="1222" height="1032" alt="Screenshot 2026-10-07 223111" src="https://github.com/user-attachments/assets/4843305f-2312-4122-a77a-5c27157239a1" />

<img width="655" height="355" alt="Screenshot 2026-10-07 223128" src="https://github.com/user-attachments/assets/0fea436a-018d-4c6a-adf3-8a99320cf78f" />

PENJELASAN OUTPUT
<img width="1288" height="997" alt="Screenshot 2026-10-07 223051" src="https://github.com/user-attachments/assets/249c8568-fe04-4193-a735-92e037e6a1ba" />

Tampilkan Data
Tambah Data
Keluar
Pilih:

Kalau pilih 1, program menampilkan data yang sudah ada di data.json.

Kalau pilih 2, program akan meminta:

Nama:

NIM:

Mata Kuliah:

Nilai:

Setelah diisi, muncul:

Data berhasil ditambahkan!

Kalau pilih 3, muncul:

Program selesai.






