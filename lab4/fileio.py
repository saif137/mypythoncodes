a = "a"
b = "b"
c = "c"

print(a < b)
print(a == b)
print(a > b)
if cmp(a, b) < 1 :
    print "test"
else:
    print "none"
print(cmp(b, a))