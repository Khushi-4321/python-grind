# ```
# 1. Create a list of 5 fruits with their prices (as strings)
#    e.g. "Apple - 50"
# 2. Write them to a file called "fruits.txt"
# 3. Read the file back line by line
# 4. Print only fruits that cost more than 40

fruits = ["Apple - 50", "Banana - 35", "Orange - 40", "Watermelon - 60", "Grapes - 140"]
with open("Fruit.txt" , "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")
                

with open("Fruit.txt", "r") as f:
    for line in f:
        parts = line.strip().split("-")
        if int (parts[1])>40:
           print(parts)
        
            