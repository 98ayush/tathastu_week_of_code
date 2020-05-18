run1=int(input("enter run of player 1 "))
run2=int(input("enter run of player 2 "))
run3=int(input("enter run of player 3 "))
strike_rate1=run1*100 / 60
strike_rate2=run2*100 / 60
strike_rate3=run3*100 / 60
print("strike rate of player 1 is ",strike_rate1)
print("strike rate of player 2 is ",strike_rate2)
print("strike rate of player 3 is ",strike_rate3)
print("run when player 1 played 60 balls more ",run1*2)
print("run when player 2 played 60 balls more ",run2*2)
print("run when player 3 played 60 balls more ",run3*2)
print("maximum no of six player 1 could have ",run1//6)
print("maximum no of six player 2 could have ",run2//6)
print("maximum no of six player 3 could have ",run3//6)
