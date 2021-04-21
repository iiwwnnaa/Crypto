# Caesar cipher
import string

key = int(input("Key : "))
val = list(input("Value : "))
res = []

alpha = list(string.ascii_uppercase)
lth = len(alpha)

if int(input("Enc 0 / Dec 1 : ")):
    for i in val:
        cur = alpha.index(i) - key
        res.append(alpha[cur*-1]) if cur > lth else res.append(alpha[cur])
else:
    for i in val:
        cur = alpha.index(i) + key
        res.append(alpha[cur % lth]) if cur > lth else res.append(alpha[cur])

print("Result :",''.join(res))