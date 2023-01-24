def voter_check(age):
    if (age >=18):
        print('Able for vote')
    else:
        print('still kid you are')

your_age = int(input('Enter your age:'))

voter_check(your_age)