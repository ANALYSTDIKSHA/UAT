try:
    user = int(input("Enter a number : "))

    if user <= 0:
        print("Ahhh crack head, enter a number which is more than 0")
    else:
        import random
        num = random.randint(1,user)
        print("Number from computer ji is : ", num)
        ans = 1
        guess = 0
        while num != ans:
            guess = guess + 1
            try:
                ans = int(input("Enter a number which you think Computer ji has entered : "))
                
                if num == ans:
                    print("Correct")
                elif num <  ans:
                    print("Try a lesser number may be.")
                elif num > ans:
                    print("Try a higher number may be.")
                    # print("Try again")
            except:
                print("Not a number try again")
        print("Total gueesses are : ", guess)

except ValueError:
    print("Heyy, I've asked you to enter a number :( ")