from typing import List


def distance_parcourue(n: int, x: int, route: List[int]) -> None:
    """
    :param n: le nombre de portions de la route
    :param x: la puissance de l'engin
    :param route: le volume de déblais sur chaque portion de la route
    """
    total_gravas = 0
    if x == 0 and route[0] != 0:
        print(0)
        return
    
    for i in range(len(route)):
        total_gravas += route[i]
        if total_gravas < 0 or total_gravas > x:
            print(i)
            return
    print(i+1)


if __name__ == "__main__":
    n = int(input())
    x = int(input())
    route = list(map(int, input().split()))
    distance_parcourue(n, x, route)
