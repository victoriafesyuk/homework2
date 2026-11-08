import string 
import random


password_length = len("viktoriia")
password = ''.join(random.choice(string.hexdigits + string.punctuation) for i in range(password_length)) 
print("Random password: ", password)
