#深拷贝
import copy


a = [1,2,3,4,5]
b = copy.copy(a)
print(b)
a[2] = 10
print(a)
print(b)
c = copy.deepcopy(a)
a[1] = 21
print(c)