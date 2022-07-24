
row1 = ["🎞","🎞","🎞"]
row2 = ["🎞","🎞","🎞"]
row3 = ["🎞","🎞","🎞"]
map = [row1,row2,row3]
print(f"{row1}\n{row2} \n{row3}")
position = input("Where do you want to put the treasure?")
horizontal_position = int(position[0])-1
vertical_position = int(position[1])-1

map[vertical_position][horizontal_position]="X"
print(f"{row1}\n{row2} \n{row3}")
