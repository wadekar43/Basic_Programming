number = 43
guess = int(input("Enter an Integer:"))

if guess == number:
    print('Congratulations, you did it.')
elif(guess < number):
    print('Number is little higher')
else:
    print('number is too small')

print("Done")