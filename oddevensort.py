def custom_sort(input_str):
    length = len(input_str)
    previous_str = input_str

    for step in range(length * 2):
        even_part = []
        odd_part = []

        # Separate into even and odd indexed parts
        for i in range(length):
            if i % 2 == 0:
                even_part.append(input_str[i])
            else:
                odd_part.append(input_str[i])

        # Sort the even and odd parts
        even_part.sort()
        odd_part.sort()

        # Combine the parts based on the first character comparison
        even_first = even_part[0] <= odd_part[0]

        new_str = []
        even_idx = 0
        odd_idx = 0

        for i in range(length):
            if (i % 2 == 0 and even_first) or (i % 2 != 0 and not even_first):
                new_str.append(even_part[even_idx])
                even_idx += 1
            else:
                new_str.append(odd_part[odd_idx])
                odd_idx += 1

        new_str = ''.join(new_str)

        # Display the string after this iteration
        print(f"Iteration {step + 1}: {new_str}")

        # If no changes occur, exit early
        if new_str == previous_str:
            break

        # Prepare for the next iteration
        previous_str = new_str
        input_str = new_str

# Example usage
input_str = "YASH"
custom_sort(input_str)