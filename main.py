import pdb

# pdb.set_trace()

# menampilkan menu aplikasi utama
input_main = input('''
        ============= SUPERMARKET ABC =================    
        Halo Bapak/Ibu, selamat datang di layanan Self Service Toko ABC!
        Layanan ini merupakan inovasi terbaru untuk mempersingkat waktu
        belanja pelanggan Supermarket ABC.
        
        Silahkan untuk melanjutkan ke pemilihan barang yang akan dibeli,
        dengan ketik "YA": ''')    

#lanjut ke menu berikutnya apabila user menjawab ya
if input_main.upper() == "YA": 
    
    #import menu input_belanja
    from modul_belanja import input_belanja
    from modul_belanja import check_input
    from write_data import write_data_to_csv
    
    #check input
    write_data_to_csv(check_input(input_belanja(input_main=input_main.upper()))) 

#keluar apabila user pilih tidak
elif input_main.upper() == "TIDAK":
    print("Terima kasih untuk kesediaan Anda menggunakan aplikasi ini")
    
#tampilkan error apabila input selain ya/tidak
else :
    raise Exception("Input error!")






