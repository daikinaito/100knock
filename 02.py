# coding: UTF-8
a = u"パトカー"
b = u"タクシー"
c = u""

# for i in range(len(a)):
#     c = c + a[i] + b[i]
for a,b in zip(a,b):
    c = c + a + b
# print(''.join([s1 + s2 for s1, s2 in zip(a, b)]))
print c