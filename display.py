line0 = ["-","-","-","-","-"]
line1 = ["-","-","-","-","-"]
line2 = ["-","-","-","-","-"]
line3 = ["-","-","-","-","-"]

lines = [line0,line1,line2,line3]

pos_raw = [0,2]

posx = pos_raw[1]
posy = pos_raw[0]
pos = [posx,posy]


if pos[0] == 0:
    use_y = line0
if pos[0] == 1:
    use_y = line1
if pos[0] == 2:
    use_y = line2
if pos[0] == 3:
    use_y = line3

use_y[pos[1]] = "+"

for i in lines:
    for c in i:
        print(c, end = " ")
    print("\n")

while True:
    pos[0] = input("x:")
    pos[1] = input("y:")
