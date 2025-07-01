#!/usr/bin/env python3
from memoraid.cli import main_menu

if __name__ == "__main__":
    while True:
        try:
            option = int(main_menu())
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        match option:
            case 1:
                list_decks()
            case 2:
                create_deck()
            case 3:
                add_card()
            case 4:
                study_deck()
            case 5:
                delete_menu()
            case 6:
                print("Goodbye! 👋")
                break
            case _:
                print("❌ Invalid choice. Try again.")
