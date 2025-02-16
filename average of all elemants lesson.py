numbers=[2,34567,4,24,6,4,56,64,45,345]
# formula to calculate average = add all the numbers up/by how many numbers there are 
average=sum(numbers)/len(numbers)
print(average)

names=["UMAR", "RAJA", "SYED", "ISA", "ENGJULL", "MARK", "LEO", "ASAD", "ALI", "HARRY"]
print(",".join(sorted(names)))

names.sort()
print(names)

numbers.sort()
print(numbers)

all=numbers+names
print(all)

#list nesting 
nested_list=[ [1,2,3] , [4,5,6] , [7,8,9]]
print(nested_list[0])
# print the last item of your list 
print(nested_list[2])
# print the first number of the first item
print(nested_list[0] [0])

print(nested_list[1] [1])
print(nested_list[2] [2])
#print each item in your list
print("****************************************************************************")
print(nested_list[0] [0])
print(nested_list[0] [1])
print(nested_list[0] [2])
print(nested_list[1] [0])
print(nested_list[1] [1])
print(nested_list[1] [2])
print(nested_list[2] [0])
print(nested_list[2] [1])
print(nested_list[2] [2])

#print each items in the list using a loop 
print("************************************&********")
for sublist in nested_list:
    for item in sublist:
        print(item)
#print each item using a loop with the help of index 
print("*****************************************************&^&^(&)")
for sublistindex in range (len(nested_list)):
    for index in range (len(nested_list[sublistindex])):
        print(nested_list[sublistindex][index])
