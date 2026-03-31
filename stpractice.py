"""Ascending order sorting"""
# nums=[2,8,3,5,7,9]
# res=sorted(nums)
# print(res)

"""Desscending order sorting"""
# nums=[2,8,3,5,7,9]
# res=sorted(nums,reverse=True)
# print(res)

"""string sorting"""
# s="deepsea"
# res=sorted(s)
# print(res)
"""if u want to join the sorted list"""
# j=" ".join(res)
# print(j)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations")





