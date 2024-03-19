# Tyler Dionne
# Bi-Color Towers of Hanoi

import sys
import math
def tower(n):
    moves = []
    def hanoi(n, src, dest, temp, moves):
        if n == 0:
            return
        hanoi(n-1, src, temp, dest, moves)
        if n % 2 == 0:
            x = int(n/2)
            moves.append(f"Move Blue Disc {x} from Peg {src} to Peg {dest}")
        else:
            x = int(math.ceil(n/2))
            moves.append(f"Move Red Disc {x} from Peg {src} to Peg {dest}")
        hanoi(n-1, temp, dest, src, moves)

    def bicolor(n, src, dest, temp, moves, count, numnotsorted):
        if n == 0:
            return
        else:
            # want to move all but the n item to the temp (normal hanoi on (n-1))
            # want to move the n item to the dest 
            # for next call (n-1) want (new src = old temp) (new dest = old src) (new temp = old dest)
            hanoi(n-1, src, temp, dest, moves)
            numnotsorted -= 1

            if numnotsorted == 1:
                return

            if count % 2 == 0:
                x = int(n/2)
                moves.append(f"Move Blue Disc {x} from Peg {src} to Peg {dest}")
            else:
                x = int(math.ceil(n/2))
                moves.append(f"Move Red Disc {x} from Peg {src} to Peg {dest}")

            bicolor(n-1, temp, src, dest, moves, count+1, numnotsorted)

    bicolor(n, 1, 2, 3, moves, 0, n)

    return moves

def main():
    towersin = sys.argv[1]
    towersout = sys.argv[2]
    with open(towersin, 'r') as file:
        for line in file:
            n = line.strip()
            n = int(n)
    orign = n
    # n pairs of disks so 2n discs total
    n = n * 2 
    moves = tower(n)

    with open(towersout, 'w') as outfile:
        moves = tower(n)
        outfile.write(f"{orign}\n")
        for move in moves:
            outfile.write(f"{move}\n")

main()

# make run-two-towers input='towers.in1' output='towers.out1'








