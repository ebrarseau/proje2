from Calisan import Calisan
class BeyazYaka(Calisan):
    def _init_(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas,yeni_maas, tesvik_primi):
        super()._init_(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
    #super().zam_hakki()
        if self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
            zam_miktari = (self.get_maas() % self.get_tecrube()) * 5 + float(self.get_tesvik_primi())
            self.set_yeni_maas(self.get_maas() + zam_miktari)
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            zam_miktari = (self.get_maas() % self.get_tecrube()) * 4 + float(self.get_tesvik_primi())
            self.set_yeni_maas(self.get_maas() + zam_miktari)
        else:
            zam_miktari = float(self.get_tesvik_primi())
            self.set_yeni_maas(self.get_maas() + zam_miktari)

    def _str_(self):
        self.zam_hakki()
        return f"{super()._str_()}, Teşvik Prim: {self.get_tesvik_primi()}"