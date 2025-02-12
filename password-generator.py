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
def replaceLetters(word):
    word = word[0].upper() + word[1:]
    if "a" in word:
        word = word.replace("a", "@")
    if "t" in word:
        word = word.replace("t", "+")
    if "e" in word:
        word = word.replace("e", "3")
    if "i" in word:
        word = word.replace("i", "!")    
    return word
    


def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    word1 = replaceLetters(word1)
    word2 = replaceLetters(word2)
    password = word1 + word2
    return password


print(generate_weaker_password()) 