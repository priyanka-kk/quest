"""1. Write a lambda function to add two numbers."""
# add_twonos=lambda a,b:a+b
# print(add_twonos(4,7))

"""2. Write a lambda function to subtract two numbers."""
# sub_2nos=lambda a,b:a-b
# print(sub_2nos(10,4))

"""3. Write a lambda function to multiply two numbers."""
# mul_2nos=lambda a,b:a*b
# print(mul_2nos(10,4))

"""4. Write a lambda function to divide two numbers."""
# div_2nos = lambda a, b: a / b if b != 0 else "Cannot divide by zero"
# print(div_2nos(10, 2))

"""5. Write a lambda function to find the square of a number."""
# squ_no=lambda a:a**2
# print(squ_no(5))

"""6. Write a lambda function to find the cube of a number."""
# cube_no=lambda a:a**3
# print(cube_no(5))

"""7. Write a lambda function to find the remainder of two numbers."""
# rem_no = lambda a, b: a % b if b != 0 else "Cannot divide by zero"
# print(rem_no(10, 3))

"""8. Write a lambda function to calculate power (a^b)."""
# power_no=lambda a,b:a**b
# print(power_no(6,4))

"""9. Write a lambda function to check whether a number is even or odd."""
# even_odd=lambda x: "even" if x%2==0 else "odd"
# print(even_odd(7))

"""10. Write a lambda function to check whether a number is positive or negative."""
# pos_neg=lambda x: "positive" if x>0 else "negative"
# print(pos_neg(-7))

"""11. Write a lambda function to check whether a number is positive, negative, or zero."""
# pos_neg_zero=lambda x: "positive" if x>0 else ("negative" if x<0 else "zero")
# print(pos_neg_zero(7))

"""12. Write a lambda function to find the greater of two numbers."""
# great_two=lambda a,b:a if a>b else b
# print(great_two(4,14))

"""13. Write a lambda function to find the smaller of two numbers."""
# small_two=lambda a,b:a if a<b else b
# print(small_two(14,5))

"""14. Write a lambda function to find the maximum of three numbers."""
# max_3nos=lambda a,b,c:a if a>b and a>c else(b if b>a and b>c else c)
# print(max_3nos(94,108,78))

"""15. Write a lambda function to find the minimum of three numbers."""
# min_3nos=lambda a,b,c:a if a<b and a<c else(b if b<a and b<c else c)
# print(min_3nos(12,18,78))

"""16. Write a lambda function to check whether a number is divisible by 5."""
# div_5=lambda x:"divisible by 5" if x%5==0 else "not divisible by 5"
# print(div_5(15))

"""17. Write a lambda function to check whether a number is divisible by both 3 and 5."""
# div_5and3=lambda x:"divisible by 5 and 3" if x%5==0 and x%3==0 else "not divisible by 5 and 3"
# print(div_5and3(23))

"""18. Write a lambda function to find the last digit of a number."""
# last_digit=lambda x:x%10
# print(last_digit(4547))

"""19. Write a lambda function to remove the last digit of a number."""
# rem_last_digit=lambda x:x//10
# print(rem_last_digit(1247))

"""20. Write a lambda function to check whether a number is a multiple of 10."""
# mul_10=lambda x:" multiple of 10" if x%10==0 else " not  a multiple of 10"
# print(mul_10(40))

"""21. Write a lambda function to calculate simple interest."""
# simp_interst=lambda p,n,r:(p*n*r )/100
# print(simp_interst(1000,20,2))

"""22. Write a lambda function to calculate the area of a rectangle."""
# area_rect=lambda l,b:l*b
# print(area_rect(4,8))

"""23. Write a lambda function to calculate the area of a square."""
# area_square=lambda a:a**2
# print(area_square(4))

"""24. Write a lambda function to calculate the perimeter of a rectangle."""
# perimeter_rect=lambda l,b:2*(l+b)
# print(perimeter_rect(4,8))

"""25. Write a lambda function to calculate the area of a triangle."""
# area_triangle=lambda b,h:(b*h)/2
# print(area_triangle(4,8))

"""26. Write a lambda function to convert Celsius to Fahrenheit."""
# celto_far=lambda c:c*(9/5)+32
# print(celto_far(45))

"""27. Write a lambda function to convert Fahrenheit to Celsius."""
# faren_tocel=lambda f:(f-32)*(5/9)
# print(faren_tocel(95))

"""28. Write a lambda function to convert a string to uppercase."""
# str_toupper=lambda text:text.upper()
# print(str_toupper("python programmer"))

"""29. Write a lambda function to convert a string to lowercase."""
# str_tolower=lambda text:text.lower()
# print(str_tolower("PYTHON PROGRAMMER"))

"""30. Write a lambda function to find the length of a string."""
# str_length=lambda text:len(text)
# print(str_length("python programmer"))

"""31. Write a lambda function to get the first character of a string."""
# fchar_str=lambda text:text[0]
# print(fchar_str("onam"))

"""32. Write a lambda function to get the last character of a string."""
# lchar_str=lambda text:text[-1]
# print(lchar_str("onam"))

""""33. Write a lambda function to reverse a string."""
# rev_str=lambda text:text[::-1]
# print(rev_str("python"))

# """34. Write a lambda function to check whether a string is a palindrome."""
# pal_str=lambda text:"palindrome" if text[::-1]==text else "not palindrome"
# print(pal_str("malayalam"))

"""35. Write a lambda function to count vowels in a string."""
# count_vowels = lambda text: sum(1 for ch in text if ch in 'AEIOUaeiou')
# print(count_vowels("onam"))

"""36. Write a lambda function to check whether a string starts with 'A'."""
# strstart_A=lambda text:"string starts with A" if text.startswith("A")==True else "string not starts with A"
# print(strstart_A("Apple"))

"""37. Write a lambda function to calculate the average of three numbers."""
# avg_3nos=lambda a,b,c:(a+b+c)/3
# print(avg_3nos(4,8,12))

"""38. Write a lambda function to swap two numbers."""
# swap_2nos = lambda a, b: (b, a)
# print(swap_2nos(2, 3))

"""39. Write a lambda function to return the absolute value of a number."""
# abs_val = lambda x: x if x >= 0 else -x
# print(abs_val(-5))
# print(abs_val(7))

"""40. Write a lambda function to check whether a character is a vowel."""
# isa_vowel=lambda x:"vowel" if x in "AEIOUaeiou" else "not a vowel"
# print(isa_vowel('I'))

"""41. Write a lambda function to check whether a character is an alphabet."""
# is_alphabet=lambda x:"alphabet" if x.isalpha()==True else "not an alphabet"
# print(is_alphabet('a'))

"""42. Write a lambda function to check whether a character is a digit."""
# is_digit=lambda x:"digit" if x.isdigit()==True else "not a digit"
# print(is_digit('9'))

"""43. Write a lambda function to join two strings."""
# join_str=lambda text1,text2:text1+" "+text2
# print(join_str("Happy","Onam"))

"""44. Write a lambda function to repeat a string n times."""
# rep_string=lambda text,n:n*text
# print(rep_string("onam ",4))

"""45. Write a lambda function to calculate the discounted price."""
# dis_price=lambda price,dis:price-(price*dis)/100
# print(dis_price(1000,20))


