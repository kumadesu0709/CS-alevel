
to_do_list = ["aaa","bbb"]
anyotherfunction = "yes"
whichtask = ""
i = 0

while anyotherfunction == "yes":
    x = int(input("What function would you like to use? (1 = add a task, 2 = display all tasks, 3 = check the next task, 4 = complete the task, 5 = quit to do list)"))
    if x == 5:
        print("Thank you for using the to do list.")
        break
    if x == 1:
        anyothertask = "yes"
        while anyothertask == "yes":
            to_do_list.append(input("What task would you like to add"))
            print("Your task has been added.")
            anyothertask = input("is there any other task that you want to add? (answer yes or no)")
            if anyothertask == "no":
                anyotherfunction = input("Is there any other function that you want to use?(answer yes or no)")
                if anyotherfunction == "no":
                    print("Thank you for using the to do list.")

    if x == 2:
        for n,l in enumerate(to_do_list):
            print("task" + str(n+1) + ":" + str(l))
        anyotherfunction = input("Is there any other function that you want to use?(answer yes or no)")
        if anyotherfunction == "no":
                    print("Thank you for using the to do list.")
    if x == 4:
        if to_do_list == []:
            print("At the moment you don't have any task to do.")
        else:
            while whichtask != "no":
                print("At the moment your tasks are:")
                for n,l in enumerate(to_do_list):
                    print("task" + str(n+1) + ":" + str(l))
                whichtask = input("Which task would you like to remove? (answer the task number)")
                to_do_list.remove(to_do_list[int(whichtask)-1])
                print("Now your tasks are:")
                for n,l in enumerate(to_do_list):
                    print("task" + str(n+1) + ":" + str(l))
                whichtask = input("would you like to remove any other task?(answer yes or no)")
                if whichtask == "no":
                     anyotherfunction = input("Is there any other function that you want to use?(answer yes or no)")
    if x == 3:
        print(to_do_list[i])
        i = i + 1



