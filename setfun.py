"""union"""
set1 = {1,2,3,4,5}
set2 ={4,5,7,8}
set3={4,5,7,8,9,22,33}
# print(set1.union(set2))
# print(set1.union(set2,set3))
# print(set1 | set2)

"""intersection"""
# print(set1.intersection(set2,set3))
# print(set1 & set2 & set3)

# who_knows_python={'najad','sahabin','yaseen','jasil'}
# who_knows_django={'richu','shahal','shony','priyanka','yaseen'}
# print(who_knows_python & who_knows_django)

"""intersectionupdate"""
# print(set1.intersection_update(set2)) #none
# print(set1)
# set1&=set2
# print(set1)

"""difference"""               
# a=set1-set2
# print(a)
# print(set1set2)
# print(set1.difference_update(set2)) #none

"""set comprehension"""
"""Cherck the numbers in the set are even or odd"""
numbers={2,1,5,7,8,9,6,3,4,7}
# even_or_odd={'even' if num%2==0 else 'odd' for num in numbers}
# print(even_or_odd)

"""if the numbers in the set is greter than 5 print one else zero """
# ab0ve_or_below5=['one' if num>5 else 'zero' for num in numbers]
# print(ab0ve_or_below5)


"""if the numbers in the set is greter than 5 print one else zero 
if the number is 5 print 5"""
for_zero = {"one" if x>5 else 0 if x<5 else 5 for x in numbers}
print(for_zero)





