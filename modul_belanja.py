import pdb

# mendefinisikan menu input belanja
def input_belanja(input_main="YA"):
    
    #memasukkan fungsi debugger
    #pdb.set_trace()

    # menampilkan menu input belanja dan input data ke dalam list
    input_item = list(input(
            ('''
                ============= SUPERMARKET ABC =================    
                Masukkan nama barang yang anda mau beli, beserta jumlahnya
                dengan format <nama barang>,<jumlah>,<harga>:\n
                ''')).split(',')
            )  
             
    #kembalikan
    return input_item


def check_input(input_item):   
    
    # kondisi agar input_belanja muncul
    if len(input_item)==3: 
        
        #mencoba ubah tipe variabel
        try:
            
            input_item[0]=str(input_item[0])
        
        #keluarkan perintah error apabila nama variabel tidak sesuai   
        except (NameError, ValueError, TypeError):
            
            print('''
                            Tipe data yang dimasukkan tidak sesuai
                            ''')   
            
            # panggil kembali fungsi input belanja
            input_belanja(input_main="YA")
            
        #mencoba ubah tipe variabel
        try:
            
            input_item[1]=int(input_item[1])
            input_item[2]=int(input_item[2])   
        
        #keluarkan perintah error apabila nama variabel tidak sesuai             
        except (NameError, ValueError, TypeError):
            
            print('''
                            Tipe data yang dimasukkan tidak sesuai
                            ''')   
            
            #panggil kembali fungsi input belanja
            input_belanja(input_main="YA")
        
        #mengembalikan variabel input_item    
        finally :
            
            return input_item   
        
    #cek jumlah data apabila tidak sesuai format
    elif len(input_item)>3 or len(input_item)<3:
            
        #munculkan tanda salah jumlah input
        print('''
            Jumlah input yang perlu dimasukkan tidak sesuai
                  ''') 



        

        
 
