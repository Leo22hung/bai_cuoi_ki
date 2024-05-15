class TuDien:
    def __init__(self):
        self.dictionary = {}

    def hash_function(self, album_name):
        return album_name[0]

    def NhapAlbum(self, album_name, songs):
        key = self.hash_function(album_name)
        if key not in self.dictionary:
            self.dictionary[key] = {}
        self.dictionary[key][album_name] = songs

    def XemAlbum(self, album_name):
        key = self.hash_function(album_name)
        if key in self.dictionary and album_name in self.dictionary[key]:
            print(f"Album: {album_name}")
            print("Bài hát:")
            for song in self.dictionary[key][album_name]:
                print(f"- Tên: {song['Tên bài hát']}, Nhạc sĩ: {song['Nhạc sĩ']}, Ca sĩ: {song['Ca sĩ']}")
        else:
            print("Không tìm thấy thông tin của album.")

tudien = TuDien()

songs_dreamland = [
    {"Tên bài hát": "Dreamland", "Nhạc sĩ": "Tom Walker", "Ca sĩ": "Tom Walker"},
    {"Tên bài hát": "Sun Goes Down", "Nhạc sĩ": "Tom Walker", "Ca sĩ": "Tom Walker"}
]
tudien.NhapAlbum("Dreamland", songs_dreamland)

songs_1989 = [
    {"Tên bài hát": "Shake It Off", "Nhạc sĩ": "Taylor Swift", "Ca sĩ": "Taylor Swift"},
    {"Tên bài hát": "Blank Space", "Nhạc sĩ": "Taylor Swift", "Ca sĩ": "Taylor Swift"}
]
tudien.NhapAlbum("1989", songs_1989)

tudien.XemAlbum("Dreamland")

tudien.XemAlbum("1989")
