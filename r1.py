from singleton.the_new_method import Foo, Boo
i = Foo(0, 2)
j = Foo(2, 4)
h = Foo(4, 8)


k = Boo(4,5)
l = Boo(6,7)
m = Boo(6,7)

print(i, i.bar())
print(j, j.bar())
print(h, h.bar())

print(k, k.bar())
print(l, l.bar())
print(m, m.bar())