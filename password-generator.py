import random 
import string
import requests

# function that genereates a single random character 
def random_character():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength = 12

# function that generates a password of random characters
input_p = input("how long does password need to be? ")
input_p = int(input_p)
def generate_strong_password():
    password = " "
    

passwordLength = input_p
print 

generate_strong_password()

def fetch_word():
    url = "https://random-word-api.herokuapp.com/word?length=6"
    
    response = requests.get(url)
    word = response.json()[0]
    return word

print(fetch_word()) 