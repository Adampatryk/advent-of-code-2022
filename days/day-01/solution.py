import pathlib

currentPath = pathlib.Path(__file__).parent.resolve()
filepath = pathlib.Path(currentPath, "input.txt")

#open file
f = open(filepath)

#initialise a max variable
maxCalorieForElf = 0

#initialise a calorie count variable
currentElfCalorieCount = 0

#for each line
for line in f:
    
    if line != "\n":    #current elf
        #if line has calories, add calories to current elf calorie count
        currentElfCalorieCount += int(line)
    else:               #new elf
        #if line is empty, 
        if (currentElfCalorieCount > maxCalorieForElf):
            maxCalorieForElf = currentElfCalorieCount
        currentElfCalorieCount = 0

#must do this one more time for the last elf
if (currentElfCalorieCount > maxCalorieForElf):
    maxCalorieForElf = currentElfCalorieCount

print(f'Elf with the most calories has {maxCalorieForElf} calories!')


    

    