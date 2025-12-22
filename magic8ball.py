import random
#a list of possible answers
answer = ["Yes - definitely", "It is decidedly so", "Without a doubt", "Reply hazy, try again", "Ask again later", "My sources say no", "Outlook not so good", "Very doubtful"]
#ask the user for their name
name = input("What is your name? ")
print(f"\nHello, {name}. ")

while True:
    def game():
        print("Let's play!")
        #have the user type a question
        question = input("\nWhat would you like to ask? ")
        #prints the user input as well as the randomly generated answer
        print(f"\nYou asked: {question}")
        print("---------------------------------------------------")
        print(f"\nMagic 8-Ball's answer: {random.choice(answer)}")

        again = input("\nWould you like to try again? Press 1. for Yes or 2. for No ")
        if again == "1":
            game()
        else:
            print("Thanks for playing!")
        return
    break

game()
      
            
