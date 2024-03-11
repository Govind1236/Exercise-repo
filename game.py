import random
# 0 for snake 1 for water and 2 for gun
def check(computer, user):
    if(computer == user):
        return 0
    if(computer == 0 and user == 1):
        return -1
    if(computer == 1 and user == 2):
        return -1
    if(computer == 2 and user == 0):
        return -1
    return 1
computer = random.randint(0, 2)
user = int(input("0 for snake 1 for water and 2 for gun: "))
print("User:",user)
print("Computer:",computer)

score = check(computer , user)
if(score == 0):
    print("Its draw:")
elif(score == -1):
    print("You lose:")
else:
    print("You Won")
if score == 1:
  score += 1
print("your score is",score)
