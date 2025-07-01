def main_menu():
    print("\n📚 Memoraid — Smart CLI Flashcards\n")
    print("1. List all decks")
    print("2. Create a new deck")
    print("3. Add a card to a deck")
    print("4. Study a deck")
    print("5. Delete a card or deck")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip()
    return choice