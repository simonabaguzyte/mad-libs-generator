print("\n****WELCOME TO MAD LIBS GENERATOR!***")

shouldContinue = 1
while shouldContinue == 1:

    print("\nPlease, enter a series of inputs below:")
    name1 = input("Name: ")
    name2 = input("2nd name: ")
    dish = input("Dish: ")
    beverage = input("Beverage: ")
    city = input("City: ")
    number = input("Number (2-9): ")
    activity = input("Activity: ")


    if name1.endswith('s') and name2.endswith('s'):
        print("\n\tOne early morning little boy named %s was walkind down the forest to visit \
his beloved grandfather %s. %s was bringing to his grandfather freshly made %s and %s bottles of %s. \
The boy had to travel all day because his grandfather %s lived in %s, far far away from him. \
As soon as %s reached his grandfather's house, he realized that his grandfather %s \
was not at home - that day he had %s practice. Little boy %s was so tired and upset \
that he took %s bottles of %s and drunk every last drop of it. After a good nap the boy went back home." \
% (name1, name2, name1, dish, number, beverage, name2, city, name1, name2, activity, name1, number, beverage))

    elif name1.endswith('s'):
        print("\n\tOne early morning little boy named %s was walkind down the forest to visit \
his beloved grandmother %s. %s was bringing to his grandmother freshly made %s and %s bottles of %s. \
The boy had to travel all day because his grandmother %s lived in %s, far far away from him. \
As soon as %s reached his grandmother's house, he realized that his grandmother %s \
was not at home - that day she had %s practice. Little boy %s was so tired and upset \
that he took %s bottles of %s and drunk every last drop of it. After a good nap the boy went back home." \
% (name1, name2, name1, dish, number, beverage, name2, city, name1, name2, activity, name1, number, beverage))

    elif name2.endswith('s'):
        print("\n\tOne early morning little girl named %s was walkind down the forest to visit \
her beloved grandfather %s. %s was bringing to her grandfather freshly made %s and %s bottles of %s. \
The girl had to travel all day because her grandfather %s lived in %s, far far away from her. \
As soon as %s reached her grandfather's house, she realized that her grandfather %s \
was not at home - that day he had %s practice. Little girl %s was so tired and upset \
that she took %s bottles of %s and drunk every last drop of it. After a good nap the girl went back home." \
% (name1, name2, name1, dish, number, beverage, name2, city, name1, name2, activity, name1, number, beverage))

    else:
        print("\n\tOne early morning little girl named %s was walkind down the forest to visit \
her beloved grandmother %s. %s was bringing to her grandmother freshly made %s and %s bottles of %s. \
The girl had to travel all day because her grandmother %s lived in %s, far far away from her. \
As soon as %s reached her grandmother's house, she realized that her grandmother %s \
was not at home - that day she had %s practice. Little girl %s was so tired and upset \
that she took %s bottles of %s and drunk every last drop of it. After a good nap the girl went back home." \
% (name1, name2, name1, dish, number, beverage, name2, city, name1, name2, activity, name1, number, beverage))


    answer = input("\n\nWould you like to try again (Y/N)? ")

    if answer.startswith('y' or 'Y'):
        shouldContinue = 1
    elif answer.startswith('n' or 'N'):
        shouldContinue = 0
        print("Thank you for using my program!")
    else:
        print("Please, check your input and try again")
        shouldContinue = 2
        
        
