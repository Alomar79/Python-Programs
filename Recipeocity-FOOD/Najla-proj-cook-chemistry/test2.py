w = 7
def main(): 
    print("before " , w) 
    z , c = summation(5 , 9)  
    print("after " , w) 
 
    print("z=", z)
    print("c=", c)

def summation(x,y):
    # global w
    w = 19
    sum = x + y 
    half = sum / 2
    return sum , half


main()        