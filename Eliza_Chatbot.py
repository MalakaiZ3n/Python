# an ELIZA chatbot

# chatbot introduction
print("Hello. I'm Elizabeth, but you may call me Eliza. I'm a chatbot.")
print('I like to write my own narrative.')
name = input('What is your name?: ')
print('Hello', name, ', it is a pleasure to meet you.')

# get year information
year = input('I am not very good at dates. What year is this?: ')
print('What a wonderful year to be alive right now. Thanks!')

# ask user to guess age
myage = input('Do you think you can guess my age? - enter a number: ')
print("You are very observant. I am", myage,
      ",and I plan to be forever young.")

# do math to calculate when chatbot will be 100
myage = int(myage)
nyears = 100 - myage
print('I will be 100 in', nyears, 'years.')
print('That will be the year', int(year) + nyears)

# food conversation
print('I love chocolate and I also like trying out new kinds of food')
food = input('How about you? What is your favorite food?: ')
print('I like', food, 'too.')
question = 'How often do you eat ' + food + '?: '
howoften = input(question)
print('Interesting. I wonder if that is good for your health')

# animal conversation
animal = input('My favorite animal is a giraffe. What is yours?: ')
print(animal, "?! I don't like them.")
print('I wonder if a', animal, 'likes to eat', food, '?')

# conversation about feelings
feeling = input('How are you feeling today?: ')
print('Why are you feeling', feeling, 'now?')
reason = input('Please tell me: ')
print('I understand. Thanks for sharing')

# goodbye
print('It has been a long day')
print('I am too tired to talk. We can chat again later.')
print('Goodbye', name, 'I liked chatting with you')
