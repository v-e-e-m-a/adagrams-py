from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def create_pool_list():
    pool_list = []
    for letter, number_of_tiles in LETTER_POOL.items():
        for index in range(0, number_of_tiles):
            pool_list.append(letter)
    return pool_list


def draw_letters():
    pool_list = create_pool_list()
    print(f'Letter pool: {pool_list}')
    hand = []
    letter_freq = {}
    draw = True
    while draw:
        letter_index = randint(0, len(pool_list)-1) #Assigns the index of the letter based on random integer
        letter = pool_list[letter_index] #Accesses the letter at index

        if letter in letter_freq and letter_freq[letter] == LETTER_POOL[letter]:
            continue
        elif letter in letter_freq and letter_freq[letter] < LETTER_POOL[letter]:
            letter_freq[letter] += 1
            hand.append(letter)
        else:
            letter_freq[letter] = 1
            hand.append(letter)
        
        #Returns the hand once it has 10 letters
        if len(hand) == 10:
            draw = False
            print(f'Hand:{hand}')
            return hand


def uses_available_letters(word, letter_bank):
    word_list = list(word.upper()) # Creates a list of all the letters within the word
    hand = letter_bank.copy() # Creates a copy of letter_bank so it does not get modified

    is_valid = False

    for letter in word_list:
        if letter in hand: # If the letter is in the hand
            is_valid = True #Then it is valid
            hand.remove(letter) #Remove the letter from our available letters to use
        else:
            is_valid = False
    
    return is_valid


def score_word(word):
    word_list = list(word.upper()) #Creates a list of the word's letters in uppercase
    score = 0

    ten_points = ['Q', 'Z']
    eight_points = ['J', 'X']
    five_points = ['K']
    four_points = ['F', 'H', 'V', 'W', 'Y']
    three_points = ['B', 'C', 'M', 'P']
    two_points = ['D',  'G']

    for letter in word_list:
        # Scores word by table given using lists (There has to be an easier way but this is all I can think of right now)
        if letter in ten_points:
            score += 10
        elif letter in eight_points:
            score += 8
        elif letter in five_points:
            score += 5
        elif letter in four_points:
            score += 4
        elif letter in three_points:
            score += 3
        elif letter in two_points:
            score += 2
        else:
            score += 1
        

        #Adds bonus 8 points if length of word is 7 or higher
    if len(word_list) >= 7:
        score += 8
    
    return score


def get_highest_word_score(word_list):
    highest_word = ''
    highest_score = 0

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_word = word
            highest_score = score
        elif score == highest_score:
            if (len(word) == len(highest_word)) or (len(highest_word) == 10):
                continue
            elif len(word) == 10:
                highest_word = word
            elif len(word) < len(highest_word):
                highest_word = word
    
    return highest_word, highest_score