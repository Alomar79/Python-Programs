
# Read information of the person for (phase1 & phase2)
def read_person_info(id , filename):
    # open file in read mode
    infile = open(filename,"r")
    next(infile)
    person_record = []
    found = False
    line = infile.readline().rstrip()  
    # loop until find the person  
    while line != '' and found == False:
        lst = line.split()
        # Bring first index of the list, it's the ID field
        if lst[0] == str(id):
            for x in lst:
                person_record.append(x)
            found = True
        line = infile.readline().rstrip()
    infile.close()
    return person_record

# Compute discharge summary
def Discharge():
    # print("\n")
    id = str(input("Enter user ID to show information : "))
    
    # Bring person record in the file "phase1.txt"
    phase1_record = read_person_info(id , "phase1.txt")
    # Bring person record in the file "phase2.txt"
    phase2_record = read_person_info(id , "phase2.txt")
    day_cost = 0
    staying_days = 0
    medicine_cost = 0
    if len(phase2_record) == 0:
        total_bill = 0
        

        #medicine_cost = float(medicine_cost)
    else:        
        # insert the number of days the person spent
        staying_days = int(input("Enter the number of staying days :"))
        # Bring insurance info from the file
        insurance = phase2_record[2]
        plan =  phase2_record[3]
        
        # calculate cost depend on insurance
        if insurance == "y":
            medicine_cost = 0
            if plan == "Normal":
                day_cost = 100
            elif plan == "Prestige":
                day_cost = 400
        elif insurance == "None":
            day_cost = 700
            medicine_cost = float(phase2_record[7])    
        # calculate the total bill
        total_bill = day_cost * staying_days + medicine_cost
    # return person records, the bill and the staying days
    return phase1_record , phase2_record , total_bill, staying_days

# main discharge_phase function 
def make_discharge_summary():

    # Bring person and bill information by calling 'Discharge' function.
    phase1_record , phase2_record , total_bill , staying_days = Discharge()
    if len(phase2_record) == 0:
        print("\nThe person didn't registered in hospital!\n")
        return 0
    # Print some of person information from phase1.
    print("\nQatar Id   : ", phase1_record[0] )
    print("Name         : ", phase1_record[1] )
    print("birthDate    : ", phase1_record[2] )
    print("ex-Symptoms  : ", phase1_record[5] )
    print("COVIDtest    : ", phase1_record[7] )
    # Print some of person information from phase2.
    print("insurance    : ", phase2_record[2] )
    print("plan         : ", phase2_record[3] )
    print("Admission_date: ", phase2_record[4] )
    print("room_no      : ", phase2_record[6] )
    print("meeting_date: ", phase2_record[9] )
    # Print some of bill information.
    print("\n\tThe Total bill : ")
    print("\t---------------------")
    print("\tTotal Days   : ", staying_days)
    print("\tMedicine     : ", phase2_record[8])
    print("\tTotal amount : " , total_bill , " QR \n" )
