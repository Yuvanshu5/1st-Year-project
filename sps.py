import random

choices = ["stone", "paper", "scissor"]

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "stone" and computer == "scissor") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissor" and computer == "paper"):
        return "user"
    else:
        return "computer"

user_score = 0
computer_score = 0
rounds = 0

while True:
    user_choice = input("Enter your choice (stone/paper/scissor or quit): ").lower()
    if user_choice == "quit":
        print("\nGame Over!")
        print(f"Final Score => You: {user_score} | Computer: {computer_score}")
        if user_score > computer_score:
            print(" You are the Champion!")
        elif user_score < computer_score:
            print(" Computer wins the match!")
        else:
            print(" It's a draw overall!")
        break

    if user_choice not in choices:
        print("Invalid input. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)

    if result == "user":
        user_score += 1
        print(" You win this round!")
    elif result == "computer":
        computer_score += 1
        print(" Computer wins this round!")
    else:
        print(" It's a tie!")

    rounds += 1
    print(f"Score after {rounds} round(s) => You: {user_score} | Computer: {computer_score}")
    print("-" * 40)
