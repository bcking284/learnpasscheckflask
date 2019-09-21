import re
def length_check(password):
    if (len(password)<8):
        return 'Password is shorter than 8 characters'
    else:
        return 'Password meets character requirement'

def caps_check(password):
    if not re.search("[A-Z]", password):
        return 'Password must contain at least one capital letter'
    else:
        return 'Password contains at least one capital letter'

def num_check(password):
    if not re.search("[0-9]", password):
        return 'Password must contain a number'
    else:
        return 'Password contains a number'


# elif not re.search("[a-z]", password):
#     flag = -1
#     break
# elif not re.search("[A-Z]", password):
#     flag = -1
#     break
# elif not re.search("[0-9]", password):
#     flag = -1
#     break
# else:
#     flag = 0
#     return 'Valid'
#     break
