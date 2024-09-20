numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
j = 0
primes = []
not_primes = []
i = 0
for i in range(len(numbers)):
    is_prime = True
    j = numbers[i]
    if j < 2:
        continue
    else:
        f = j ** (1 / 2)
    for a in range(2, int(f + 1)):
        if j % a == 0:
            is_prime = False
            break
    if not (is_prime):
        not_primes.append(j)
    else:
        primes.append(j)
is_prime = True
print('Primes: ', primes)
print('Not primes: ', not_primes)
