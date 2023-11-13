# list_material:[
#             {"NO":1,"Nama":"Gayung","Qty":10,"Jenis Material":"Padat","Peruntukan Material":"Cetak Barang","Supplier":"CV.Setia Abadi"},
#             {"NO":2,"Nama":"Kuas","Qty":20,"Jenis Material":"Padat","Peruntukan Material":"Mengcat Tembok","Supplier":"PT.DNT Indonesi"},
#             {"NO":3,"Nama":"Roll","Qty":10,"Jenis Material":"Padat","Peruntukan Material":"Mengcat Tembok","Supplier":"Mata Pelangi"},
#             {"NO":4,"Nama":"Lakban Kertas","Qty":50,"Jenis Material":"Padat","Peruntukan Material":"Menempelkan sesuatu","Supplier":"CV.Pusat Niaga Sejahtera"},
#             {"NO":5,"Nama":"Amplas","Qty":25,"Jenis Material":"Padat","Peruntukan Material":"Mengamplas benda","Supplier":"CV.Pusat Niaga Sejahtera"},
#         ]

list_material=[
            {   
                "NO":0,
                "Nama":"Gayung",
                "Qty":10,
                "Harga":2000,
                "Buffer Stock":10,
                "Supplier":"PT.DNT Indonesia"
            },
            {   
                "NO":1,
                "Nama":"Kuas",
                "Qty":20,
                "Harga":2000,
                "Buffer Stock":10,
                "Supplier":"PT.DNT Indonesia"
            },
            {   "NO":2,
                "Nama":"Roll",
                "Qty":20,
                "Harga":2000,
                "Buffer Stock":10,
                "Supplier":"Mata Pelangi"
            },
            {   
                "NO":3,
                "Nama":"Lakban Kertas",
                "Qty":20,
                "Harga":2000,
                "Buffer Stock":10,
                "Supplier":"CV.Pusat Niaga Sejahtera"
            },
            {   
                "NO":4,
                "Nama":"Amplas",
                "Qty":20,
                "Harga":2000,
                "Buffer Stock":10,
                "Supplier":"CV.Pusat Niaga Sejahtera"},
            ]
from tabulate import tabulate
#tampilin produk
def tampil():
    global list_material
    x=list_material
    # print("NO\t|Nama\t|Qty\t|Harga\t|Buffer Stock\t|Supplier")
    # for i in range(len(x)):
    #     print(f'{list_material[i]["NO"]}\t|{list_material[i]["Nama"]}\t|{list_material[i]["Qty"]}\t|{list_material[i]["Harga"]}\t|{list_material[i]["Buffer Stock"]}\t|{list_material[i]["Supplier"]}')            
    header = list_material[0].keys()
    rows = [x.values() for x in list_material]
    print(tabulate(rows, header, tablefmt="github"))

def read1 ():
    while True:
        global list_material
        x=list_material
        print("===========================================")
        print("Data material di toko Agung Abadi")
        print("===========================================\nMenu Read")
        print("1. Tampilkan seluruh data material toko ")
        print("2. Tampilkan data yang ingin di tampilkan")
        print("3. Kembali ke menu pertama")
        no=int(input("Masukan menu yang ingin di pilih="))
        if no == 1:
            print("Data material Toko Bangunan agung Abadi")
            tampil()
        elif no == 2:
            data=int(input("Masukan no material yang ingin di cari ="))
            for line in range(len(x[0])):
                if line == data:
                    header = list_material[0].keys()
                    rows = [list_material[data].values()]
                    print(tabulate(rows, header, tablefmt="github")) 
                    break
            if line != data:
                print("Data yang di cari tidak di temukan")
            
        else:
            menu()   
            
            # print(f'{list_material[line]["NO"]}\t|{list_material[line]["Nama"]}\t|{list_material[line]["Qty"]}\t|{list_material[line]["Harga"]}\t|{list_material[line]["Buffer Stock"]}\t|{list_material[line]["Supplier"]}')
            # if urutan == 0:
            #     print("Maaf kata yang anda cari tidak di temukan")
            # else:
            #     print()
            #     print(urutan)

# create
def create2 ():
    global list_material
    while True:
        print("\n===========================================")
        print("Data material di toko Agung Abadi")
        print("===========================================\nMenu Create")
        print("1. Menambahkan Material baru")
        print("2. Kembali ke menu pertama")
        pilih=int(input("Masukan menu yang ingin di pilih="))
        if pilih == 1:
            no=int(input("Masukan Index Material yang ingin di input ="))
            for cek in range (len(list_material[0])):
                if cek == no:
                    print("Data yang akan di tambahkan sudah tersedia\n")
                    break
            if cek != no :
                Nama=(input("Masukan Nama Material yang ingin di input ="))
                qty=input("Masukan qty material yang ingin di input =")
                harga=input("Masukan harga barang Material =")
                bufferStock=int(input("Masukan qty buffer stock minimum barang ="))
                supplier=input("Masukan Nama suplier =")
                list_sementara=[{}]
                list_sementara.append({
                    "NO": no,
                    "Nama": Nama,
                    "Qty": qty,
                    "Harga": harga,
                    "Buffer Stock": bufferStock,
                    "Supplier": supplier})
                header = list_material[0].keys()
                rows = [x.values() for x in list_sementara]
                # rows = [list_sementara.values()]
                print(tabulate(rows, header, tablefmt="github"))    
                yakin=input("Apakah anda yakin ingin menyimpan data tersebut?(Ya/tidak)")
                if yakin == "Ya":
                    list_material.append({
                    "NO": no,
                    "Nama": Nama,
                    "Qty": qty,
                    "Harga": harga,
                    "Buffer Stock": bufferStock,
                    "Supplier": supplier})
                    print("Data berhasil disimpan")
                    tampil()
                elif yakin == "tidak":
                    create2 ()
        elif pilih == 2:
            menu()
            

def hapus3():
    global list_material
    tampil()
    print("===========================================")
    print("Data material di toko Agung Abadi")
    print("===========================================\nMenu Hapus")
    print("1. Pilih nomor data yang ingin di hapus")
    print("2. kembali ke menu awal")
    pilih=int(input("Masukan menu yang ingin di pilih ="))
    if pilih == 1:
        hapus=int(input("Masukan nomor data yang ingin di hapus ="))
        index={item['NO']: item for item in list_material}
        # for i, item in enumerate(list_material):
        if hapus in index:
            yakin=input("apakah anda yakin ingin menghapus?(Ya/tidak)")
            if yakin == "Ya":
                for i,item in enumerate(list_material):
                    if item["NO"]== hapus:
                        del list_material [i]
                        print("Data berhasil di hapus")
                        tampil ()
                        break
        else:
            print(f"Nomor {hapus} yang akan di hapus tidak tersedia\n")
        
        
    
def update():
    while True:
        global list_material
        print("===========================================")
        print("Data material di toko Agung Abadi")
        print("""1. Update data""")
        print("2. kembali ke menu awal")
        pilih=int(input("Masukan menu yang ingin di pilih ="))
        if pilih == 1:
            tampil ()
            nomor_index=int(input("Masukan no data yang ingin di update ="))
            header = list_material[0].keys()
            rows = [list_material[nomor_index].values()]
            print(tabulate(rows, header, tablefmt="github"))    
            for index in range(len(list_material)):
                if index == nomor_index:
                    print("Kolom apa yang ingin di ubah ")
                    print("1. Kolom NO")
                    print("2. Kolom nama")
                    print("3. Kolom Qty")
                    print("4. Kolom Harga")
                    print("5. Kolom Buffer stock")
                    print("6. Kolom Supplier")
                    kolom=int(input("Masukan nomor untuk memilih kolom yang diubah ="))
                    if kolom == 1:
                        ubah=int(input("Masukan nomor baru="))
                        list_material[nomor_index].update({"NO":ubah})
                        print(list_material)
                        tampil()
                    elif kolom == 2:
                        ubah=(input("Masukan nama baru="))
                        list_material[nomor_index].update({"Nama":ubah})
                        tampil()
                    elif kolom == 3:
                        ubah=int(input("Masukan qty baru="))
                        list_material[nomor_index].update({"Nama":ubah})
                        tampil()
                    
                    elif kolom == 4:
                        ubah=int(input("Masukan harga baru="))
                        list_material[nomor_index].update({"Nama":ubah})
                        tampil()    
                    
                    elif kolom == 5:
                        ubah=int(input("Masukan qty buffer stock baru="))
                        list_material[nomor_index].update({"Nama":ubah})
                        tampil()
                    
                    elif kolom == 6:
                        ubah=input("Masukan nama supplier baru=")
                        list_material[nomor_index].update({"Supplier":ubah})
                        tampil()
                    else:
                        print("Nomor yang anda pilih tidak tersedia")
        else:
            menu()
keranjang=[]
def beli ():
        global list_material,keranjang
        x=list_material
        y=keranjang
        tampil()
        while True:
        # header = ["NO","Nama","Qty","Harga"]
        # rows = [x.values() for x in list_material]
        # print(tabulate(rows, header, tablefmt="github"))
            pilih=int(input("Masukan nomor barang yang ingin di beli =") )
            jumlah=int(input("Masukan jumlah yang di inginkan ="))
            if list_material[pilih]["Qty"]<jumlah:
                print("Stock barang tidak mencukupi")
                continue
                    
            keranjang.append({
                "NO": list_material[pilih]["NO"],
                "Nama": list_material[pilih]["Nama"],
                "Qty": jumlah,
                "Harga": list_material[pilih]["Harga"],
                "Total":jumlah*list_material[pilih]["Harga"]})
            break
            # print(keranjang)
            # header = keranjang[0].keys()
            # rows = [keranjang[0].values()]
            # print(tabulate(rows, header, tablefmt="github"))
        kondisi=True
        while kondisi:
            tambahan=input("Apakah anda ingin menambah pesanan?(Ya/tidak) ")
            if tambahan.lower() == "ya":
                pilih=int(input("Masukan nomor barang yang ingin di beli = ") )
                jumlah=int(input("Masukan jumlah yang di inginkan = \n"))
                if list_material[pilih]["Qty"]<jumlah:
                    print("Stock barang tidak mencukupi")
                    continue
                keranjang.append({
                "NO": list_material[pilih]["NO"],
                "Nama": list_material[pilih]["Nama"],
                "Qty": jumlah,
                "Harga": list_material[pilih]["Harga"],
                "Total":jumlah*list_material[pilih]["Harga"]})
                header = ["NO","Nama","Qty","Harga","Total"]
                rows = [x.values() for x in y]
                print(tabulate(rows, header, tablefmt="github"))
                continue
            elif tambahan == "tidak":
                pass
        # yakin=input("Apakah anda yakin dengan barang belanja anda sudah cukup?(Ya/tidak)= ")
        # if yakin == "Ya":
            total_belanja = sum(item["Total"]for item in keranjang)
            # header = ["NO","Nama","Qty","Harga","Total"]
            # rows = [x.values() for x in y]
            # print(tabulate(rows, header, tablefmt="github"))
            print(f"Total belanja ={total_belanja}")
            while kondisi:
                input_uang=int(input("Masukan Jumlah uang : "))
                if input_uang == total_belanja:
                    print("Terima kasih")
                    kondisi=False
                    break
                elif input_uang < total_belanja:
                    print(f"Uang anda kurang sebesar :{(total_belanja-input_uang)}")
                    continue
                elif input_uang > total_belanja:
                    print(f"\nTerima kasih\nUang kembalian anda : {input_uang-total_belanja}")
                    kondisi=False
                    break
                else:
                    break
    # elif yakin == "tidak"
    #         menuCustomer()

    

             
            # print(rows)
            # print(type(rows))
            # print(len(rows))
            # for x in keranjang:
            #     total=["Total"][0+x]
            #     print(total)
            #     header = ["NO","Nama","Qty","Harga","Total"]
            #     rows = [x.values() for x in y]
            
        



def menuCustomer():
    print("\n================================================")     
    print("Selamat Datang Di Toko Material CV agung mandiri")
    print("================================================")
    print("1. Menampilkan Daftar Material")
    print("2. Membeli Material")
    print("3. Exit Program")
    No_menu=int(input("Masukan nomor menu :"))
    if No_menu == 1:
        read1()
    elif No_menu ==2:
        beli ()
        menuCustomer()
    elif No_menu == 3:
        print("Terima Kasih sudah berbelanja di toko kami")
        exit ()



while  True:
    login=input("Apakah anda Pemilik Toko (Ya/tidak) = ")
    if login == "Ya":
        pasword=input("Masukan password anda = ")
        if pasword == "admin123":
            print("Selamat password anda berhasil") 
            break
        else:
            print("Coba lagi ingat 'admin'") 
    elif login == 'tidak':
        menuCustomer ()
    else:
        print("Coba lagi,jawaban harus sesuai (Ya/tidak)")


def menu () :
    while  True:
            print("================================================")     
            print("Selamat Datang Di Toko Material CV agung mandiri")
            print("================================================")
            print("List Menu\n")
            print("1. Menampilkan Daftar Material")
            print("2. Menambah Material")
            print("3. Menghapus Material")
            print("4. Update Material")
            print("5. Membeli Material")
            print("6. Exit Program")
            No_menu=(input("Masukan nomor menu = "))
            if No_menu == '1':
                read1()
                menu()
            elif No_menu == '2':
                create2()
                menu()
            elif No_menu == '3':
                hapus3()
                menu()
            elif No_menu == '4':
                update()
            elif No_menu == '5':
                beli ()
            elif No_menu == '6':
                print("Anda berhasil keluar")
                exit()
            
menu()


