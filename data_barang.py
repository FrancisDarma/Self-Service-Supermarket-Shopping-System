import numpy as np
import pandas as pd

list_barang = {
    'nama_barang':['Tahu', 'Tempe', 'Susu Kedelai', 'Beras 5 Kg', 'Minyak Goreng', 'Ayam Broiler', 'Sapi Lokal', 'Fillet Salmon', 'Udang Windu', 'Kerang Darah'],
    'harga_barang':[2000, 3000, 2500, 30000, 15000, 35000, 120000, 200000, 50000, 30000]
}

table_barang = pd.DataFrame(data=list_barang, columns=[keys for keys in list_barang])
table_barang