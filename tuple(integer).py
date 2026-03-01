# Ask the user to enter integers separated by spaces
user_input = input("Enter a series of integers separated by spaces: ")

# Convert the input string into a tuple of integers
numbers = tuple(map(int, user_input.split()))

# a) Print total number of items
print("Total number of items:", len(numbers))

# b) Print the last item
if len(numbers) > 0:
    print("Last item:", numbers[-1])
else:
    print("Tuple is empty.")

# c) Print elements in reverse order
print("Tuple in reverse order:", numbers[::-1])

# d) Check if 5 is in the tuple
if 5 in numbers:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining, and print result
if len(numbers) > 2:
    modified = numbers[1:-1]      # Remove first and last
    sorted_modified = tuple(sorted(modified))
    print("Sorted tuple after removing first and last items:", sorted_modified)
else:
    print("Not enough elements to remove first and last items.")