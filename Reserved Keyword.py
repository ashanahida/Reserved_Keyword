from printing_functions import main_menu
from operation_functions import user_input


def start():
    main_menu()
    user_input()


start()

def main_menu():
    # main menu for keyword program
    print(""" 
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    +           1.Add a new keyword                      +
    +           2.Update a keyword                       + 
    +           3.Delete a keyword                       +
    +           4.Print all keywords                     +
    +           5.Search for a keyword                   +
    +           6.Export to a file                       +
    +           8.quit                                   +
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """)


def update_menu():
    # update keyword or sample code
    print("""
    1.Update the name of a keyword
    2.Update the description of a keyword
    3.Update the sample code of a keyword
    4.Return to the main menu
    """)


def add_keyword_menu():
    # add keywords in the directory
    print("""
    1.Add a new keyword
    2.Return to the main menu
    """)


def quit():
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("BYE BYE!")


keywords = {

}

from printing_functions import main_menu, quit, update_menu
from dictionary import keywords


def user_input():
    menu = input("Please enter your choice: ")
    while menu != "8":
        if menu == "1":
            add_keyword()
        elif menu == "2":
            update_keyword()
        elif menu == "3":
            remove_keyword()
        elif menu == "4":
            show_all_keywords()
        elif menu == "5":
            search_keyword()
        elif menu == "6":
            export()
        elif menu == "7":
            remove_all_keywords()
        else:
            print("Invalid choice!!!")
    quit()


def update_keyword():
    # for updating keyword
    print("go back? Press 'b'")
    input_keyword = input("Enter the keyword: ")
    while input_keyword.lower() != "b":
        for key, value in keywords.items():
            if input_keyword.lower() == key.lower():
                print("Name:", value["name"])
                print("Description:", value["des"])
                print("sample Code:", value["sc"])
                update_menu()
                user_input_update(value["name"])
                break
        else:
            print("Not found")
        break
    else:
        main_menu()
        user_input()


def add_keyword():
    print("go back? Press 'b'")
    input_keyword = input("Please enter the keyword: ")

    while input_keyword.lower() != "b":
        for key, value in keywords.items():
            if input_keyword.lower() == key.lower():
                print("Keyword already exists")
                break
        else:
            input_description = input("Please enter the description: ")
            input_sample_code = input("Please enter the sample code: ")
            keywords[input_keyword] = {
                "name": input_keyword,
                "des": input_description,
                "sc": input_sample_code
            }
            print("Keyword added successfully")
            break
        break
    else:
        main_menu()
        user_input()


def search_keyword():
    # used for searching keyword
    print("go back? Press 'b'")
    input_keyword = input("Enter the keyword: ")
    while input_keyword.lower() != "b":
        for key, value in keywords.items():
            if input_keyword.lower() == key.lower():
                print("Name:", value["name"])
                print("Description:", value["des"])
                print("Sample Code:", value["sc"])
                break
        else:
            print("Not found")
        break
    else:
        main_menu()
        user_input()


def user_input_update(input_keyword):
    menu = input("Enter your choice: ")
    while menu != "4":
        if menu == "1":
            input_name = input("Enter the new keyword: ")
            keywords[input_keyword]["name"] = input_name
            print("Keyword name updated")
            break
        elif menu == "2":
            input_description = input("Enter the new description: ")
            keywords[input_keyword]["des"] = input_description
            print("Keyword description updated")
            break
        elif menu == "3":
            input_sample_code = input("Enter the new sample code: ")
            keywords[input_keyword]["sc"] = input_sample_code
            print("Keyword sample code updated")
            break
        else:
            print("Invalid choice")
            break
    main_menu()
    user_input()


def remove_keyword():
    print("Press 'a' for previous option")
    input_keyword = input("Please enter the keyword: ")
    while input_keyword.lower() != "a":
        for key, value in keywords.items():
            if input_keyword.lower() == key.lower():
                del keywords[key]
                print("Keyword removed successfully")
                break
        else:
            print("Not found")
        break
    else:
        main_menu()
        user_input()


def show_all_keywords():
    count = 0
    for key, value in keywords.items():
        print("Keyword", count, ":", key)
        count += 1
        for key, value in value.items():
            print(key + ": ", value)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    main_menu()
    user_input()


def remove_all_keywords():
    keywords.clear()
    print("All keywords removed successfully")


def export():
    with open("keywords.txt", "w") as f:
        count = 0
        for key, value in keywords.items():
            count += 1
            print(str(count) + ".", file=f)
            for key, value in value.items():
                f.write(key + ": " + value + "\n")
            f.write(
                "+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("File exported")

    main_menu()
    user_input()
