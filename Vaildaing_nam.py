def check_Name():
    check = True

    get_Name = input("Enter a Gental Men name")
    if get_Name == "":
        print("You entered your name")
        check = False
        exit(101)

    else:
        for name in get_Name:
            if name in "01212312121":
                print("Your name are not allowed")
                check = False
                exit()
            elif name in "%!@%^*()&@&!)@*@#{@#":
                print("You name Special Character are not Allowed")
                check = False
                exit()
            elif name in "qwertyuiopasdfghjklzxcvbnm":
                print("Your name small letter are not allowed ")
                check = False
                exit()

        if check:
            print("You name is Correct")
            print("Congrulations")
check_Name()
