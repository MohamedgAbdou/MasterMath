import random

while True:
    score = 0
    correct = 0
    operations = ['+','-','*','/']
    difficulty = input("Select difficulty level (easy, medium, hard): ")
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid input. Please enter either 'easy', 'medium', or 'hard'.")
        difficulty = input("Select difficulty level (easy, medium, hard): ")
    if difficulty == "easy":
        range_num = 10
    elif difficulty == "medium":
        range_num = 50
    else:
        range_num = 100

    while correct < 10:
        num1 = random.randint(0,range_num)
        num2 = random.randint(0,range_num)
        operation = random.choice(operations)
        if operation == '/':
            if num2 == 0:
                num2 = 1
        question = 'What is {} {} {}?'.format(num1, operation, num2)
        answer = input(question)
        try:
            if answer == "exit":
                exit()
            elif answer == "reset":
                print("The game is restarting...")
                break
            answer = int(answer)
            if operation == '+':
                correct_answer = num1 + num2
            elif operation == '-':
                correct_answer = num1 - num2
            elif operation == '*':
                correct_answer = num1 * num2
            elif operation == '/':
                correct_answer = num1 // num2
            if answer == correct_answer:
                print("Correct!")
                score += 1
                correct += 1
            else:
                print("Incorrect.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
        print("Current score: {}".format(score))

    print("You have completed the game with score {}".format(score))
