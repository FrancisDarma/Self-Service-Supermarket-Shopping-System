"""
==========SUPER_CASHIER_1.0================
Ini adalah file main dari program
SUPER CASHIER 1.0
===========================================
"""

#import modul dan class-class yang diperlukan
from modul_id import IDPembeli
from modul_belanja import MenuInput
from write_data_csv import WriteData
    
#create fungsi main menu
def main_menu():
    
    """
    Fungsi ini berperan sebagai file utama dan terpusat untuk
    eksekusi setiap modul yang mendukung algoritma yang terdapat
    pada file ini
    
    Args:
        Fungsi ini akan langsung dijalankan tanpa argumen apapun
        
    Returns:
        Fungsi ini tidak akan di return terhadap nilai sebuah variabel
    """
    # menampilkan menu aplikasi utama


    #create konfirmasi melanjutkan belanja
    input_main = input('''
                ============= SUPERMARKET ABC ==================================    
                Halo Bapak/Ibu, selamat datang di layanan Self Service Toko ABC!
                Layanan ini merupakan inovasi terbaru untuk mempersingkat waktu
                belanja pelanggan Supermarket ABC.
                
                Silahkan untuk melanjutkan ke pemilihan barang yang akan dibeli,
                dengan ketik "YA": ''')    

    #uppercase hasil input_main
    input_main = input_main.upper()

    #coba jalankan kode dibawah
    try:
        
        #lanjut ke menu berikutnya apabila user menjawab ya
        if input_main == "YA":
            
            #buat objek dictionary
            input_item = {}
            
            #create unik user ID
            id_pembeli = IDPembeli(agree=input_main).generate_id(agree=input_main)
            
            #buat objek menu_input_instance dari class MenuInput
            menu_input_instance = MenuInput(input_main=input_main, input_item=input_item, id_pembeli=id_pembeli, ulang_belanja=None, input_check_order=None, input_menu_update=None)
            
            #masukkan entry untuk data pertama dengan menggunakan menu check input
            input_item = menu_input_instance.check_input(id_pembeli=id_pembeli, input_main=input_main)
            
            #create instance dari write data
            write_data = WriteData(input_main=input_main, input_item=input_item, ulang_belanja=None, check_first_data=None)
            
            #tuliskan data pertama pada csv dengan instance WriteData
            check_first_data = write_data.input_data_pertama(input_item=input_item)
            
            #meminta customer untuk input tambahan barang belanjaan kedua, ketiga, dst
            ulang_belanja = menu_input_instance.tambah_belanja(id_pembeli=id_pembeli, input_item=input_item, check_first_data=check_first_data, input_main=input_main)
            
            #lakukan checking pada tipe data customer agar sesuai dengan kebutuhan sistem
            input_check_order = menu_input_instance.check_order(input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
            #tampilkan konfirmasi ubah data dan pilihan menu ubah data
            update = menu_input_instance.menu_update(input_check_order=input_check_order, input_item=input_item, input_main=input_main, id_pembeli=id_pembeli, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
            #jalankan perintah lanjutan dan eksekusi untuk setiap menunya
            menu_input_instance.ubah(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, input_menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
        #tampilkan pesan terima kasih apabila customer memutuskan untuk tidak melanjutkan belanja
        elif input_main == "TIDAK":
            
            print('''
                ===========================================================
                Terima kasih untuk kesediaan Anda menggunakan aplikasi ini
                ===========================================================''')
            
        #tampilkan error apabila customer memasukkan input selain ya/tidak
        else:
            
            #pesan error yang dimunculkan
            print('''
                ===============ERROR=========================
                Error pada fungsi main_menu :
                Masukkan kata-kata yang sesuai!
                Masukkan YA/TIDAK
                =============================================
                ''')
            
            main_menu()
            
     #keluarkan perintah error apabila tipe dan nama input tidak sesuai   
    except (NameError, ValueError, TypeError, IndexError):
                
              #munculkan pesan error
              print('''
                      =============ERROR===========================
                      Error pada fungsi main_menu :
                      Tipe data yang dimasukkan tidak sesuai
                      =============================================
                                  ''')   
              
    #memunculkan pesan terminal apabila program diberhentikan secara paksa            
    except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi main_menu :
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
    
    #tampilkan pesan error apabila ada kekeliruan indentasi pada program            
    except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi main_menu:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')   
    
    #tampilkan pesan error apabila terdapat error syntax pada main_menu         
    except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi main_menu:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
            
    return input_main
        
#jalankan perintah main menu    
main_menu()
