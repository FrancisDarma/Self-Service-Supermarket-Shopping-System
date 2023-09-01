#import modul yang dibutuhkan
from write_data_csv import WriteData
from table_write import import_data_table  

# membuat kelas menu input
class MenuInput:  
    
    """
    Kelas ini bertujuan untuk mengelompokkan semua object dan method
    yang diperlukan untuk input data.
    
    Instance Attributes:
        input_main(str): yang harus diisi 'YA/TIDAK' dari menu setuju untuk memasukkan data
        input_item(dict): kumpulan dictionary item yang di input ke program
        id_pembeli(str): kode unik transaksi untuk satu kali sesi login
        ulang_belanja(str): yang harus diisi 'YA/TIDAK' dari menu mengulang belanja

    """
    
    #membuat atribut kelas MenuInput
    def __init__(self, input_main, input_item, id_pembeli, ulang_belanja, input_check_order):
        self.id_pembeli = id_pembeli
        self.input_main = input_main
        self.input_item = input_item
        self.ulang_belanja = ulang_belanja
        self.input_check_order = input_check_order
    
    #definisikan menu check_input
    def check_input(self, id_pembeli, input_main):
        
        """
        Fungsi ini punya untuk melakukan check data 
        input apakah sudah sesuai dengan tipe data yang diperlukan atau tidak.
        
        Args :
            id_pembeli(str): id otomatis dari 1 kali sesi login
            input_main : hasil 'YA/TIDAK' dari menu utama

        Returns:
            input_item(dict): hasil pengolahan input menjadi dictionary sesuai
            dengan yang program perlukan
        """

        #menampilkan menu input belanja dan input data ke dalam list
        input_item = list(input(
                ('''
                    ============= SUPERMARKET ABC ===========================    
                    Masukkan nama barang yang anda mau beli, beserta jumlahnya
                    dengan format <nama barang>,<jumlah>,<harga>,<kota>:
                    =========================================================\n'''))
                    .strip().split(',')
                )  
        
        #ketika input tidak sama dengan 4 elemen
        if len(input_item)!=4 and input_main=='YA':
                    
            #munculkan notifikasi jumlah input tidak sesuai
            print('''
                    ===============================================
                    Jumlah input yang perlu dimasukkan tidak sesuai!
                    ===============================================
                        ''') 
    
            #tampilkan kembali menu check_input
            self.check_input(id_pembeli=id_pembeli, input_main=input_main)
            
        #konversi input menjadi dictionary
        if len(input_item)==4 and input_main=='YA':    

            #coba jalankan kode mengubah input menjadi dictionary
            try:
                                    
                #buat variabel nama baris
                input_item = {'id_pembeli':id_pembeli,'nama_barang':input_item[0],'jumlah_barang':input_item[1],'harga_barang':input_item[2],'kota':input_item[3]}
                                
                #kembalikan input ke dalam sebuah dictionary
                input_item = dict(input_item)
            
                #ubah setiap values menjadi tipe data yang sesuai
                input_item['id_pembeli']=str(input_item['id_pembeli'])
                input_item['nama_barang']=str(input_item['nama_barang']).upper()
                input_item['jumlah_barang']=int(input_item['jumlah_barang'])   
                input_item['harga_barang']=int(input_item['harga_barang'])            
                input_item['kota']=str(input_item['kota']) 
                            
            #keluarkan perintah error apabila tipe, nama dan index variabel tidak sesuai   
            except (NameError, ValueError, TypeError,IndexError):
                
                #munculkan pesan error
                print('''
                    =============ERROR===========================
                    Error pada fungsi check_input :
                    Tipe dan nama data yang dimasukkan 
                    tidak sesuai
                    =============================================
                                ''')   
                
                #panggil kembali fungsi check_input
                self.check_input(id_pembeli=id_pembeli, input_main=input_main)
                
            #apabila error disebabkan karena interupsi keyboard                
            except (InterruptedError):
                
                #munculkan pesan error berikut
                print('''
                    =============ERROR===========================
                    Error pada fungsi check_input :
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
            #apabila error disebabkan karena masalah indentasi pada program
            except (IndentationError):
                
                #munculkan pesan error berikut
                print('''
                    =============ERROR===========================
                    Error pada fungsi check_input :
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')   
                
            #apabila error disebabkan karena kesalahan syntax pada program    
            except (SyntaxError):
                
                #munculkan pesan error berikut
                print('''
                    =============ERROR===========================
                    Error ada fungsi check_input :
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   

            #apabila data lolos dari pengujian sebelumnya   
            finally :
                
                #simpan dictionary ke dalam variabel input_item
                self.input_item = dict(input_item)
                                
                #print proses berhasil/sukses
                print('''
                      ==========PROSES SELESAI======================
                       Proses check input selesai dilakukan
                      =============================================
                      ''')

        #kembalikan dictionary input_item ke fungsi check_input
        return self.input_item
                
    #definisikan menu tambah_belanja untuk melakukan proses tambah_belanja
    def tambah_belanja(self, id_pembeli, input_main, input_item, check_first_data): 
        
        """
        Fungsi ini berperan sebagai menu untuk input data tambahan barang belanjaan
        yang mau dimasukkan ke dalam keranjang
        
        Args:
            id_pembeli(str): yaitu kode unik transaksi yang sudah di generate di awal
            input_main(str): hasil 'YA/TIDAK' dari menu utama
            input_item(dict): yaitu dictionary yang dihasilkan dari menu check_input

        Returns:
            _type_: _description_
        """
        
        #menampilkan perintah ulang_belanja
        ulang_belanja = input('''
             ============= SUPERMARKET ABC =================    
             Apakah Bapak/Ibu ingin menambah barang belanjaan?
             Ketik "YA" untuk menambahkan keranjang belanja: 
             ==============================================\n''')
        
        #ubah input ulang_belanja ke uppercase
        self.ulang_belanja = ulang_belanja.upper()
    
        #coba jalankan perintah berikutnya
        try:
            
            #cek input belanja bila bukan YA/TIDAK
            if self.ulang_belanja != 'YA' and self.ulang_belanja != 'TIDAK' and input_main=='YA':
                    
                #tampilkan pesan error    
                print(f'''ulang_belanja{ulang_belanja}
                    ================ERROR========================
                    Data yang anda masukkan error! Coba input
                    dengan kata yang sesuai yaitu YA/TIDAK
                    ====================================================
                    ''')
                
                #kembalikan ke variable ulang belanja
                self.ulang_belanja = self.tambah_belanja(id_pembeli=id_pembeli, input_item=input_item, check_first_data=check_first_data, input_main=input_main)

            #apabila perintah input belanja ya
            elif self.ulang_belanja == 'YA' and input_main=='YA' and check_first_data == False: 
                                            
                #buat objek menu input kembali
                input_item = self.check_input(id_pembeli=id_pembeli, input_main=input_main)
                
                #buat instance write_data
                write_data = WriteData(input_main=input_main, input_item=input_item, ulang_belanja=self.ulang_belanja, check_first_data=check_first_data)
                
                #tulis/append data
                write_data.input_data_tambah(input_item=input_item, check_first_data=check_first_data, ulang_belanja=self.ulang_belanja)
            
               #kembalikan ke variable ulang belanja
                self.ulang_belanja = self.tambah_belanja(id_pembeli=id_pembeli, input_item=input_item, check_first_data=check_first_data, input_main=input_main)
                
            #apabila ulang belanja 'TIDAK'
            elif self.ulang_belanja=='TIDAK' and input_main=='YA':
                
                #lanjutkan ke perintah berikutnya
                print('''
                      =============================================
                      Stop menambahkan keranjang belanja
                      =============================================
                      ''')      
            
        #keluarkan perintah error apabila nama variabel tidak sesuai   
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi tambah_belanja:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
                
            #kembalikan ke variable ulang belanja
            self.ulang_belanja = self.tambah_belanja(id_pembeli=id_pembeli, input_item=input_item, check_first_data=check_first_data, input_main=input_main)
                
        #memunculkan pesan terminal apabila program diberhentikan secara paksa           
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi tambah_belanja:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   

        #tampilkan pesan error apabila ada kekeliruan indentasi pada program                  
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi tambah_belanja:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila terdapat error syntax pada tambah_belanja                  
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi tambah_belanja :
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   

        #kembalikan ke list    
        return self.ulang_belanja
    
    #buat method check_order        
    def check_order(self, input_main, input_item, check_first_data, ulang_belanja):
        
        """
        Fungsi ini bertujuan untuk meminta konfirmasi customer
        apabila mereka hendak melakukan perubahan data
        
        Args:
            input_main(str): secara default berisi 'YA'
            ulang_belanja(str): secara default berisi 'TIDAK'

        Returns:
            input_check_order(str): konfirmasi Customer untuk mengubah data
                                    berupa jawaban 'YA/TIDAK'
        """
        
        #buat instance write_data
        write_data = WriteData(input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
        #jalankan fungsi rekap_data
        write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
            
        #input check order
        input_check_order = str(input('''
        =======================================================
                    Apakah pesanan diatas sudah benar 
                    dan tidak memerlukan perubahan lagi?
                    ==> Isi Ubah/Tidak
        =======================================================\n\n
              ''')
            )
        
        #uppercase input check order
        self.input_check_order = input_check_order.upper()

        #coba jalankan lini kode berikutnya
        try:
                        
            #lakukan ini apabila check order tidak sesuai input
            if self.input_check_order != 'UBAH' and self.input_check_order != 'TIDAK':
                
                #coba tampilkan pesan error
                print(
                    '''
                    ===============ERROR===========================
                    Input yang Anda masukkan tidak sesuai!
                    Tolong input dengan "ubah/tidak"
                    ==============================================
                    '''
                )
                
                #ulangi fungsi
                self.input_check_order = self.check_order(ulang_belanja=ulang_belanja, input_main=input_main, input_item=input_item, check_first_data=check_first_data)
            
            #cek apabila sesuai input
            elif self.input_check_order == 'YA' or self.input_check_order == 'TIDAK':
                
                #lanjutkan ke kode program berikutnya
                pass
             
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai   
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi check_order :
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
                
            #ulangi fungsi
            self.input_check_order = self.check_order(ulang_belanja=ulang_belanja, input_main=input_main, input_item=input_item, check_first_data=check_first_data)
                
        #memunculkan pesan terminal apabila program diberhentikan secara paksa                  
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi check_order :
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
            
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program                   
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi check_order:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')   
    
        #tampilkan pesan error apabila terdapat error syntax pada check_order                 
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi check_order:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #tampilkan proses berhasil  
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========PROSES SELESAI======================
                      Setuju untuk melakukan perubahan
                      ===============================================
                      ''')
                
        #return nilai input_check_order ke fungsi
        return self.input_check_order

    #definisikan menu checkout            
    def checkout(self, input_main, input_item, check_first_data, ulang_belanja, input_check_order):
        
        """
        Fungsi ini berfungsi untuk menunjukkan rekap data terakhir
        untuk kemudian di inject ke dalam SQL
        
        Args:
            check_order(str): secara default bernilai 'TIDAK'
            
        Returns:
            No Returns
        """
    
        #coba jalankan lini kode berikutnya
        try:
                    
            #lakukan ini apabila check_order == tidak
            if input_check_order=='TIDAK':

                #buat instance write_data
                write_data = WriteData(input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
                        
                #jalankan fungsi read data
                list = write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
                
                #injek data ke dalam table
                import_data_table(input_item=list)
                                
                #print menyimpan data ke database
                print('''
                        <<<Berhasil menyimpan data ke SQL>>>
                        ''')

                #ucapkan terima kasih
                print('''
        ====================================================================================
                            Terima kasih atas 
                            pembelanjaan yang anda lakukan
        ====================================================================================\n\n
                    ''')    
                
            #lakukan ini apabila check_order == tidak
            else:
                
                pass
            
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai   
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi checkout:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
                
            #panggil kembali fungsi checkout
            self.checkout(input_main=input_main, input_item=input_item, check_first_data=check_first_data, ulang_belanja=ulang_belanja, input_check_order=input_check_order)
                
        #memunculkan pesan terminal apabila program diberhentikan secara paksa                  
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi checkout :
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
            
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program                   
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi checkout:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')   
    
        #tampilkan pesan error apabila terdapat error syntax pada checkout                 
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi checkout:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
    
    #buat menu pilihan update
    def menu_update(self, id_pembeli, input_main, input_item, check_first_data, ulang_belanja, input_check_order):
        
        """
        Berfungsi untuk menampilkan pilihan menu dan fitur-fitur
        untuk mengubah data

        Returns:
            menu_update(str): berisi nomor pilihan menu yang di input oleh Customer
        """
        
        #coba jalankan lini program berikutnya
        try:
         
            #keluarkan menu update jika check_order iya
            if input_check_order == 'UBAH':
                
                #munculkan menu pilihan check order
                menu_update = str(input('''
                                    
                Lakukan perubahan dengan menu berikut:
                1. Ubah Nama Barang
                2. Ubah Jumlah Barang
                3. Ubah Harga Barang
                4. Hapus Barang dari keranjang
                5. Reset Keranjang
                6. Tambah Keranjang
                
                Input pilihan menu dibawah ini:\n\n
                '''))
            
                #uppercase input menu_update
                menu_update = menu_update.upper()
            
            #jika tidak ubah maka    
            elif input_check_order == 'TIDAK': 
                
                #panggil kembali fungsi checkout
                self.checkout(input_main=input_main, input_item=input_item, check_first_data=check_first_data, ulang_belanja=ulang_belanja, input_check_order=input_check_order)
                
                #uppercase input menu_update
                menu_update = 0
            
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai   
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi menu_update:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
                
            #panggil kembali fungsi menu_update
            self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, check_first_data=check_first_data, ulang_belanja=ulang_belanja, input_check_order=input_check_order)
                
        #memunculkan pesan terminal apabila program diberhentikan secara paksa                  
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi menu_update:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
            
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program                   
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi menu_update:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')   
    
        #tampilkan pesan error apabila terdapat error syntax pada menu_update                 
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi menu_update:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
                
        #kembalikan variable menu update
        return menu_update
    
    #membuat fungsi ubah nama
    def ubah(self, id_pembeli, input_main, input_item, check_first_data, ulang_belanja, menu_update):
        
        """
        Fungsi ini berperan sebagai flow control dari semua pilihan menu untuk
        perubahan data 
        
        Returns:
        No Returns
        """
        
        #coba jalankan lini program berikutnya
        try: 
            
            #buat instance write_data
            write_data = WriteData(input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
            #jika menu_update 0 maka jalankan lini berikutnya
            if menu_update==0:
                
                #lanjut ke baris program berikutnya
                pass
            
            #menjalankan perintah ubah nama barang
            elif menu_update == '1':
    
                #lihat rekap data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
                        
                #input jumlah baris
                nama_barang = str(input(
                        ('''
                            ============= SUPERMARKET ABC ===========================    
                            Masukkan nama barang yang anda akan ubah :
                            \n'''))
                            .strip()
                        ).upper()                
                
                #input nama_kolom      
                nama_item_baru = str(input(
                        ('''
                            ============= SUPERMARKET ABC ===========================    
                            Masukkan nama item baru :
                            \n'''))
                            .strip()
                        ).upper()         
                            
                #jalankan perintah ubah
                write_data.ubah_nama(nama_barang=nama_barang, new_data=nama_item_baru)

                #lihat rekap data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
        
                #tampilkan menu check order
                input_check_order = self.check_order(ulang_belanja=ulang_belanja, input_main=input_main, input_item=input_item, check_first_data=check_first_data)

                #tampilkan menu update kembali
                update = self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data, input_check_order=input_check_order)
        
                #lakukan fungsi ubah nama
                self.ubah(id_pembeli=id_pembeli, input_item=input_item, input_main=input_main, menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
            #jalankan perintah mengubah jumlah
            elif menu_update == '2':
                
                #lihat data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
                
                #input jumlah baris
                nama_barang = str(input(
                        ('''
                            ============= SUPERMARKET ABC ===========================    
                            Masukkan nama barang dari jumlah barang yang anda akan ubah :
                            \n'''))
                            .strip()
                        ).upper()                    
                
                #input nama_kolom      
                jumlah_baru = int(input(
                        ('''
                            ============= SUPERMARKET ABC ===========================    
                            Masukkan jumlah item baru :
                            \n'''))
                            .strip()
                        )         
                            
                #jalankan perintah ubah
                write_data.ubah_jumlah(nama_barang=nama_barang, new_data=jumlah_baru)

                #lihat data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
        
                #tampilkan menu check order
                input_check_order = self.check_order(ulang_belanja=ulang_belanja, input_main=input_main, input_item=input_item, check_first_data=check_first_data)

                #tampilkan menu update kembali
                update = self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data, input_check_order=input_check_order)
        
                #lakukan fungsi ubah nama
                self.ubah(id_pembeli=id_pembeli, input_item=input_item, input_main=input_main, menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
            #jalankan perintah mengubah harga barang
            elif menu_update == '3':
                
                #lihat rekap data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
                
                #input jumlah baris
                nama_barang = str(input(
                        ('''
                            ============= SUPERMARKET ABC ===========================    
                            Masukkan nama barang yang akan anda ubah :
                            \n'''))
                            .strip()
                        ).upper()                    
                
                #input nama_kolom      
                harga_baru = int(input(
                        ('''
                            ============= SUPERMARKET ABC ===========================    
                            Masukkan harga barang baru :
                            \n'''))
                            .strip()
                        )         
                            
                #jalankan perintah ubah
                write_data.ubah_harga(nama_barang=nama_barang, new_data=harga_baru)

                #lihat data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
                
                #tampilkan menu check order
                input_check_order = self.check_order(ulang_belanja=ulang_belanja, input_main=input_main, input_item=input_item, check_first_data=check_first_data)

                #tampilkan menu update kembali
                update = self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data, input_check_order=input_check_order)
        
                #lakukan fungsi ubah nama
                self.ubah(id_pembeli=id_pembeli, input_item=input_item, input_main=input_main, menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
            #jalankan perintah menghapus nama barang
            elif menu_update == '4':
                
                #lihat rekap data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
                
                #input jumlah baris
                nama_barang = str(input(
                        ('''
                            ============= SUPERMARKET ABC ===========================    
                            Masukkan nama barang yang akan anda hapus :
                            \n'''))
                            .strip()
                        ).upper()                    
                            
                #jalankan perintah ubah
                write_data.hapus_item(nama_barang=nama_barang)

                #lihat data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
        
                #tampilkan menu check order
                input_check_order = self.check_order(ulang_belanja=ulang_belanja, input_main=input_main, input_item=input_item, check_first_data=check_first_data)

                #tampilkan menu update kembali
                update = self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data, input_check_order=input_check_order)
        
                #lakukan fungsi ubah nama
                self.ubah(id_pembeli=id_pembeli, input_item=input_item, input_main=input_main, menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
        
            #jalankan perintah reset data
            elif menu_update == '5':
                
                #lihat rekap data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
                
                #jalankan perintah ubah
                write_data.reset_data()

                #lihat data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
        
                #tampilkan menu check order
                input_check_order = self.check_order(ulang_belanja=ulang_belanja, input_main=input_main, input_item=input_item, check_first_data=check_first_data)

                 #tampilkan menu update kembali
                update = self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data, input_check_order=input_check_order)
        
                #lakukan fungsi ubah nama
                self.ubah(id_pembeli=id_pembeli, input_item=input_item, input_main=input_main, menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
                    
            #jalankan perintah menambahkan kembali barang belanjaan
            elif menu_update == '6':
                
                #lihat rekap data
                write_data.rekap_data(input_main=input_main, ulang_belanja=ulang_belanja)
                
                #meminta customer untuk input tambahan barang belanjaan kedua, ketiga, dst
                ulang_belanja = self.tambah_belanja(id_pembeli=id_pembeli, input_item=input_item, check_first_data=check_first_data, input_main=input_main)
                
                #tampilkan menu check order
                input_check_order = self.check_order(ulang_belanja=ulang_belanja, input_main=input_main, input_item=input_item, check_first_data=check_first_data)

                #tampilkan menu update kembali
                update = self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data, input_check_order=input_check_order)
        
                #lakukan fungsi ubah nama
                self.ubah(id_pembeli=id_pembeli, input_item=input_item, input_main=input_main, menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
            
            #apabila memasukkan input selain menu diatas tampilkan pesan error            
            else :
                
                print('''
                      ===============================
                      Masukkan menu input yang sesuai
                      ===============================
                      ''')
                            
                #tampilkan menu update kembali
                update = self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, check_first_data=check_first_data, input_check_order=input_check_order)
        
                #lakukan fungsi ubah nama
                self.ubah(id_pembeli=id_pembeli, input_item=input_item, input_main=input_main, menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
        
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai   
        except (NameError, ValueError, TypeError,IndexError):
                
        #munculkan pesan error
             print('''
                     =============ERROR===========================
                     Error pada fungsi ubah:
                     Tipe data yang dimasukkan tidak sesuai
                     =============================================
                                ''')   
            
             #tampilkan menu update kembali
             update = self.menu_update(id_pembeli=id_pembeli, input_main=input_main, input_item=input_item, ulang_belanja=ulang_belanja, input_check_order=input_check_order)
        
             #lakukan fungsi ubah nama
             self.ubah(id_pembeli=id_pembeli, input_item=input_item, input_main=input_main, menu_update=update, ulang_belanja=ulang_belanja, check_first_data=check_first_data)
                
        #memunculkan pesan terminal apabila program diberhentikan secara paksa                  
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
            
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program                   
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')   
    
        #tampilkan pesan error apabila terdapat error syntax pada ubah             
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi ubah:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
 
        

        
 
