import math

a = lambda x: x**2

b = lambda x, y: math.sqrt(x**2 + y**2)

c = lambda *args: sum(args)/len(args)

d = lambda s: "".join(set(s))

print(f"Hasil fungsi a (kuadrat dari 5): {a(5)}")
print(f"Hasil fungsi b (akar kuadrat dari 3^2 + 4^2): {b(3, 4)}")
print(f"Hasil fungsi c (rata-rata dari 1, 2, 3, 4, 5): {c(1, 2, 3, 4, 5)}")
print(f"Hasil fungsi d (unik karakter dari 'hello'): {d('hello')}")