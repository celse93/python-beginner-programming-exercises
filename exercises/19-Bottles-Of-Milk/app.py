# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range (99, -1, -1):
        if i == 0:
            print("No more bottles of milk on the wall, no more bottles of milk.\n" +
                "Go to the store and buy some more, 99 bottles of milk on the wall.")
        elif i == 1:
            print("1 bottle of milk on the wall, 1 bottle of milk.\n" +
                "Take one down and pass it around, no more bottles of milk on the wall.\n")
        else:
            print(f"{i} bottles of milk on the wall, {i} bottles of milk.\n" +
                f"Take one down and pass it around, {i-1} bottles of milk on the wall.\n")


number_of_bottles()
