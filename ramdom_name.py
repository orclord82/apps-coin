import random
import string

def ran_name():
    char_set = string.ascii_lowercase + string.digits
    ranname = ''.join(random.sample(char_set*6, 6))
   
    return ranname