#Muhamad Rezky Pratama (152023063)


data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen":{
            "padi": 1200,
            "jagung": 800,
            "kedelai": 500
        }
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen":{
            "padi": 1500,
            "jagung": 900,
            "kedelai": 450
        }
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen":{
            "padi": 1100,
            "jagung": 750,
            "kedelai": 600
        }
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen":{
            "padi": 1300,
            "jagung": 850,
            "kedelai": 550
        }
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen":{
            "padi": 1400,
            "jagung": 950,
            "kedelai": 480
        }
    }
}
for i,j in data_panen.items():
    print(f"{i}: {j}")
print("\nJumlah hasil panen jagung dari lokasi 2 sebanyak:", data_panen["lokasi2"]["hasil_panen"]["jagung"])
print("\nNama Lokasi 3:", data_panen["lokasi3"]["nama_lokasi"])


for i, j in data_panen.items():
    jumlah_padi = int(j["hasil_panen"]["padi"])
    jumlah_kedelai = int(j["hasil_panen"]["kedelai"])
    print("\n")
    print(i)
    print(f"\nJumlah Padi {j['nama_lokasi']}: {jumlah_padi}")
    print(f"Jumlah Kedelai {j['nama_lokasi']}: {jumlah_kedelai}")

for i, j in data_panen.items():
    jumlah_padi = int(j["hasil_panen"]["padi"])
    jumlah_jagung = int(j["hasil_panen"]["jagung"])
    if jumlah_padi > 1300 or jumlah_jagung > 800:
        print(f"\nLokasi {j['nama_lokasi']}: lokasi ini memerlukan penanganan khusus")
    else:
        print(f"\nLokasi {j['nama_lokasi']}: lokasi ini dalam kondisi baik")
