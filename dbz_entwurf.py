import numpy as np

    
    
def break_into_prime(number):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 23]
    denominator = []
    if number == 0:
        return number
    index = 0
    while True:
        try:
            i = prime_numbers[index]
            if (number % i) == 0:
                denominator.append(i)
                number = number // i
            else:
                index += 1
        except IndexError:
            return number, denominator


def get_feldspektrum():
    g = np.array([0])
    for i in range(1, int(nenner_q)+1):
        g = np.append(g, -i)
        g = np.append(g, i)
        v_strich = p * (1 + 6 * g / nenner_q)
    result = v_strich[0]
    result = np.append(result, v_strich[-2:])
    return result, v_strich


p2 = 44
m = 3
moegliche_ausf = []
for i in range(2, p2+1):
    if (p2 % i) == 0:
        moegliche_ausf.append(i)
ausf = moegliche_ausf[0]
nenner_q = p2 / ausf
q = (2 * p2 + ausf) / p2
N = p2 * m * q
p = p2 / 2
den_N = break_into_prime(N)[1]
den_p = break_into_prime(p)[1]
t = list(set(den_N).intersection(den_p))[0]
N_strich = N / t
urwicklung = p2 / t
if (N % 2) == 0:
    a = 2 * t
    q_stern = N_strich / (2 * m)
else:
    a = t
    q_stern = N_strich / m

feldspektrum, v = get_feldspektrum()

print(f"nenner_q is {nenner_q}")
print(f"v ist {v}")
print(f"feldspektrum ist {feldspektrum}")
