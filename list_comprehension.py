
nums=[1,4,8]
new_list=[n+1 for n in nums]

print(new_list)


name = "Aditya"

char_list = [letter for letter in name]

print(char_list)


list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(string_) for string_ in list_of_strings]
result = [n for n in numbers if n%2==0]
print(result)