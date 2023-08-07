# Buka file nama_file.csv
# mode = 'w' (write) atau mode tulis
# newline untuk mendefinisikan pemisah antar baris

def write_data_to_csv(input_item):
    
    # Import modul csv
    import csv

    with open(file= "D:/pacmann/super_cashier/test_txt_data/csv_test.csv", mode='w', newline='') as csvtest:
        # definisikan nama kolom
        cols = ['nama_barang','harga_barang','jumlah_barang']   
            
        # buat objek csv writer
        csv_dict_writer = csv.DictWriter(csvtest, fieldnames = cols)
            
        # tulis nama kolom
        csv_dict_writer.writeheader()
            
        # buat variabel nama baris
        rows = [
                {'nama_barang':input_item[0],'harga_barang':input_item[1],'jumlah_barang':input_item[2]}
                ]
            
        # tulis nama baris
        csv_dict_writer.writerows(rows)

        
    with open(file='D:/pacmann/super_cashier/test_txt_data/csv_test.csv',mode='r',newline='') as csvread:
            
        # read csv
        csv_read = csv.DictReader(csvread)
            
        # Looping baris data
        for rows in csv_read:
                
            #cetak baris data
            print(rows)
            print("Data berhasil tersimpan")
    