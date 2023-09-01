#masukkan modul yang dibutuhkan
import time
import random

#create Class IDPembeli untuk menciptakan UID
class IDPembeli():
    
    """
    Modul ini diciptakan untuk menciptakan UID bagi customer
    
    Attributes:
        counter(int): yaitu komponen id customer berdasarkan jumlah, dimulai dari 0 ke 9
        agree(str): berisi persetujuan customer untuk melanjutkan belanja
        
    Returns:
    Tidak mengembalikan nilai apapun
    """

    def __init__(self,agree):
        self.counter = 0
        self.agree = agree
    
    #modul untuk menciptakan UID dengan random serial transaction
    def generate_id(self, agree):
        
        #apabila customer menjawab setuju untuk melanjutkan proses belanja
        if self.agree == 'YA':
            
            #catat timestamp realtime
            timestamp=int(time.time())
            
            #buat random number 
            random_part = random.randint(1000,9999)
            
            #setiap penambahan customer create tambahan 
            self.counter += 1
            return f'{timestamp}_{random_part}_{self.counter}'
        
        #apabila syarat tidak terpenuhi maka lewati ke baris selanjutnya
        else:
            
            pass