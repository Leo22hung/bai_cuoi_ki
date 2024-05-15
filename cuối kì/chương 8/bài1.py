class TuDien:
    def __init__(self):
        self.dictionary = {}

    def hash_function(self, word):
        return word[0]

    def NhapTu(self, word, synonym=None, antonym=None):
        key = self.hash_function(word)
        if key not in self.dictionary:
            self.dictionary[key] = {}
        self.dictionary[key][word] = {'Đồng nghĩa': synonym, 'Trái nghĩa': antonym}

    def TraTu(self, word):
        key = self.hash_function(word)
        if key in self.dictionary and word in self.dictionary[key]:
            return self.dictionary[key][word]
        else:
            return {'Đồng nghĩa': None, 'Trái nghĩa': None}

tudien = TuDien()
tudien.NhapTu('mèo', 'cat', 'dog')
tudien.NhapTu('chó', 'dog', 'cat')

print(tudien.TraTu('mèo'))
print(tudien.TraTu('chó'))
