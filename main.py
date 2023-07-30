
# menampilkan menu aplikasi
input_main = input('''
        ============= SUPERMARKET ABC =================    
        Halo Bapak/Ibu, selamat datang di layanan Self Service Toko ABC!
        Layanan ini merupakan inovasi terbaru untuk mempersingkat waktu
        belanja pelanggan Supermarket ABC.
        
        Silahkan untuk melanjutkan ke pemilihan barang yang akan dibeli,
        dengan ketik "YA": ''')    
    
    # mengembalikan nilai input1

# definisikan fungsi/metode menambah item
def add_item(pilihan):
    if pilihan == 'YA':
        from super_cashier import data_barang
        print("Betul")
        return pilihan 
    else:
        print("Salah")
    
add_item(input_main.upper())    