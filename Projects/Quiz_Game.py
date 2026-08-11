print("Welcome to Quiz Game!")
Playing = input("Do you want to plan the Quiz Game:").lower()
if Playing != "yes":
    quit()
Score=0
Question=input("What is CPU stands for:")
if Question.lower()=="central processing unit":
    print("Correct!")
    Score+=1
else:
    print("Incorrect!")

Question=input("What is Ram stands for:")
if Question.lower()=="randam access memory":
    print("Correct!")
    Score+=1
else:
    print("Incorrect!")

Question=input("What is ROM stands for:")
if Question.lower()=="read only memory":
    print("Correct!")
    Score+=1
else:
    print("Incorrect!")

Question=input("What is URL stands for:")
if Question.lower()=="uniform resource locater":
    print("Correct!")
    Score+=1
else:
    print("Incorrect!")

print(f"You have answered {Score} questions")
print(f"You got {Score/4*100} %")