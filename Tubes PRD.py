# Tubes PRD
file_data = open("data.csv","r")
def count_row(file):
    # Subprogram untuk menghitung jumlah baris dari file csv
    
    # Kamus Lokal
    # rowcount: int

    # Algoritma
    # Inisialisasi rowcount menjadi 0
    rowcount  = 0
    # Iterasi menghitung count sepanjang file
    for row in file:
        rowcount+= 1
    return rowcount

def parsing_file2(nama_tempat,var1,var2,var3,var4):
    # Subprogram untuk menginisialisasi file data.csv

    file_data = open('data.csv','r')
    Lines = file_data.readlines()
    
    count = 0
    for line in Lines:
        nama_tempat[count] = ""
        i = 0
        while i<len(line):
            if line[i] !=";":
                nama_tempat[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var1[count] = ""
        while i<len(line):
            if line[i] !=";":
                var1[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var2[count] = ""
        while i<len(line):
            if line[i] !=";":
                var2[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var3[count] = ""
        while i<len(line):
            if line[i] !=";":
                var3[count]+=line[i]
                i+=1
            else:
                break
        i+=1
        var4[count] = ""
        if count != (row_data-1):
            while i<(len(line)-1):
                if line[i] !=";":
                    var4[count]+=line[i]
                    i+=1
                else:
                    break
        else:
            while i<len(line):
                if line[i] !=";":
                    var4[count]+=line[i]
                    i+=1
                else:
                    break            
        count+=1
    return nama_tempat,var1,var2,var3,var4


row_data = count_row(file_data)
nama_tempat = [0 for i in range(row_data)]
kategori_tempat = [0 for i in range(row_data)]
kategori2 = [0 for i in range(row_data)]
range_budget = [0 for i in range(row_data)]
deskripsi = [0 for i in range(row_riwayat)]
parsing_file2(nama_tempat,kategori_tempat,kategori2,range_budget,deskripsi)

print("Selamat datang di aplikasi Traveller. Berapa lama Anda akan menjelajahi Bandung?")
hari = input()
print("\n")
print("Kami menyarankan agar setiap hari hanya diisi 8-10 jam aktivitas untuk mengantisipasi kejadian tak terduga dan mengakomodasi waktu perjalanan")
print("Silahkan memilih kategori aktivitas kegiatan yang ingin dilakukan: ")
print("Kegiatan air")
print("Wisata Alam")
print("Museum")
print("Spot Foto")
print("Kuliner")
print("Anak anak")
print("Trekking")
print("Panjat Tebing")
