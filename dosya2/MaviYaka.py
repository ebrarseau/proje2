from Calisan import Calisan
class MaviYaka(Calisan):
    def _init_(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas, yipranma_payi):
        super()._init_(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        if self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
            zam_orani = (self.get_maas() % self.get_tecrube()) / 2 + (self.get_yipranma_payi() * 10)
            self.set_yeni_maas(self.get_maas() + (zam_orani * self.get_maas() / 100))
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            zam_orani = (self.get_maas() % self.get_tecrube()) / 3 + (self.get_yipranma_payi() * 10)
            self.set_yeni_maas(self.get_maas() + (zam_orani * self.get_maas() / 100))
        else:
            zam_orani = (self.get_yipranma_payi() * 10)
            self.set_yeni_maas(self.get_maas() + (zam_orani * self.get_maas() / 100))

    def _str_(self):
        self.zam_hakki()
        return f"{super()._str_()}, Yıpranma Payı: {self.get_yipranma_payi()}"