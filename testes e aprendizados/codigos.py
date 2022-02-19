def fatorial (x):
    fat = 1
    fatinho = x
    while fatinho > 1:
        fatinho-=1
        fat = fat * fatinho

    return fat

print(fatorial(5))