from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()
        
        while True:
            ekan_siirto = self._eka_siirto()
            tokan_siirto = self._toka_siirto(ekan_siirto)
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            if not self._onko_ok_siirrot(ekan_siirto, tokan_siirto):
                break

        print('Kiitos!')
        print(tuomari)


    def _eka_siirto(self):
        return input('Ensimmäisen pelaajan siirto: ')
    
    def _toka_siirto(self, eka_siirto):
        raise NotImplementedError("Needs to be defined in the child class")
    
    def _onko_ok_siirrot(self, *siirrot):
        ok_siirrot = ['k', 'p', 's']
        for siirto in siirrot:
            if siirto not in ok_siirrot:
                return False
        return True
    
    @staticmethod
    def luo_peli(pelityyppi):
        pelityypit = {
            "a" : KPSPelaajaVsPelaaja(),
            "b" : KPSTekoaly(),
            "c" : KPSParempiTekoaly()
        }
        return pelityypit.get(pelityyppi, None)

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toka_siirto(self, eka_siirto):
        return input("Toisen pelaajan siirto: ")

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toka_siirto(self, eka_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(eka_siirto)
        return tokan_siirto

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _toka_siirto(self, eka_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(eka_siirto)
        return tokan_siirto
