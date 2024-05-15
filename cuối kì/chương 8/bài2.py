class TuDien:
    def __init__(self):
        self.dictionary = {}

    def hash_function(self, word):
        return word[0]
    
    def NhapTu(self, word, synonyms=None, antonyms=None):
        key = self.hash_function(word)
        if key not in self.dictionary:
            self.dictionary[key] = {}
        self.dictionary[key][word] = {'Đồng nghĩa': synonyms, 'Trái nghĩa': antonyms}

    def DongNghia(self, word):
        key = self.hash_function(word)
        if key in self.dictionary and word in self.dictionary[key]:
            return self.dictionary[key][word]['Đồng nghĩa']
        else:
            return []

    def TraiNghia(self, word):
        key = self.hash_function(word)
        if key in self.dictionary and word in self.dictionary[key]:
            return self.dictionary[key][word]['Trái nghĩa']
        else:
            return []

tudien = TuDien()
tudien.NhapTu('mèo', synonyms=['mèo con', 'mèo nhà'], antonyms=['chó'])
tudien.NhapTu('chó', synonyms=['chó cắn', 'chó con'], antonyms=['mèo'])

print(tudien.DongNghia('mèo'))
print(tudien.TraiNghia('mèo'))
