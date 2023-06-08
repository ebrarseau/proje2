from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def statu_bul(self):
        etkiler = {
            "mavi yaka": 0.2,
            "beyaz yaka": 0.35,
            "yönetici": 0.45
        }
        maks_etki = 0
        en_uygun_statu = ""

        for statu, yil in self.__tecrube.items():
            try:
                yil = int(yil)
                if statu in etkiler:
                    etki = yil * etkiler[statu]
                    if etki > maks_etki:
                        maks_etki = etki
                        en_uygun_statu = statu
                else:
                    return "Geçersiz bir statü bulunuyor. Lütfen kontrol ediniz."
            except ValueError:
                return "Geçersiz bir yıl değeri bulunuyor. Lütfen kontrol ediniz."

        return en_uygun_statu

    def __str__(self):
        en_uygun_statu = self.statu_bul()
        return f"{super().__str__()}, En Uygun Statü: {en_uygun_statu}"