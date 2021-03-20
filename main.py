from random import randrange
import time

HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
game_continue = True
strikes = 0
global guess, progress, word


# Main Menu
def main_menu():
    print('Welcome to......\n--H-A-N-G-M-A-N--' + HANGMANPICS[0])
    loop_menu = True
    # Loop through main menu to get game mode (1 or 2)
    while loop_menu:
        mode = str(input('One Player or Two Player?\n'))
        if mode.lower() == ('1' or 'one'):
            return 1
        elif mode.lower() == ('2' or 'two'):
            return 2
        else:
            print('Invalid Input!')
            continue


# Game Loop
def game_loop(mode):
    print('H A N G M A N')
    global guess, progress, word
    if mode == 1:
        # Word creation
        word = list(random_word())
        progress = list('_' * len(word))
        while game_continue:
            print('S-I-N-G-L-E--P-L-A-Y-E-R\n' + HANGMANPICS[strikes] + '\n')
            print(progress)
            print(word)
            # Capture user guess

            guess = list(input('Take a Guess:\n'))
            # Check if game over or if guessed correctly
            if (strikes != 6) and (guess in word):
                progress = check_progress()
            print(progress)
    else:
        # Word and progress creation and convert to list
        word = str(input('Player 1, please enter your word:\n'))
        word = list(word)
        progress = list('_' * len(word))
        progress_banner = 'P-R-O-G-R-E-S-S:\n'
        print('\n' * 3)
        print('M-U-L-T-I--P-L-A-Y-E-R' + HANGMANPICS[strikes] + '\n'
              + progress_banner + str(progress))


# Return random word in a list
def random_word():
    # get data from .txt file formatted in "str, str"
    word_string = open("list_v2.txt").readlines()
    # data in list
    word_list = word_string[0].split(", ")
    return word_list[randrange(len(word_list))]


# Check guess and return updated progress
def check_progress():
    global guess, progress, word
    # Check letter in word and if correct replace and loop
    word = list(word)
    progress = list(progress)
    print(guess, word, progress)
    # Check each letter for correct guess and change if true
    while strikes < 6:
        for letter in word:
            # Compare letters and loop word
            if (guess not in word) and strikes < 6:
                wrong_guess()
            elif guess == letter:
                # Add correct letter to progress
                correct_guess()
    return end_game()


# End Game with Win
def win_game():
    print('--C-O-N-G-R-A-T-U-L-A-T-I-O-N-S--' + HANGMANPICS[strikes] + '\nYou won with %d guesses left!' % (
                6 - strikes))
    return exit(-1)


# End Game Message
def end_game():
    print(HANGMANPICS[6] + '\n--G-A-M-E--O-V-E-R--')
    time.sleep(2)
    print(('\n' * 3) + '--R-E-S-U-L-T-S--\nYou have %s letters remaining' % progress.count('_'))


# Return new guess
def wrong_guess():
    global guess, progress
    increment()
    print('Wrong!' + HANGMANPICS[strikes] + '\n' + str(progress))
    guess = input('Try Again:\n')
    return check_progress()


# Replace Letters in progress
def correct_guess():
    global progress, guess, word
    count = 0
    for letters in word:
        if guess == letters:
            progress = list(progress)
            progress[count] = letters
        count += 1
        if str(progress) == str(word):
            return win_game()
    guess = input('Correct!' + HANGMANPICS[strikes] + '\n' + str(progress) + '\nPlease enter another guess: \n')
    return check_progress()


# Increment Strikes
def increment():
    global strikes
    strikes += 1
    return strikes


guess = 's'
progress = '___________'
word = 'mississippi'
print(check_progress())
