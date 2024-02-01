import random
import string


def change_to_upper(string):
    converted_string = ""
    for char in string:
        if char.islower():
            char = char.upper()
        converted_string += char
    return converted_string
    
    
def gen_market_id(length):
    characters = string.ascii_uppercase + string.digits
    certificate_id = ''.join(random.choice(characters) for _ in range(length))
    return certificate_id

# Example usage: generate a certificate ID with a length of 10 characters
name = input('Enter the first name of the candidate : ')
last_name = input('Enter the last name of the candidate : ')

fname = change_to_upper(name)
lname = change_to_upper(last_name)
    
candidate_id = input('Enter candidate ID: '  )

name_chars = fname[:2] + lname[:2]

market_id = gen_market_id(6)

new_id = 'XBL' + name_chars + candidate_id
print(new_id)


