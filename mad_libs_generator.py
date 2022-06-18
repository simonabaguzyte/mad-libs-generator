print("\n****WELCOME TO THE MAD LIBS GENERATOR!***")

shouldContinue = True
while shouldContinue:

    print("\nPlease, enter a series of inputs below:")
    name1 = input("Name: ")
    name2 = input("Friend's name: ")
    dish = input("Dish: ")
    beverage = input("Beverage: ")
    city = input("City: ")
    number = input("Number (2-9): ")
    activity = input("Activity: ")

    name1_male = name1.endswith('s')
    name2_male = name2.endswith('s')

    if name1_male and name2_male:
        print(f"\n\tOne early morning little boy named {name1} was walkind down the forest to visit " +\
              f"his beloved grandfather {name2}. {name1} was bringing to the grandfather freshly made {dish} and {number} bottles of {beverage}. " +\
              f"The boy had to travel all day because his grandfather {name2} lived in {city}, far far away from him. " +\
              f"As soon as {name1} reached his grandfather's house, he realized that his grandfather {name2} " +\
              f"was not at home - that day he had {activity} practice. Little boy {name1} was so tired and upset " +\
              f"that he took {number} bottles of {beverage} and drank every last sip of it. After a good nap the boy went back home.")

    elif name1_male:
        print(f"\n\tOne early morning little boy named {name1} was walkind down the forest to visit " +\
              f"his beloved grandmother {name2}. {name1} was bringing to the grandmother freshly made {dish} and {number} bottles of {beverage}. " +\
              f"The boy had to travel all day because his grandmother {name2} lived in {city}, far far away from him. " +\
              f"As soon as {name1} reached his grandmother's house, he realized that his grandmother {name2} " +\
              f"was not at home - that day she had {activity} practice. Little boy {name1} was so tired and upset " +\
              f"that he took {number} bottles of {beverage} and drank every last sip of it. After a good nap the boy went back home.")

    elif name2_male:
        print(f"\n\tOne early morning little girl named {name1} was walkind down the forest to visit " +\
              f"her beloved grandfather {name2}. {name1} was bringing to the grandfather freshly made {dish} and {number} bottles of {beverage}. " +\
              f"The girl had to travel all day because her grandfather {name2} lived in {city}, far far away from her. " +\
              f"As soon as {name1} reached her grandfather's house, she realized that her grandfather {name2} " +\
              f"was not at home - that day he had {activity} practice. Little girl {name1} was so tired and upset " +\
              f"that she took {number} bottles of {beverage} and drank every last sip of it. After a good nap the girl went back home.")

    else:
        print(f"\n\tOne early morning little girl named {name1} was walkind down the forest to visit " +\
              f"her beloved grandmother {name2}. {name1} was bringing to the grandmother freshly made {dish} and {number} bottles of {beverage}. " +\
              f"The girl had to travel all day because her grandmother {name2} lived in {city}, far far away from her. " +\
              f"As soon as {name1} reached her grandmother's house, she realized that her grandmother {name2} " +\
              f"was not at home - that day she had {activity} practice. Little girl {name1} was so tired and upset " +\
              f"that she took {number} bottles of {beverage} and drank every last sip of it. After a good nap the girl went back home.")

    while True:
        answer = input("\n\nWould you like to try again (Y/N)? ").lower()

        if answer == 'y' or answer == 'yes':
            break
        elif answer == 'n' or answer == 'no':
            print("Thank you for using my program!")
            shouldContinue = False
            break
        else:
            print("Please, check your input and try again:")
        
        
        
        
