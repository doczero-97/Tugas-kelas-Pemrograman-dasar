# Immutable: tanggal lahir (tipe str)
tanggal_lahir_tweedledoom = "1861-10-23"
tanggal_lahir_tweedledee = "1861-10-23"

# Mutable: kemampuan (tipe list)
kemampuan_tweedledoom = ["Bersyair", "Menyanyi", "Suka Berpura-pura"]
kemampuan_tweedledee = ["Bersyair", "Menyanyi", "Suka Berpura-pura"]

print("Sebelum :", kemampuan_tweedledee, "| id:", id(kemampuan_tweedledee))

# cari posisi "Bersyair", lalu ganti dengan "Memanah"
posisi = kemampuan_tweedledee.index("Bersyair")
kemampuan_tweedledee[posisi] = "Memanah"

print("Sesudah :", kemampuan_tweedledee, "| id:", id(kemampuan_tweedledee))
print("Tweedledoom:", kemampuan_tweedledoom)