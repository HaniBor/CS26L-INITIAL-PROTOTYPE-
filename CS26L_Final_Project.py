import sys
Titles = {}

while True:
    print("==========MENU=========")
    print("1.Create title\n2.Add to title\n3.Show task\n4.Update\n5.Delete\n6.Exit")
    print("=======================")
    option = input("Choose option: ") 
 #=====CREATE TITLE=====   
    if option == "1":
        create = True
        while create:
            print("-----Type '0' Back to menu-----")
            create_titles = input("Title: ")
            
            if create_titles == "0":
                create = False
            else:
                if create_titles not in Titles:
                    Titles[create_titles] = []
                else:
                    print("TITLE ALREADY EXIST!")
 #=====ADD TO TITLE=====                           
    elif option == "2":
        priority = {"LOW", "MEDIUM", "HIGH"}
        status = {"PENDING", "IN PROGRESS", "COMPLETED"}
        confirm = True
       
        if not Titles:
            print("EMPTY, CREATE TITLES!")
            continue
        
        while confirm:          
            print("\n------TITLES------")
            for index, title_name in enumerate(Titles.keys(), 1):
                print(f"{index}. {title_name}")
            print("---SELECT TITLE---")
            selected_title = input("Enter exact name of title (0.Return): ")
        
            if selected_title in Titles:
                task_name = input("Task name: ")
                task_deadline = input("Enter deadline 'MM/DD/YY': ")
                p = True
                s = True 
                while p:
                    task_priority = input("Task priority 'LOW, MEDIUM, HIGH': ").upper()
                    if task_priority not in priority:
                        print("INVALID INPUT!")
                    else:
                        p = False
                while s:        
                    task_status = input("Task status 'PENDING, IN PROGRESS, COMPLETED': ").upper()
                    if task_status not in status:
                        print("INVALID INPUT!")
                    else:
                        s = False
            
                task_info = {"Task": task_name, "Deadline": task_deadline, "Priority": task_priority, "Status": task_status}
                Titles[selected_title].append(task_info)
            elif selected_title == "0":
                confirm = False
            else:
                print("INCORRECT SPELLING!")
 #=====SHOW TASK=====                
    elif option == "3":
        decide = True
        if not Titles:
            print("EMPTY!")
            continue
        
        while decide:
            print("\n------TITLES------")
            for index, title_name in enumerate(Titles.keys(), 1):
                print(f"{index}. {title_name}")
            print("---SELECT TITLE---")
            show_title = input("Enter exact name of title (0.Return): ")
        
            if show_title in Titles:
                task_inside_titles = Titles[show_title]
                if not task_inside_titles:
                    print("NO TASK ADDED!")
                else:    
                    for item in task_inside_titles:
                        print(f"Task name: {item['Task']} | Deadline: {item['Deadline']} | Priority: {item['Priority']} | Status: {item['Status']}")
            elif show_title == "0":
                decide = False
            else:
                print("INCORRECT SPELLING!")
 #=====UPDATE=====               
    elif option == "4":
        decision = True

        if not Titles:
            print("EMPTY!")
            continue

        while decision:
            # SELECT TITLE
            print("\n------TITLES------")
            for index, title_name in enumerate(Titles.keys(), 1):
                print(f"{index}. {title_name}")
            print("0. Return")

            update_title = input("Enter exact name of title: ")

            if update_title == "0":
                decision = False
                continue

            if update_title not in Titles:
                print("INCORRECT SPELLING!")
                continue

            update = True
            while update:
                # WHAT TO UPDATE
                print("\n-----WHAT TO UPDATE-----")
                print("1.Title")
                print("2.Task")
                print("3.Deadline")
                print("4.Priority")
                print("5.Status")
                print("0.Back")

                choice = input("Choose what to update: ")

                if choice == "0":
                    update = False
                    continue

                # UPDATE TITLE
                if choice == "1":
                    new_title = input("Enter new title: ")

                    if new_title == "0":
                        continue

                    if new_title in Titles:
                        print("TITLE ALREADY EXIST!")
                    else:
                        Titles[new_title] = Titles.pop(update_title)
                        update_title = new_title
                        print("TITLE UPDATED!")

                # UPDATE TASK
                elif choice == "2":
                    if not Titles[update_title]:
                        print("NO TASK ADDED!")
                        continue

                    task_choose = True

                    while task_choose:
                        print("\n------TASKS------")

                        for index, item in enumerate(Titles[update_title], 1):
                            print(f"{index}. {item['Task']}")

                        print("0. Back")

                        task_number = input("Choose task: ")

                        if task_number == "0":
                            task_choose = False
                            continue

                        if task_number.isdigit():
                            task_number = int(task_number)

                            if 1 <= task_number <= len(Titles[update_title]):
                                new_task = input("Enter new task: ")

                                if new_task != "0":
                                    Titles[update_title][task_number - 1]["Task"] = new_task
                                    print("TASK UPDATED!")
                            else:
                                print("INVALID TASK!")
                        else:
                            print("INVALID INPUT!")

                # UPDATE DEADLINE
                elif choice == "3":
                    if not Titles[update_title]:
                        print("NO TASK ADDED!")
                        continue

                    task_choose = True
                    while task_choose:
                        print("\n------TASKS------")

                        for index, item in enumerate(Titles[update_title], 1):
                            print(f"{index}. {item['Task']}")

                        print("0. Back")

                        task_number = input("Choose task: ")

                        if task_number == "0":
                            task_choose = False
                            continue

                        if task_number.isdigit():
                            task_number = int(task_number)

                            if 1 <= task_number <= len(Titles[update_title]):
                                new_deadline = input("Enter new deadline 'MM/DD/YY': ")

                                if new_deadline != "0":
                                    Titles[update_title][task_number - 1]["Deadline"] = new_deadline
                                    print("DEADLINE UPDATED!")
                            else:
                                print("INVALID TASK!")
                        else:
                            print("INVALID INPUT!")

                # UPDATE PRIORITY
                elif choice == "4":
                    if not Titles[update_title]:
                        print("NO TASK ADDED!")
                        continue

                    task_choose = True
                    while task_choose:
                        print("\n------TASKS------")

                        for index, item in enumerate(Titles[update_title], 1):
                            print(f"{index}. {item['Task']}")

                        print("0. Back")

                        task_number = input("Choose task: ")

                        if task_number == "0":
                            task_choose = False
                            continue

                        if task_number.isdigit():
                            task_number = int(task_number)

                            if 1 <= task_number <= len(Titles[update_title]):
                                new_priority = input("Enter new priority 'LOW, MEDIUM, HIGH': ").upper()

                                if new_priority == "0":
                                    continue

                                if new_priority in {"LOW", "MEDIUM", "HIGH"}:
                                    Titles[update_title][task_number - 1]["Priority"] = new_priority
                                    print("PRIORITY UPDATED!")
                                else:
                                    print("INVALID INPUT!")
                            else:
                                print("INVALID TASK!")
                        else:
                            print("INVALID INPUT!")

                # UPDATE STATUS
                elif choice == "5":
                    if not Titles[update_title]:
                        print("NO TASK ADDED!")
                        continue

                    task_choose = True
                    while task_choose:
                        print("\n------TASKS------")

                        for index, item in enumerate(Titles[update_title], 1):
                            print(f"{index}. {item['Task']}")

                        print("0. Back")

                        task_number = input("Choose task: ")

                        if task_number == "0":
                            task_choose = False
                            continue

                        if task_number.isdigit():
                            task_number = int(task_number)

                            if 1 <= task_number <= len(Titles[update_title]):
                                new_status = input("Enter new status 'PENDING, IN PROGRESS, COMPLETED': ").upper()

                                if new_status == "0":
                                    continue

                                if new_status in {"PENDING", "IN PROGRESS", "COMPLETED"}:
                                    Titles[update_title][task_number - 1]["Status"] = new_status
                                    print("STATUS UPDATED!")
                                else:
                                    print("INVALID INPUT!")
                            else:
                                print("INVALID TASK!")
                        else:
                            print("INVALID INPUT!")

                else:
                    print("INVALID OPTION!")
 #=====DELETE=====                            
    elif option == "5":
        if not Titles:
            print("EMPTY!")
            continue

        pick = True
        while pick:
            print("\n------TITLES------")
            for index, title_name in enumerate(Titles.keys(), 1):
                print(f"{index}. {title_name}")
            print("---SELECT TITLE---")
            delete_title = input("Enter exact name of title (0.Return): ")

            if delete_title == "0":
                pick = False
                continue
            if delete_title not in Titles:
                print("INCORRECT SPELLING!")
                continue

            delete = True
            while delete:
                print("\n-----WHAT TO DELETE-----")
                print("1.Title\n2.Task\n0.Back")
                user_input = input("Choose what to delete: ")

                if user_input == "0":
                    delete = False

                elif user_input == "1":
                    del Titles[delete_title]
                    print("TITLE DELETED!")
                    delete = False
                    if not Titles:
                        pick = False

                elif user_input == "2":
                    task_delete = True
                    while task_delete:
                        if not Titles[delete_title]:
                            print("NO TASK ADDED!")
                            task_delete = False
                            continue

                        print("\n------TASKS------")
                        for index, item in enumerate(Titles[delete_title], 1):
                            print(f"{index}. {item['Task']}")
                        print("0. Back")
                        task_num = input("Choose task: ")

                        if task_num == "0":
                            task_delete = False
                        elif task_num.isdigit():
                            task_num = int(task_num)
                            if 1 <= task_num <= len(Titles[delete_title]):
                                removed = Titles[delete_title].pop(task_num - 1)
                                print(f"'{removed['Task']}' DELETED!")
                            else:
                                print("INVALID TASK!")
                        else:
                            print("INVALID INPUT!")
                else:
                    print("INVALID OPTION!")
                    
 #=====EXIT=====            
    elif option == "6":
        confirmation = True
        while confirmation:
            pick = input("Do you want exit 'YES' or 'NO': ").upper()
            if pick == "YES":
                sys.exit()
            elif pick == "NO":
                confirmation = False
            else:
                print("INVALID OPTION!")
 #=====ERROR HANDLING=====  
    else:
        print("INVALID OPTION!")
        
        