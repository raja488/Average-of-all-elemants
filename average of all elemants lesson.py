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

#code to find the item in a list 
print(len(nested_list))


# write a code to join 2 lists
l1=[12,3,34,3,5,23,13,3]
l2=[123,34,23,32,3,23,4,2,34,3]
l3=l1+l2
print(l3)
l3.sort()
print(l3)
#3d dimensial
d3list=[[[1,2,3,4,5],[6,7,8,9],[10,11,12,13]]],[[[14,15,16,17,18,19],[20,21,22],[23,24,25]]],[[[26,27,28,29,30],[31,32,33,34],[35,36,37]]]
d4list=[[[100,23,42,32],[1,2,3,4],[1,2,3,4,5]]],[[[1,2,3,4,5,6],[1,2,3,4,5],[1,2,3,4]]],[[[1,2,3,4,5,6],[1,2,3,4,5],[1,2,3,4,5]]]
d6list=d3list+d4list
print(d6list)
print(d3list[1] [0] [0] [1])
print(d3list[1] [0] [2] [2])
print(d3list[2] [0] [0])


animals=["lion","tiger","zebra","girrafe","penguin","cat"]
#write a code to create a list which contains all the item which contain the letter e 
newlist=[ x for x in animals if "e" in x]
print(newlist)
