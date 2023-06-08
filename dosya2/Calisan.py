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

    def zam_hakki(self):
        yeni_maas = 0
        if self._tecrube >= 2 and self.tecrube <= 4 and self._maas < 15000:
            zam_orani = self._maas % self._tecrube
            self._yeni_maas += (zam_orani * self.maas / 100) + self._maas
        elif self._tecrube > 4 and self._maas < 25000:
            zam_orani = (self._maas % self._tecrube) / 2
            self._yeni_maas += (zam_orani * self.maas / 100) + self._maas
        else:
            zam_orani = 0
            self._yeni_maas = self._maas

    def _str_(self):
        self.zam_hakki()
        return f"{super()._str()}, Tecrübe: {self.tecrube}, Yeni Maaş: {self._yeni_maas}"

