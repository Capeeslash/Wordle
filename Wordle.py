import random

def start_game():
    print("Welcome to Wordle!")
    print("Your aim is to guess the 5 letter word within 6 tries")
    print("If you guess the correct letter in the correct position it will display +")
    print("If you guess the correct letter in the wrong position it will display ?")
    print("If you guess the wrong letter in the wrong position it will display -")
    print("\nGood luck!\n")

def get_target_word(file_path='target_words.txt'):
    with open('target_words.txt') as f:
        words = f.readlines()
    return random.choice(words).strip()

def get_valid_word(file_path='all_words.txt'):
    with open('all_words.txt') as f:
        words = f.readlines()
    valid_words = [word.strip() for word in words]
    return valid_words

def ask_for_guess(valid_words_list):
    while True:
        guess = input("Enter guess: ").lower()
        if guess in valid_words_list:
            return guess
        else:
            print("Invalid word!")
            continue

def is_correct(score):
    if score == ['2', '2', '2', '2', '2']:
        return True
    else:
        return False

def score_guess(guess_word, target_word):
    target_counts = {}
    guess_score = []

    for i, letter in enumerate(target_word):
        if letter in target_counts:
            target_counts[letter].append(i)
        else:
            target_counts[letter] = [i]

    for i in range(len(guess_word)):
        if guess_word[i] == target_word[i]:
            guess_score.append('2')
            if target_counts[guess_word[i]]:
                target_counts[guess_word[i]].pop(0)
        elif guess_word[i] in target_counts and target_counts[guess_word[i]]:
            guess_score.append('1')
            target_counts[guess_word[i]].pop(0)
        else:
            guess_score.append('0')
    return guess_score


def format_score(score):
    score1 = [str(s) for s in score]
    score2 = "".join(score1)
    score3 = score2.replace('2', '+')
    score4 = score3.replace('1', '?')
    final_score = score4.replace('0', '-')
    return final_score

valid_word_list = get_valid_word()


max_attempts = 6
attempt = 0
again = True
total_attempts = 0
successful_guess = 0
while again:
    start_game()
    target = get_target_word()
    attempt = 0
    while attempt < max_attempts:
        print("You have", max_attempts - attempt, "guesses left")
        guess = ask_for_guess(valid_word_list)
        score = score_guess(guess, target)
        final_score = format_score(score)
        if is_correct(score):
            successful_guess += 1
            total_attempts += attempt + 1
            average_attempts = total_attempts/successful_guess
            s_average_attempts = str(average_attempts)
            print("Congratulations, you've guessed the word!")
            print("Average number of tries: " + s_average_attempts)
            break
        else:
            print(guess.upper())
            print(final_score)
            attempt += 1
        if attempt == max_attempts:
            print("You ran out of guesses! The correct word was:", target)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        again = True
        continue
    else:
        break
