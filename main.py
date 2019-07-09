from typing import List
import math


def win(board: List[int], size: int) -> int:

    # Denna funktion blir extremt användbar då jag kan använda den för kolla om en viss stegning på brädet ger vinst
    def search_line(first, steps, jump, b):
        last = first + steps * jump
        for i in range(first, last, jump):
            if b[first] == 0 or b[i] != b[i + jump]:
                return 0
        return b[first]


    # Kollar vertikalt
    for col in range(0, size):
        res = search_line(col, size - 1, size,  board)
        if res:
            return res

    # Kollar horisontalt
    for row in range(0, size ** 2, size):
        res = search_line(row, size - 1, 1, board)
        if res:
            return res

    # Kollar diagonal 1
    res = search_line(0, size - 1, size + 1, board)
    if res:
        return res

    # Kollar diagonal 2
    return search_line(size - 1, size - 1, size - 1, board)
    # Haha kanske borde infört en ny variabel med värdet (size - 1) typ "max"
    # Returnerar 0 om ingen vinner
    # Eftersom att dia 2 är det sista jag kollar kan jag returnera dess resultat som det slutgiltiga


if __name__ == '__main__':
    b = [-1, -1, 1,
         1, 1, 1,
         1, 1, -1]

    print(win(b, int(math.sqrt(len(b)))))
