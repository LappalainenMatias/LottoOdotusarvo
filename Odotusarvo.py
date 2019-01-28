import random
import timeit

minun_luvut = [1,2,5,8,18,32,33]

def lottoNumerot():
    """
    Tekee listan, joka sisältää kahdeksan numeroa.
    Mikään numero ei toistu kahdesti
    :return: lista joka sisältää kahdeksan numeroa (Int)
    """
    my_randoms = random.sample(range(1, 41), 8)
    return my_randoms

def voitto(lottonumerot):
    """
    :param lottonumerot: koneen arpomat 7 numeroa + lisänumero
    :return: Palauttaa tuloksen
    tulokset:
    3+1 = 2e
    4 = 10e
    5 = 50e
    6 = 2000e
    6+1 = 100 000e
    7 = 15 000 000e
    """
    osumien_maara = len(list(set(lottonumerot[0:7]).
                             intersection(minun_luvut)))

    if osumien_maara < 3:
        return

    if lottonumerot[7] in minun_luvut:
        tulos = str(osumien_maara) + " + 1"
    else:
        tulos = str(osumien_maara)

    if tulos == "3 + 1":
        return 2
    elif tulos == "4":
        return 10
    elif tulos == "5":
        return 50
    elif tulos == "6":
        return 2000
    elif tulos == "6 + 1":
        return 100000
    elif tulos == "7":
        return 15000000


def main():
    start = timeit.default_timer()
    rivienmaara = 1500
    lopputulos = -1*rivienmaara
    for i in range(0,rivienmaara):
        tulos = voitto(lottoNumerot())
        if tulos:
            lopputulos = lopputulos+tulos

    print(lopputulos)
    print(lopputulos/rivienmaara)

    stop = timeit.default_timer()
    print('Time: ', stop - start)


main()