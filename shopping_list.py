shopping_list = []


def add_item(item: str) -> None:
    shopping_list.append({"item": item, "checked": False})
    print(f"Added: {item}")


def remove_item(item: str) -> None:
    for entry in shopping_list:
        if entry["item"] == item:
            shopping_list.remove(entry)
            print(f"Removed: {item}")
            return
    print(f"Item not found: {item}")


def check_item(item: str) -> None:
    for entry in shopping_list:
        if entry["item"] == item:
            entry["checked"] = True
            print(f"Checked: {item}")
            return
    print(f"Item not found: {item}")


def show_list() -> None:
    if not shopping_list:
        print("Shopping list is empty.")
        return
    print("Shopping List:")
    for entry in shopping_list:
        status = "[x]" if entry["checked"] else "[ ]"
        print(f"  {status} {entry['item']}")


if __name__ == "__main__":
    while True:
        print("\nOptions: add / remove / check / show / quit")
        command = input("> ").strip().lower()
        if command == "quit":
            break
        elif command == "add":
            item = input("Item name: ").strip()
            if item:
                add_item(item)
        elif command == "remove":
            item = input("Item name: ").strip()
            remove_item(item)
        elif command == "check":
            item = input("Item name: ").strip()
            check_item(item)
        elif command == "show":
            show_list()
        else:
            print("Unknown command.")
