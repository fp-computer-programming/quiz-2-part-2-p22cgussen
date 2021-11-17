# Author CCG 11/17/21

sentence = input("Enter a statement: ")
lower_sentence = sentence.lower()

if lower_sentence == "not":
    print(sentence)
elif lower_sentence[0:3] == "not":
    print(sentence)
else:
    print("You're not " + sentence + ". Now SCRAM!")
