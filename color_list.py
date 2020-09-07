color_list= ["Red","Green","Black","Yellow","Blue","Pink"]
n=len(color_list)
print ("Number of colors in the list : ", n)
def my_func():
    v=int(input("Input the position at which you want to know the color : "))
    print("\n")
    if(v>n-1):
        print("Please enter appropriate location !")
        print("\n")
    else:
        print("The color at position " +str(v)+" is : " + color_list[v])
while(True):
    my_func()
