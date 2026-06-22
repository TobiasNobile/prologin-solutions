from typing import List
import operator

def engrenages(n: int, l: List[int]) -> None:
    """
    :param n: nombre d'engrenages
    :param l: liste des engrenages, représentés par leur nombre de dents
    """
    # TODO Afficher sur une ligne, et séparés par des espaces, les engrenages
    # par leur nombre de dents dans l'ordre qui permet de maximiser la vitesse
    # du dernier engrenage.
    restant = l.copy()
    final_order = []
    total = 0
    
    for i in range(n):
        possibilities = {} # indice de de l'élement:total
        
        for element in restant:
            possibilities[l.index(element)] = total + element
        
        total = max(possibilities.values())
        indice_kept = max(possibilities, key=possibilities.get)
        restant.remove(l[indice_kept])
        final_order.append(l[indice_kept])
    
    print(" ".join(list(map(str, final_order))))


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    engrenages(n, l)