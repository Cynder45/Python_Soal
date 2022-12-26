"""
nama_0 = str(input("Masukan nama :"))
umur_0 = str(input("Masukan umur :"))
nama_1 = str(input("Masukan nama :"))
umur_1 = str(input("Masukan umur :"))
data_nama = nama 
data_umur = umur
data_peserta = [data_nama,data_umur]
list_peserta = [data_peserta]
for peserta in list_peserta:
    print(f"nama peserta : {peserta[0]}")
    print(f"umur peserta : {peserta[1]}")
"""
for i in range(5):
    name = input("masukan nama ")
    score = float(input("masukan angka "))
    data_name = [name]
    data_score = [score]
    data_name.sort()
    data_score.sort()
    data = [data_name,data_score]
    print(data)
