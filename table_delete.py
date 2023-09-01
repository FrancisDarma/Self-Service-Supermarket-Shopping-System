#import library yang diperlukan
from sqlalchemy import create_engine, text

#create fungsi hapus table
def hapus_table():
    
    """
    Fungsi ini bertujuan untuk melakukan penghapusan
    terhadap table sql yang sudah dibuat sebelumnya
    
    Args:
    Tidak memerlukan parameter apapun
    
    Returns:
    Tidak mengembalikan nilai apapun
    """

    #membuat SQLite database engine
    engine = create_engine('sqlite:///data_super_cashier.db')

    #membangun koneksi ke database
    conn = engine.connect()

    #eksekusi query SQL untuk membuat table transaksi
    conn.execute(text("""
                        DROP TABLE transaksi;
                    """))
    
    #tutup koneksi database
    conn.close()
    
#jalankan fungsi    
hapus_table()