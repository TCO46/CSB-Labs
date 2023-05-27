colors = ["purple", "blue", "pink", "green"]

print(f"Color list: {colors}")

delete_item_input = input("Item to delete: ")

if delete_item_input.isnumeric():
    delete_item_input = int(delete_item_input)
    colors.pop(delete_item_input - 1)
else:
    colors.remove(delete_item_input)

print(colors)