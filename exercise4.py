name = input("Enter a name: ")
new = name.split(" ")
code = input("Do you want to code or decode? press 0 for code and 1 for decode: ")
code = True if (code == "0") else False
new1 = []
if(code):
 for letter in new:
  if len(letter) >= 3:
    rand = "ada"
    rand1 = "qrw"
    user_input = rand + letter[1:] + letter[0] + rand1
    new1.append(user_input)
 else:
  new1.append(user_input[::-1])
else:
  for letter in new:
    if len(letter) >= 3:
      user_input = letter[3:-3] 
      user_input = letter[-1] + letter[1:-1] + letter[0]
      new1.append(user_input)
    else:
      new1.append(user_input[::-1])
print("".join(new1))