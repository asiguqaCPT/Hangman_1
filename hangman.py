#TIP: use random.randint to get a random word from the list
import random

def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    words = open(file_name,'r')
    lines = words.readlines()
    return lines


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    r_word_pos = random.randint(0,len(words)-1)
    r_word = words[r_word_pos]
    letter_pos = random.randint(0,len(r_word)-1)
    letter = r_word[letter_pos]
    word_prompt = r_word[:letter_pos] + '_' + r_word[letter_pos+1:]
    print("Guess the word:",word_prompt)
    return r_word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    guess = input("Guess the missing letter: ")
    return guess


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

