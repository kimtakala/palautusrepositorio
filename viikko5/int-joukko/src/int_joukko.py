INITIAALIKAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=INITIAALIKAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")

        self.__kapasiteetti = kapasiteetti
        self.__kasvatuskoko = kasvatuskoko
        self.__ljono = self._luo_lista(self.__kapasiteetti)
        self.__alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.__ljono

    def __kasvata_kapasiteettia(self):
        self.__kapasiteetti += self.__kasvatuskoko
        self.__ljono.extend(self._luo_lista(self.__kasvatuskoko))

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.__ljono[self.__alkioiden_lkm] = n
            self.__alkioiden_lkm += 1

            if self.__alkioiden_lkm == self.__kapasiteetti:
                self.__kasvata_kapasiteettia()
            return True

        return False

    def poista(self, n):
        try:
            self.__ljono.remove(n)
            self.__ljono.append(0)
            self.__alkioiden_lkm -= 1
            return True
        except ValueError:
            return False

    def mahtavuus(self):
        return self.__alkioiden_lkm

    def to_int_list(self):
        return [int(self.__ljono[i]) for i in range(self.__alkioiden_lkm)]

    @staticmethod
    def __create_start_items(a: "IntJoukko", b: "IntJoukko") -> tuple:
        a = a.to_int_list()
        b = b.to_int_list()
        return (IntJoukko(len(a + b)), a, b)

    @staticmethod
    def yhdiste(a, b):
        x, a_taulu, b_taulu = IntJoukko.__create_start_items(a, b)

        for item in a_taulu:
            x.lisaa(item)

        for item in b_taulu:
            x.lisaa(item)

        return x

    @staticmethod
    def leikkaus(a, b):
        x, a_taulu, b_taulu = IntJoukko.__create_start_items(a, b)

        for item_a in a_taulu:
            for item_b in b_taulu:
                if item_a == item_b:
                    x.lisaa(item_a)
                    break

        return x

    @staticmethod
    def erotus(a, b):
        x, a_taulu, b_taulu = IntJoukko.__create_start_items(a, b)

        for item in a_taulu:
            x.lisaa(item)

        for item in b_taulu:
            x.poista(item)

        return x

    def __str__(self):
        tuotos = ", ".join(map(str, self.__ljono[:self.__alkioiden_lkm]))
        return f"{{{tuotos}}}"
