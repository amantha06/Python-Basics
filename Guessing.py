secret_word = "Girraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ") 
        guess_count += 1
    else:
        out_of_guesses = True


if guess == secret_word:
    print("You got the right word!")
if out_of_guesses:
    print("You ran out of tries :(( ")