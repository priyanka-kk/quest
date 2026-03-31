# vegetables=['tomato','carrot','beetroot']
# print(vegetables)
# print(vegetables[0])
# print(vegetables[1])


# sample_list=[1,2,3,'Quest',10.25,[7,8,9,10],True,None]
# print(type(sample_list))
# print(sample_list)
# print(sample_list[5][1]) #gives the element 8 in list
# print(len(sample_list))

# sample_list2=list(1,2,3)
# print(type(sample_list2))

# sample_list2=list[(1,2,3)]
# print(type(sample_list2))
# print(sample_list2)
# # print(len(sample_list2))
# print(sample_list2([5]))

# path = "C:/Users/Documents/report.pdf"
# extension = path.rsplit(".", 1)[1]
# print(extension)

# path = "C:/Users/Documents/report.pdf"
# extension = path.split('/')
# # res=extension[3].split('.')[1]
# res=extension[3].removeprefix('report.')
# print(res)

"""operators"""
# numbers=[1,2,3,4,5,6,7,8,9]
# sample_list=[10,20,30,40,50]
# updated_list=numbers+sample_list #concatenation
# print(updated_list)
# numbers+=10
# print(numbers)

# numbers *=2
# print(numbers)

# numbers=[1,2,3,4,5,6,7,8,9,[10,20,30]]
# print(30 in numbers[9])
# print(len(numbers[-1]))
# print(numbers[7])
# print(numbers[8])
# print(numbers[10])
# print(numbers[-5])
# print(numbers[-1][-1])

# numbers=[1,2,3,4,5,6,7,8,9,[10,20,30],[100,200,300,[400,500,600],700,800,900]]
# print(numbers[-1][3][1])
# print(numbers[-1][5])

# numbers[3]=400
# # numbers[3]+=400
# numbers[3]*=400
# print(numbers)

"""list slicing"""
# numbers=[1,2,3,4,5,'quest','thejas','richu',6,7,8,9,[10,20,30]]
# print(numbers[6][1:4])

# matrix = [[0,1,2],[3,4,5],[6,7,8]]
# # print(matrix[0],matrix[1],matrix[2])
# for i in matrix:
#     for j in i:
#         # print(i)
#       print(j, end=" ")
#     print()

# matrices = [[0,1,2],[3,4,5],[6,7,8]]
# for matrix in matrices:
#     for m in matrix:
#         print(m,end=" ")
#     print()
