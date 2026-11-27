# A
hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}
print("a. Belanja hari pertama: ", hari_pertama, "\n   Belanja hari kedua: ", hari_kedua)

# B
hari_kedua.add("keju")
print("b. ", hari_kedua)

# C
c = hari_pertama.intersection(hari_kedua)
print("c. ", c)

# D
d = hari_pertama.difference(hari_kedua)
print("d. ", d)

# E
hari_pertama.remove("garam")
print("e. ", hari_pertama)

# F
f = hari_kedua.difference(hari_pertama)
print("f. ", f)

# G
g = hari_pertama.symmetric_difference(hari_kedua)
print("g. ", g)

# H
print("h. ", hari_pertama)

# I
print("i. ", hari_kedua)
