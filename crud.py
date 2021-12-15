# Code By AdrianProgrammer
data = []
class inviteData:
    def insert_data(nik, nama, tempat_lahir, asal_sekolah, alamat, hp, jalur):
        global data
        key = ('nik', 'nama', 'tempat_lahir', 'asal_sekolah', 'alamat', 'hp', 'jalur')
        value = (nik, nama, tempat_lahir, asal_sekolah, alamat, hp, jalur)
        todict = dict(zip(key, value))        
        data.append(todict)
        
    def validasi():
        jalur_masuk = ['[1].mandiri', '[2].prestasi', '[3].beasiswa']
        nik = int(input("Masukan Nik: "))
        nama = input("Masukan Nama: ")
        tempat_lahir = input("Masukan Tempat lahir: ")
        asal_sekolah = input("Masukan Asal sekolah: ")
        alamat = input("Masukan Alamat: ")
        hp = int(input("Masukan No hp: "))
        for i in jalur_masuk:
            print(i)
            
        choose = int(input("Masukan Jalur: "))
        if choose == 1:
            jalur = jalur_masuk[0]
        elif choose == 2:
            jalur = jalur_masuk[1]
        elif choose == 3:
            jalur = jalur_masuk[2]
        else:
            print("tidak ada dalam pilihan!")
            
        inviteData.insert_data(nik, nama, tempat_lahir, asal_sekolah, alamat, hp, jalur)
        
def show_data():
    global data
    if len(data) == 0:
        print("belom ada data!")
    else:
        for i in range(len(data)):
            print(f"{i} - {data[i]}")
        
def edit_data():
    global data
    show_data()
    choose = input("data yang ingin di ubah: ")
    if choose == 'nik':
        input1 = input("Masukan nik yang ingin di ubah: ")
        input2 = input("Masukan Nik baru: ")
        for d in data:
            d.update((k, input2) for k,v in d.items() if input1 == v)
    elif choose == 'nama':
        input1 = input("Masukan Nama yang ingin di ubah: ")
        input2 = input("Masukan Nama baru: ")
        for d in data:
            d.update((k, input2) for k,v in d.items() if input1 == v)
    elif choose == 'tempat lahir':
        input1 = input("Masukan tempat lahir yang ingin di ubah: ")
        input2 = input("Masukan tempat lahir baru: ")
        for d in data:
            d.update((k, input2) for k,v in d.items() if input1 == v)
    elif choose == 'asal sekolah':
        input1 = input("Masukan asal sekolah yang ingin di ubah: ")
        input2 = input("Masukan asal sekolah baru: ")
        for d in data:
            d.update((k, input2) for k,v in d.items() if input1 == v)
    elif choose == 'alamat':
        input1 = input("Masukan alamat yang ingin di ubah: ")
        input2 = input("Masukan alamat baru: ")
        for d in data:
            d.update((k, input2) for k,v in d.items() if input1 == v)
    elif choose == 'hp':
        input1 = input("Masukan Nomor hp yang ingin di ubah: ")
        input2 = input("Masukan Nomor hp baru: ")
        for d in data:
            d.update((k, input2) for k,v in d.items() if input1 == v)
    elif choose == 'jalur':
        input1 = input("Masukan jalur yang ingin di ubah: ")
        input2 = input("Masukan jalur baru: ")
        for d in data:
            d.update((k, input2) for k,v in d.items() if input1 == v)
    else:
        print("data tidak di temukan")
        
def hapus_data():
    global data
    show_data()
    choose = int(input("Masukan index yang ingin di hapus: "))
    for d in range(len(data)):
        if choose == d:
            del data[choose]
        else:
            print("data tidak di temukan")
            
def options():
    options = ["[1]show data", "[2]insert data", "[3]edit data", "[4]hapus data", "[5]exit"]
    for i in options:
        print(i)
        
    ask = int(input("Masukan Pilihan: "))
    if ask == 1:
        show_data()
    elif ask == 2:
        inviteData.validasi()
    elif ask == 3:
        edit_data()
    elif ask == 4:
        hapus_data()
    elif ask == 5:
        print("Good Bye!")
        exit()

while True:
    options()