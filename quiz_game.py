print("Welcome to the quiz game!!!")
proceed = input("Do you want to start? ")
if proceed.lower() != "yes":
    print("bye")
else:
    print("Let's start")
    score = 0
    answer = input("what is the full form of HTML? ")
    if answer.lower() == "hyper text markup language":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("what is the full form of CSS? ")
    if answer.lower() == "cascading style sheets":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("what is the full form of JS? ")
    if answer.lower() == "java script":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("what is the other name of JavaScript? ")
    if answer.lower() == "live script":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("HTML, CSS, JS includes in which course? ")
    if answer.lower() == "web development":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print("Your score is", score)
    print("You got", (score / 5) * 100, "% questions correct!")
    print("Quiz ended")
