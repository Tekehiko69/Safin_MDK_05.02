def moveTower(from_pole, to_pole, other_pole, n):
    if n == 0:
        return
    moveTower(from_pole, other_pole, to_pole, n-1)
    print('Move disk from:', from_pole, 'put disk to:', to_pole)
    moveTower(other_pole, to_pole, from_pole, n-1)


n = int(input())
moveTower('A', 'B', 'C', n)