def recept(antal):
    print("Ägg: ", round(3/4*antal), " st")
    print("Ströbröd: ", round(3/4*antal), " dl")
    print("Vaniljsocker ", round(1/2*antal), " tsk")
    print("Bakpulver: ", round(1/2*antal), " tsk")
    print("Vetemjöl: ", round(3/4*antal), " dl")
    print("Smör: ", round(75/4*antal), " g")
    print("Vatten: ", round(1/4*antal), " dl")


def tidblanda(antal):
    return 10 + antal


def tidgrädda(antal):
    return 30 + antal*3


def sockerkaka(antal):
    Totaltid = tidblanda(antal) + tidgrädda(antal)
    print("Sockerkaka för ", antal, " personer:")
    print()
    recept(antal)
    print()
    print("Tidsåtgång: ", Totaltid, " minuter")


sockerkaka(4)
sockerkaka(7)
