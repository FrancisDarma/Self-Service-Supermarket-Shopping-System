"""
========WRITE_DATA_CSV==============
"""

#import modul yang diperlukan
import csv
import pandas as pd
import numpy as np

#buat class WriteData
class WriteData:
    
    """
    Class ini diperuntukkan untuk melakukan proses CRUD 
    (Create, Read, Update, Delete) input data Customer
    pada file csv sebagai stagging area sebelum keranjang
    customer final untuk kemudian di inject ke database
    SQL.

    Attributes:
        input_item(dict): berisi dictionary data yang akan diubah
        ulang_belanja(str): berisi konfirmasi Customer ulang belanja
                            sebagai syarat untuk melakukan 
                            perubahan data yaitu hanya terjadi
                            jika Customer sudah mengulang belanja
        check_first_data(boolean): berisi True/False yang muncul hanya
                                   ketika customer sudah melalui cek
                                   apabila file csv kosong atau tidak
    """
    
    #membuat atribute write class
    def __init__(self, input_item, ulang_belanja, check_first_data, input_main):
        self.input_item = input_item
        self.ulang_belanja = ulang_belanja
        self.check = check_first_data
        self.input_main = input_main

    #create fungsi input_data_pertama         
    def input_data_pertama(self, input_item):
        
        """
        Fungsi ini dipakai untuk menuliskan entry data pertama pada 
        csv stagging.
        
        Args:
            input_item(dict): input_item yang sudah melalui fungsi check_input

        Returns:
            check_first_data(Boolean): hasil dari fungsi ini berupa true atau false
                                       untuk memastikan apakah ada data pada saat
                                       file csv ditulis atau tidak
        """
        
        #coba jalankan perintah dibawah
        try:
            
            if len(input_item)!=0:
            
                #buka file csv kosong
                with open(file= "D:/pacmann/super_cashier/csv_stagging.csv", mode='w', newline='') as csvtest:

                    #definisikan nama kolom
                    cols = ['id_pembeli','nama_barang','jumlah_barang','harga_barang','kota']                   
                        
                    #define rows data dengan variable input item               
                    rows = input_item
                                        
                    # buat objek csv writer
                    csv_dict_writer = csv.DictWriter(csvtest, fieldnames = cols)      
                    
                    #menulis nama kolom
                    csv_dict_writer.writeheader()
                        
                    # tulis nama baris
                    csv_dict_writer.writerow(rows)
                    
                    #print data berhasil tersimpan
                    print('''
                            <<<Data pertama berhasil tersimpan pada csv>>>
                            ''')

                    #check apakah ini entry data pertama atau bukan
                    check_first_data = (csvtest.tell() == 0)
                
            elif len(input_item)!=0:
                
                pass
            
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi input_data_pertama:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi input_data_pertama:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi input_data_pertama:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')        
                
        #tampilkan pesan error apabila terdapat error syntax pada input_data_pertama   
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi input_data_pertama:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
                
        #munculkan perintah proses berhasil dilakukan dan input_data_pertama berhasil   
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========INPUT SUKSES======================
                      Proses tulis data pertama pada fungsi
                      input_data_pertama berhasil dilakukan 
                      =============================================
                      ''')
            
            #kembalikan nilai fungsi input_data_pertama dengan variable check_first_data
            return check_first_data
  
    #create fungsi tulis lini pertama di csv            
    def input_data_tambah(self, input_item, check_first_data, ulang_belanja):
        
        """
        Fungsi ini bertujuan untuk menuliskan data tambahan sesudah
        file csv terisi setidaknya dengan nama header
        
        Args:
            input_item(dict):
            ulang_belanja(str): Secara default parameter ulang_belanja akan berisi 'YA'
                                karena tidak mungkin menjalankan fungsi ini apabila
                                customer tidak setuju untuk mengulangi belanja.
                                
        Returns:
            Fungsi ini tidak mengembalikan nilai dari variabel apapun
        """
        #coba jalankan kode
        try:
            
            #apabila ulang belanja 'YA' dan csv tidak kosong maka       
            if ulang_belanja=='YA' and check_first_data==False and len(input_item)!=0:
            
                #buka file csv untuk append
                with open(file= "D:/pacmann/super_cashier/csv_stagging.csv", mode='a', newline='') as csvtest:
                    
                    #definisikan nama kolom
                    cols = ['id_pembeli','nama_barang','jumlah_barang','harga_barang','kota'] 
                    
                    #buat objek csv dictwriter
                    csv_writer = csv.DictWriter(csvtest, fieldnames=cols)
                    
                    #tidak tuliskan header apabila ini bukan data pertama
                    if csvtest.tell()==0:
                        
                        #tuliskan header apabila data ke 2,3,dst
                        csv_writer.writeheader()
                        
                    #tuliskan nama baris    
                    csv_writer.writerow(input_item)

                    #print data berhasil tersimpan
                    print('''
                    <<<Data tambahan berhasil tersimpan pada csv>>>
                    ''')

            #apabila customer menjawab tidak dan file csv tidak kosong
            elif ulang_belanja=='TIDAK' and check_first_data==False and (len(input_item)==0 or len(input_item)!=0):
                
                #teruskan ke baris kode berikutnya
                pass
            
            #apabila customer menjawab selain iya dan tidak dan csv entah kosong atau tidak
            else:
                
                #munculkan pesan error
                print(f'''ulang_belanja : {ulang_belanja}
                          check_first_data : {check_first_data}
                        =============ERROR===========================
                        Error pada fungsi input_data_tambah:
                        Harap masukkan kata-kata yang sesuai
                        yaitu YA/TIDAK
                        =============================================
                                    ''')   
              
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi input_data_tambah:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi input_data_tambah:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi input_data_tambah:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')          
                
        #tampilkan pesan error apabila terdapat error syntax pada input_data_tambah 
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi input_data_tambah:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #munculkan perintah proses berhasil dilakukan dan input_data_pertama berhasil   
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========INPUT SUKSES======================
                      Proses tulis tambahan data pada fungsi
                      input_data_tambah berhasil dilakukan 
                      =============================================
                      ''')
            
            
    #membaca data rekap        
    def rekap_data(self, ulang_belanja, input_main):  
        
        """
        Fungsi ini bertujuan untuk melakukan read data yang ditulis
        pada file stagging csv untuk kemudian di rekap, dihitung
        harga totalnya, diskon dan harga final setelah diskon, kemudian
        data ditampilkan  kepada customer sehingga customer bisa 
        mengambil keputusan untuk melanjutkan pembelian atau tidak
        
        Args:
            ulang_belanja(str): Secara default berisi 'TIDAK' karena menu ini
                                baru akan ditampilkan setelah customer tidak
                                mau mengulang pembelanjaan
            input_main(str): secara default pasti akan berisi 'YA' karena 
                             customer yang sudah sampai tahap ini pasti sudah
                             setuju untuk berbelanja di awal
                             
        Returns:
            list_data(dict): keranjang belanja customer yang direkap dan dihitung
                             diskonnya dikembalikan ke dictionary untuk nantinya
                             di inject ke SQL.
                             
        """
        
        #create list kosong
        list_data = []
      
        try:
               
            #read dan rekap data dilakukan apabila customer tidak akan mengulang pembelanjaan
            if ulang_belanja == 'TIDAK' and input_main == 'YA':
            
                #buka file untuk membaca
                with open(file='D:/pacmann/super_cashier/csv_stagging.csv',mode='r') as csvread:
                        
                    #read csv
                    csv_read = csv.DictReader(csvread)

                    #tampilkan header data
                    cols = csv_read.fieldnames
                    
                    #menambahkan kolom total_harga, diskon dan harga_diskon
                    cols.append('total_harga')
                    cols.append('diskon')
                    cols.append('harga_diskon')
                    
                    #tampilkan judul rekap data    
                    print('''
                        
    =====================================================================================
                        CART SUMMARY
    =====================================================================================
                        ''')   
                                
                    #lakukan perhitungan
                    for row in csv_read:
                                
                        #hitung total bayar
                        harga_barang = int(row['harga_barang'])
                        jumlah_barang = int(row['jumlah_barang'])
                        total_harga = harga_barang*jumlah_barang
                        row['total_harga'] = total_harga
                        
                        #kalkulasi diskon yang sesuai dengan total harga
                        if row['total_harga']>200000 and row['total_harga']<=300000:
                        
                            diskon = 0.05
                            harga_diskon = (1-diskon)*total_harga
                            row['diskon'] = diskon
                            row['harga_diskon'] = harga_diskon 
                        
                        #kalkulasi diskon yang sesuai dengan total harga
                        elif row['total_harga']>300000 and row['total_harga']<=500000:
                        
                            diskon = 0.06
                            harga_diskon = (1-diskon)*total_harga
                            row['diskon'] = diskon
                            row['harga_diskon'] = harga_diskon   
                             
                        #kalkulasi diskon yang sesuai dengan total harga    
                        elif row['total_harga']>500000:
                        
                            diskon = 0.07
                            harga_diskon = (1-diskon)*total_harga
                            row['diskon'] = diskon
                            row['harga_diskon'] = harga_diskon                                              
                            
                        else:
                            
                            diskon = 0
                            harga_diskon = (1-diskon)*total_harga
                            row['diskon'] = diskon
                            row['harga_diskon'] = harga_diskon
                        
                        #buat list of dictionaries
                        list_data.append(row)    
                        
                #cetak baris data
                rekap_data = pd.DataFrame(data=list_data,columns=cols)
                
                #tambahkan baris total
                total_harga_row = {
                    'id_pembeli':'',
                    'nama_barang':'Total',
                    'jumlah_barang': rekap_data['jumlah_barang'].astype(int).sum(),
                    'harga_barang':'',
                    'kota':'',
                    'total_harga': rekap_data['total_harga'].sum(),
                    'diskon':'',
                    'harga_diskon': rekap_data['harga_diskon'].sum()
                }
                
                #conver dictionary ke dataframe
                total_harga_row = pd.DataFrame([total_harga_row])
                
                #reset index baris data
                rekap_data.reset_index(drop=True, inplace=True)
                total_harga_row.reset_index(drop=True, inplace=True)
                
                #gabungkan dengan table
                rekap_data = pd.concat([rekap_data,total_harga_row], ignore_index=True)
                
                #cetak data pada terminal
                print(rekap_data.to_string(index=False))
                        
            #pengkondisian lain keluarkan keterangan not applicable
            else :
                
                #munculkan pesan error
                print(f'''ulang_belanja : {ulang_belanja}
                          input_main : {input_main}
                        =============ERROR===========================
                        Error pada fungsi rekap_data:
                        Proses tidak dapat diterapkan
                        =============================================
                                    ''')   
        
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi rekap_data:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi rekap_data:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi rekap_data:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')          
                
        #tampilkan pesan error apabila terdapat error syntax pada rekap_data  
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi rekap_data:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #munculkan perintah proses rekap data berhasil  
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========SUKSES============================
                      Proses rekap data sukses
                      =============================================
                      ''')
             
        #kembalikan nilai variable list data ke fungsi
        return list_data
    
    #create fungsi read_data
    def read_data(self):
        
        """
        Fungsi ini bertujuan untuk read data csv yang terdapat pada file csv

        Args:
        Tidak memerlukan argumen apapun

        Returns:
            list_baca(dict): mengembalikan hasil baca file csv ke dalam sebuah list
        """
        
        #coba jalankan kode program berikut
        try:
            
            #buka file csv untuk dibaca
            with open(file='D:/pacmann/super_cashier/csv_stagging.csv',mode='r') as csvread:
                    
                #buat list kosong       
                list_baca = [] 
                    
                #read csv
                csv_read = csv.DictReader(csvread)

                #tampilkan header data
                cols = csv_read.fieldnames
                    
                #cetak setiap baris            
                for row in csv_read:
                                
                    #buat list of dictionaries
                    list_baca.append(row) 
                        
                #kembalikan hasil bacaan ke dalam variable list baca      
                return list_baca      
                    
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi read_data:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi read_data:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi read_data:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')          
                
        #tampilkan pesan error apabila terdapat error syntax pada read_data  
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi read_data:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #munculkan perintah proses read data berhasil  
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========SUKSES============================
                      Proses read data sukses
                      =============================================
                      ''')
    
    #create fungsi ubah_nama
    def ubah_nama(self, nama_barang, new_data):
        
        """
        Fungsi ini berfungsi untuk melakukan perubahan nama barang
        belanjaan berdasarkan filter nama
        
        Args:
            nama_barang(str): yaitu nama barang yang akan di ubah namanya
            new_data(str): yaitu nama baru dari nama barang yang diubah
            
        Returns:
            Fungsi ini tidak akan mengembalikan nilai apapun
        """
        
        #buat list kosong
        list_data = []
        
        #coba jalankan program berikut
        try:
            
            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='r') as csvupdate:
                    
                #read csv
                csv_update = csv.DictReader(csvupdate)

                #tampilkan header data
                cols = csv_update.fieldnames
                    
                #cetak setiap baris            
                for row in csv_update:
                                
                    #buat list of dictionaries
                    list_data.append(row) 
                
                #ubah baris yang mengandung nama barang yang akan diubah
                for row in list_data:
                    if row['nama_barang'] == nama_barang:
                
                        #ubah nama barang dengan nama baru
                        row['nama_barang']=new_data

            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='w') as csvupdate:
                            
                # Menggunakan DictWriter untuk menulis data kembali ke file CSV
                writer = csv.DictWriter(csvupdate, fieldnames=list_data[0].keys())
                
                #tuliskan header kolom
                writer.writeheader()
                
                #tuliskan baris
                writer.writerows(list_data)
            
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_nama:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_nama:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_nama:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')          
                
        #tampilkan pesan error apabila terdapat error syntax pada ubah_nama
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi ubah_nama:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #munculkan perintah proses ubah nama berhasil  
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========SUKSES============================
                      Proses ubah nama sukses
                      =============================================
                      ''')
                
    #membuat fungsi mengubah ubah_jumlah       
    def ubah_jumlah(self, nama_barang, new_data):
        
        
        """
        Fungsi ini berfungsi untuk melakukan perubahan jumlah barang
        belanjaan berdasarkan filter nama
        
        Args:
            nama_barang(str): yaitu nama barang yang akan di ubah jumlahnya
            new_data(str): yaitu jumlah baru dari nama barang yang diubah
            
        Returns:
            Fungsi ini tidak akan mengembalikan nilai apapun
        """
        
        #create list kosong
        list_data = []
        
        #coba jalankan algoritma berikutnya
        try:
        
            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='r') as csvupdate:
                    
                #read csv
                csv_update = csv.DictReader(csvupdate)

                #tampilkan header data
                cols = csv_update.fieldnames
                    
                #cetak setiap baris            
                for row in csv_update:
                                
                    #buat list of dictionaries
                    list_data.append(row) 
                
                #cek baris yang mengandung nama barang yang akan diubah 
                for row in list_data:
                    if row['nama_barang'] == nama_barang:
                        
                        #ubah nama barang dengan data baru
                        row['jumlah_barang']=int(new_data)

            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='w') as csvupdate:
                            
                # Menggunakan DictWriter untuk menulis data kembali ke file CSV
                writer = csv.DictWriter(csvupdate, fieldnames=list_data[0].keys())
                
                #tuliskan header
                writer.writeheader()
                
                #tuliskan setiap baris
                writer.writerows(list_data)

        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_jumlah:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_jumlah:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_jumlah:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')          
                
        #tampilkan pesan error apabila terdapat error syntax pada ubah_jumlah 
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi ubah_jumlah:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #munculkan perintah proses ubah jumlah berhasil  
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========SUKSES============================
                      Proses ubah jumlah sukses
                      =============================================
                      ''')
            
    #create fungsi ubah_harga        
    def ubah_harga(self, nama_barang, new_data):
        
        """
        Fungsi ini berfungsi untuk melakukan perubahan harga barang
        belanjaan berdasarkan filter nama
        
        Args:
            nama_barang(str): yaitu nama barang yang akan di ubah harganya
            new_data(str): yaitu harga baru dari nama barang yang diubah
            
        Returns:
            Fungsi ini tidak akan mengembalikan nilai apapun
        """
        
        #create list kosong
        list_data = []
        
        #coba jalankan kode berikutnya
        try:
        
            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='r') as csvupdate:
                    
                # read csv
                csv_update = csv.DictReader(csvupdate)

                #tampilkan header data
                cols = csv_update.fieldnames
                    
                #cetak setiap baris            
                for row in csv_update:
                                
                    #buat list of dictionaries
                    list_data.append(row) 
                
                #cek setiap baris yang mengandung nama_barang yang ingin diubah
                for row in list_data:
                    if row['nama_barang'] == nama_barang:
                    
                        #ubah harga barang
                        row['harga_barang']=int(new_data)

            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='w') as csvupdate:
                            
                # Menggunakan DictWriter untuk menulis data kembali ke file CSV
                writer = csv.DictWriter(csvupdate, fieldnames=list_data[0].keys())
                
                #tuliskan header
                writer.writeheader()
                
                #tuliskan kembali setiap barisnya
                writer.writerows(list_data)

        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_harga:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_harga:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi ubah_harga:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')          
                
        #tampilkan pesan error apabila terdapat error syntax pada ubah_harga
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi ubah_harga:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #munculkan perintah proses ubah harga berhasil  
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========SUKSES============================
                      Proses ubah harga sukses
                      =============================================
                      ''')
            
    #buat fungsi menghapus item
    def hapus_item(self, nama_barang):

        """
        Fungsi ini berfungsi untuk menghapus item belanjaan
        belanjaan berdasarkan filter nama
        
        Args:
            nama_barang(str): yaitu nama barang yang akan di hapus dari keranjang
            
        Returns:
            Fungsi ini tidak akan mengembalikan nilai apapun
        """
        
        #create list kosong
        list_data = []
        
        #coba jalankan kode berikutnya
        try:
        
            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='r') as csvupdate:
                    
                #read csv
                csv_update = csv.DictReader(csvupdate)

                #tampilkan header data
                cols = csv_update.fieldnames
                    
                #cetak setiap baris            
                for row in csv_update:
                                
                    #buat list of dictionaries
                    list_data.append(row) 
    
            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='w') as csvupdate:

                # Menggunakan DictWriter untuk menulis data kembali ke file CSV
                writer = csv.DictWriter(csvupdate, fieldnames=list_data[0].keys())

                #tuliskan nama kolom
                writer.writeheader()
                
                #tuliskan baris yang tidak mengandung nama barang yang akan dihapus                                 
                for row in list_data:
                    if row['nama_barang'] != nama_barang:
                    
                        #tulis baris
                        writer.writerow(row)
                        
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi hapus_item:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi hapus_item:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi hapus_item:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')          
                
        #tampilkan pesan error apabila terdapat error syntax pada hapus_item  
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi hapus_item:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #munculkan perintah proses hapus item berhasil  
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========SUKSES============================
                      Proses hapus item sukses
                      =============================================
                      ''')
         
    #create fungsi reset_data            
    def reset_data(self):
        
        """
        Fungsi ini berfungsi untuk reset data keranjang menjadi kosong
        
        Args:
            Fungsi ini tidak memerlukan argumen apapun
            
        Returns:
            Fungsi ini tidak akan mengembalikan nilai apapun
        """
        
        #create list kosong
        list_data = []
        
        #coba jalankan baris perintah berikutnya
        try:
    
            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='r') as csvupdate:
                    
                #read csv
                csv_update = csv.DictReader(csvupdate)

                #tampilkan header data
                cols = csv_update.fieldnames

            #open csv file
            with open(file="D:/pacmann/super_cashier/csv_stagging.csv", mode='w') as csvupdate:
                            
                #Menggunakan DictWriter untuk menulis data kembali ke file CSV
                writer = csv.DictWriter(csvupdate, fieldnames=cols)
                
                #tuliskan nama kolom
                writer.writeheader()
                
                #tuliskan kolom kosong
                writer.writerows(list_data)
    
        #keluarkan perintah error apabila tipe dan nama input tidak sesuai 
        except (NameError, ValueError, TypeError,IndexError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi reset_data:
                    Tipe data yang dimasukkan tidak sesuai
                    =============================================
                                ''')   
        
        #memunculkan pesan terminal apabila program diberhentikan secara paksa     
        except (InterruptedError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi reset_data:
                    Program diberhentikan secara paksa
                    =============================================
                                ''')   
                
        #tampilkan pesan error apabila ada kekeliruan indentasi pada program          
        except (IndentationError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error pada fungsi reset_data:
                    Terdapat kesalahan indentasi fungsi
                    =============================================
                                ''')          
                
        #tampilkan pesan error apabila terdapat error syntax pada reset_data  
        except (SyntaxError):
                
            #munculkan pesan error
            print('''
                    =============ERROR===========================
                    Error ada fungsi reset_data:
                    Terdapat kesalahan syntax program
                    =============================================
                                ''')   
        
        #munculkan perintah proses reset data berhasil  
        finally :

            #print proses berhasil/sukses
            print('''
                      ===========SUKSES============================
                      Proses reset data sukses
                      =============================================
                      ''')
            
