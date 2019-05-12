def make_bricks(s, b, g):
    mb = g/5
    if mb<=b:
        g = g- mb*5
    else:
        g = g-b*5
        if(g <= s):
            print("True")
        else:
            print("False")

make_bricks(40,2,47)