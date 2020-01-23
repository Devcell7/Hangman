import random
def secret_word():
    word=('cat','man','tank','help')
    hint=("animal","human","armour","feeling")
    no = random.randint(0, 3)
    print(hint[no])
    return word[no]

def ask_letter():
    l=input("Guess a Letter.").lower()
    return l

def check():
    count = 0
    Words = secret_word()
    words = list(Words)
    HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
       ===''']

    while count < 6:
        letter = ask_letter()
        
        if letter in words:
            words.remove(letter)
            if len(words)==0:
                count = 8
                print(f'YOU WORD IS {Words}')
            
        else:
            print('Enter Again')
            print()
            count = count+1
            print(HANGMAN_PICS[count])
    if count == 6:
        print('You lose')

check()