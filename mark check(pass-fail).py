# write python program that get the mark of a student as an input, 
# and check if the student pass or Fail.
#     Pass Mark = 25 
#     >50 or <0 Display out of range.


mark=int(input("Enter the mark:"))
if (mark < 0) or (mark > 50):
    print("out of range!")
else:
    if mark > 25:
        print("Pass")
    else:
        print("Fail") 