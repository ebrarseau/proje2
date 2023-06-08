from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = yeni_maas

    def get_sektor(self):
        return self.__sektor
    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas
    def set_maas(self, maas):
        self.__maas = maas

    def get_yeni_maas(self):
        return self.__yeni_maas
    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas
##commitliler yukarda
    def zam_hakki(self):
        try:
            yeni_maas = 0
            if self.__tecrube >= 2 and self.__tecrube <= 4 and self.__maas < 15000:
                zam_orani = self.__maas % self.__tecrube
                self.__yeni_maas += (zam_orani * self.__maas / 100) + self.__maas
            elif self.__tecrube > 4 and self.__maas < 25000:
                zam_orani = (self.__maas % self.__tecrube) / 2
                self.__yeni_maas += (zam_orani * self.__maas / 100) + self.__maas
            else:
                zam_orani = 0
                self.__yeni_maas = self.__maas
        except Exception as e:
            print("Hata oluştu:", str(e))

    def __str__(self):
        self.zam_hakki()
        return f"{super().__str__()}, Tecrübe: {self.__tecrube}, Yeni Maaş: {self.__yeni_maas}"