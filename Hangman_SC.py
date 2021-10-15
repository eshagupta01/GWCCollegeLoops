#Hangman Starter Code

def print_list(log):
    for x in log:
        print(x, end = '\t')
    print()
    
if __name__ == "__main__":
    string = input("Enter a word to guess:")
    guess = input("Enter a character to guess: ")
    print("You lost, the word was : " + string)
    print("You won!")
