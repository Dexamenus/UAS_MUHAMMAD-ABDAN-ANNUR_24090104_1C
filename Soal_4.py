class buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.rasa = rasa
        self.warna = warna
    '''Metode'''
    def setNama(self, item):
        self.nama = item
    def setWarna(self, gantiwarna):
        self.warna = gantiwarna
    def setRasa(self, gantirasa):
        self.rasa = gantirasa
    def information(self):
        return f'Buah: {self.nama} | Warna : {self.warna} | Rasa: {self.rasa}'
    
mangga = buah('mangga','hijau','manis')
buah.setRasa('pait')
print(mangga.information())
