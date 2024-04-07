import random

def generate_string(target_sum):
    result = ''
    while target_sum >= 32:  # Only continue the loop if target_sum is 32 or greater
        # ASCII range for printable characters is 32-126
        new_char_val = random.randint(32, min(target_sum, 126))
        result += chr(new_char_val)
        target_sum -= new_char_val
    if target_sum > 0:  # If there's a remaining sum less than 32, add it to the result
        result += chr(target_sum)
    return result


# Generate a string
generated_strings = set()
for _ in range(100):
    new_string = generate_string(1337)
    if new_string not in generated_strings and new_string.strip() != '':
        # Check that the sum of the ASCII values is exactly 1337
        if sum(ord(c) for c in new_string) == 1337:
            print(new_string)
            generated_strings.add(new_string)