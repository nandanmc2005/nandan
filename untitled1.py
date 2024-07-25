List = []
for i in range(1, 10):
    List.append(i)

print("List after Addition of elements from 1-10:")
print(List)

List.extend([11, 12, 13])
print("List after extending with [11, 12, 13]:")
print(List)

List.insert(14, 25)  # Insert 25 at index 14 (which is beyond the current length of the list)
print("List after inserting 25 at index 14:")
print(List)

List.remove(4)  # Remove the first occurrence of 4 from the list
print("List after removing the first occurrence of 4:")
print(List)

List.pop(4)  # Remove the element at index 4
print("List after popping the element at index 4:")
print(List)

print("List in reverse:")
print(List[::-1])  # Print the list in reverse order

print("List after Repetition (* 2):")
print(List * 2)  # Print the list repeated twice

print("List after Concatenation with [11, 12, 13]:")
print(List + [11, 12, 13])  # Concatenate the list with [11, 12, 13]

print("List membership operator (10 in List):")
print(10 in List)  # Check if 10 is in the list
print("List membership operator (6 in List):")
print(6 in List)  # Check if 6 is in the list

print("The length of the list:", len(List))  # Print the length of the list
