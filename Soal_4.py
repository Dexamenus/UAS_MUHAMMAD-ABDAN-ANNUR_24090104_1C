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
    
buah1 = buah('p','p','p')
buah1.setNama('mangga')
buah1.setWarna('hijau')
buah1.setRasa('pait')
print(buah1.information())
