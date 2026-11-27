# A
daftar_penumpang = ["William", "Kate", "Anderson", "Jame", "Mady"]
print("a. ", daftar_penumpang)

# B
daftar_penumpang.append("Jones")
print("b. ", daftar_penumpang)

# C
daftar_penumpang [2] = "Grace"
print("c. ", daftar_penumpang)

# D
print("d. ", "Thompson" in daftar_penumpang)

# E
daftar_penumpang.sort()
print("e. ", daftar_penumpang)

# F
print("f. Penumpang sampai di Yogyakarta: ")
for orang in daftar_penumpang:
    print("   -", orang)

# G
daftar_penumpang.clear()
print("g. ", daftar_penumpang)