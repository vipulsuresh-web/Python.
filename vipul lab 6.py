'''#
#list task
students = ["Alice", "Charlie", "Nick", "Liam", "Ben"]
print("1.student list:", students)
#
students.append("Diana")
print("2.After append():",students)
#
students.insert(1,"Noah")
print("3.After insert():",students)
#
students.remove("Liam")
print("4.After removing():",students)
#
print("5.Length of the list:", len(students))
#
students.reverse()
print("6.reversing():",students)
#
numbers=[65,45,88,95,88,12,56,0,88,99]
print("8.The largest is", max(numbers))
#
print("9.occurence",numbers.count(88))'''
#



'''#tuple task
print("10. Original list:", students)
print("Copied list:", students.copy())
# 
numbers = (10, 25, 40, 25, 60)
print("1. Initial tuple:", numbers)
# 
tuple_length = len(numbers)
print("2. Length of the tuple:", tuple_length)
#
first_element = numbers[0]
last_element = numbers[-1]
print(f"3. First element: {first_element}, Last element: {last_element}")
#
count_25 = numbers.count(25)
print("4. Occurrence of '25':", count_25)
#
index_40 = numbers.index(40)
print("5. Index of '40':", index_40)
#
tuple2 = (70, 85)
combined_tuple = numbers + tuple2
print("6. Concatenated tuple:", combined_tuple)
#
mixed_tuple = ("Python", 3.14, True, 42)
print("7. Mixed data types tuple:", mixed_tuple)
#
my_list = ["apple", "banana", "cherry"]
converted_tuple = tuple(my_list)
print("8. Converted list to tuple:", converted_tuple)
#
converted_list = list(numbers)
print("9. Converted tuple to list:", converted_list)
#
element_to_check = 40
exists = element_to_check in numbers
print(f"10. Does {element_to_check} exist in the tuple?: {exists}")'''



#Set Tasks
#
A={3,5,9,1,8}
B={2,5,6,7,1}
print(A)
#
A.add(12)
#
A.remove(5)
#
A.discard(1)
#
print(A.union(B))
#
print(A.intersection(B))
#
print(A.difference(B))
#
print(A.issubset(B))
#
print(A.issuperset(B))
#
print(A.clear)



#


#Combined Tasks
list = [10, 20, 30, 40, 50]
tuple = (10, 20, 30, 40, 50)
set = {10, 20, 30, 40, 50}
print("List :",list)
print("Tuple:",tuple)
print("Set  :",set)















































