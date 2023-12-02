# Python>Strings>The Minion Game

#Given a string (s). Calculate de winner.

#--Game Rules--
# Both players are given the same string, s.
# Both players have to make substrings using the letters of the string s.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

#--Scoring--
# A player gets +1 point for each occurrence of the substring in the string s.

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

#Ex:
#Sample Input
# s = 'BANANA'

# (Stuart has 12 points and Kevin has 9 points)

#Sample Output:
# Stuart 12

# If both have the same score, print "Draw"


#Solution:-------------

#Check if a letter is a vowel
def is_vowels(letter):
    if ((letter=='A') or (letter=='E') or (letter=='I') or (letter=='O') or (letter=='U') ):
        return True
    else:
        return False

#Calculate score
def calculate_score(main_word, indexes):
    score = 0
    word_lengt = len(main_word)
    for index in indexes:
        # +1 point for each letter until the end
        score = score + (word_lengt-index)
        
    return score


def minion_game(string):

    word = string
    # Initialize indexes list
    vowels_indexes = []
    consonants_indexes = []
    # Initialize string position
    position = 0

    # Check the word letter by letter
    for letter in word:
        #Store vowel and consonants indexes
        if(is_vowels(letter)):
            vowels_indexes.append(position)
        else:
            consonants_indexes.append(position)
        position += 1

    # Calculate scores
    k_score = calculate_score(word, vowels_indexes)
    s_score = calculate_score(word, consonants_indexes)
    
    #Print results
    if (k_score > s_score):
        print(f"Kevin {k_score}")
    elif (k_score < s_score):
        print(f"Stuart {s_score}")
    else:
        print("Draw")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)