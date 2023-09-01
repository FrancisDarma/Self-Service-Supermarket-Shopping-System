#import library yang diperlukan
from sqlalchemy import create_engine, text

#create fungsi buat table
def connect_sql():
    
    """
    Fungsi ini bertujuan untuk membuat table yang akan menampung
    database final data super cashier
    
    Args:
    Tidak memerlukan parameter
    
    Returns:
    Tidak melakukan return terhadap fungsi
    """

    #membuat SQLite database engine
    engine = create_engine('sqlite:///data_super_cashier.db')

    #membangun koneksi ke database
    conn = engine.connect()

    #eksekusi query SQL untuk membuat table transaksi
    conn.execute(text("""
                    CREATE TABLE transaksi(
                        id_transaksi INTEGER PRIMARY KEY,
                        id_pembeli VARCHAR,
                        nama_barang VARCHAR,
                        jumlah_barang INT,
                        harga_barang INT,
                        kota STRING,
                        total_harga INT,
                        diskon INT,
                        harga_diskon INT,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                    """))
    
    #tutup koneksi
    conn.close()
    
#jalankan fungsi
connect_sql()