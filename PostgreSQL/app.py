from socket import TCP_NODELAY


from database import add_entry, view_entries

menu = ""Please select one of the following options:
1) Add new entry for today
2) View entries
3) Exit

Your selection: ""

welcome="Welcome to the programming diary!"

print(welcome)

# code for the user menu

while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing...")
    else:
        print("Invalid option, please try again")
