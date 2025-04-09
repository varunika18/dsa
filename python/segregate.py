#segregate the given list as even elements first in descending order and then odd elements next in ascending order
l = [5,3,2,4,6,7]
even = [x for x in l if x % 2 == 0]
odd = [x for x in l if x % 2 != 0]
even.sort(reverse=True)
odd.sort()
result = even + odd
print(result)
