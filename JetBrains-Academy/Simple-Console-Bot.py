def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    for n in range(num +1):
        print(f"{n}!")


def test():
    print("Let's test your programming knowledge.")
    print("What is PEP8?")
    print("1. Post-Exposure Prophylaxis")
    print("2. Noun")
    print("3. Programming function")
    print("4. Set of programming style rules")
    answer = input()
    if answer == 4:
        print('Completed, have a nice day!')
    else:
        print("Please, try again.")


def end():
    print('Congratulations, have a nice day!')


greet('Simplyy', '2022')
remind_name()
guess_age()
count()
test()
end()
