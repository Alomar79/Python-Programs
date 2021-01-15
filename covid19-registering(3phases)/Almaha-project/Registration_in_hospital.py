import random
import os.path

# Reserve room for the person in file (rooms)
def reserve_room(room_no):
    out = open("rooms_numbers.txt", "a")        
    out.write(str(room_no) + "\n")
    out.close()

# Reserve suite for the person in file (suites)
def reserve_suite(suite_no):
    out = open("suites_numbers.txt", "a")        
    out.write(str(suite_no) + "\n")
    out.close()

# Check a Room if reserved before
def is_room_reserved(room_no):
    isReserved = False
    # Check if the file exist
    if os.path.exists("rooms_numbers.txt"):
        # open rooms file in read mode
        ifile = open("rooms_numbers.txt", "r")
        line = ifile.readline().rstrip()
        # check if isn't reserved before (not stored in the file)
        while line !='' and isReserved == False:
            room = int(line)
            if room == room_no:
                isReserved = True
            line = ifile.readline().rstrip()
        ifile.close()
    # Return the state of the room
    return isReserved

# Check a Suite if reserved before
def is_suite_reserved(suite_no):
    isReserved = False
    # Check if the file exist
    if os.path.exists("suites_numbers.txt"):
        # open suites file in read mode
        ifile = open("suites_numbers.txt", "r")
        line = ifile.readline().rstrip()
        # check if isn't reserved before (not stored in the file)
        while line !='' and isReserved == False:
            suite = int(line)
            if suite == suite_no:
                isReserved = True
            line = ifile.readline().rstrip()
        ifile.close()
    # Return the state of the suite
    return isReserved

# Compute the Date now
def date_now():
    import datetime
    x = datetime.datetime.now()
    thisDay = x.strftime("%d")
    thisMonth = x.strftime("%m")
    thisYear = x.strftime("%y")   # return the year as 'yy' 
    reg_date = thisDay+'.'+thisMonth+'.'+thisYear
    return reg_date

# Write person information to the file
def writeToFile(id, name,insurance,insurance_plan, admission_date, staying_way, reserved_place_no, 
            medicine_cost, medicine_name, meeting_date, doctors_name):
  
    # Display header names
    if not os.path.exists("phase2.txt"):
        # Open file as first time
        out = open("phase2.txt", "w")
        # Header names 
        string = "ID \t Name \tinsurance\tinsurance_plan\tAdmission_date\tstaying_way\troom_no\t"\
            +"medicine_cost\tmedicine_name\tmeeting_date\tdoctors_name\n"
        out.write(string)
    # open file to append new person
    out = open("phase2.txt", "a")
    out.write(id)
    out.write("\t"+ name)
    out.write("\t"+ insurance)
    out.write("\t"+ insurance_plan)
    out.write("\t"+ admission_date)
    out.write("\t"+ staying_way)
    out.write("\t"+ str(reserved_place_no))
    out.write("\t"+ str(medicine_cost ))
    out.write("\t"+ medicine_name )
    out.write("\t"+ meeting_date)
    out.write("\t"+ doctors_name + "\n")
    out.close()

# Read person information by ID
def read_user_info(id):
    # open phase1 file in read mode
    infile = open("phase1.txt","r")
    next(infile)
    person_record = []
    found = False
    line = infile.readline().rstrip()
    # Read lines from the file to search about ID
    while line != '' and found == False:
        lst = line.split()
        if lst[0] == str(id):
            for x in lst:
                person_record.append(x)
            found = True
        line = infile.readline().rstrip()
    infile.close()
    # return list of fields of the person record
    return person_record

# Display the menu
def display_menu():
    print("\tregistration Phase")
    print("\t+++++++++++++++++++")
    print("Option 1: Insurance (Y/N)")
    print("Option 2: Date of Admission (dd/mm/yy)")
    print("Option 3: suites or normal room")
    print("Option 4: medicine info")
    print("Option 5: Doctors that examined him")
    print("Option 6: Exit\n")

# Print phase1 information
def display_phase1_info(id):
    # Call (read_user_info) function 
    person_record = read_user_info(id)
    print ("\nEarlier details for the patient: ", person_record[1])
    print("======================================")
    print("qatarId: ", person_record[0])
    print("birthDate: ", person_record[2])
    print("address: ", person_record[3])
    print("N-Residents: ", person_record[4])
    print("ex-Symptoms: ", person_record[5])
    print("symptomsComment: ", person_record[6])
    print("COVIDtest: ", person_record[7] , "\n")

# choosing the staying way
def staying_way():
    reserved = True
    stay_Way = (str(input("Suites or Normal room ? (S/N): "))).lower()
    # Check if the room reserved before
    while reserved == True:                    
        if stay_Way == "s":
            stayingWay = "Suite"
            # select suite No randomly
            suite_no = random.randint(1 , 4) 
            # check if the suite is not resreved before
            if is_suite_reserved(suite_no) == False:
                # Reserve the suite if its not reserved before
                reserve_suite(suite_no)
                reserved_place_no = suite_no
                reserved = False
        elif stay_Way == "n":
            stayingWay = "Room"
            # select room No randomly
            room_no = random.randint(1 , 21)
            # check if the room is not resreved before
            if is_room_reserved(room_no) == False:
                # Reserve the room if its not reserved before
                reserve_room(room_no)
                reserved_place_no = room_no
                reserved = False
    # Return staying way and the number of room
    return stayingWay , reserved_place_no

# check have Insurance
def Insurance_check():
    # Read insurance from the user
    insurance = (str(input("Option 1:Insurance (Y/N):"))).lower()
    if insurance == "y":
        # insert insurance plan
        insurance_plan = (str(input("prestige or normal plan (P or N): "))).lower()
        if insurance_plan == "p":
            insurance_plan = "Prestige"
        else:
            insurance_plan = "Normal"
    else:
        insurance_plan = "None"
        # Return insurance and insurance plan
    return insurance , insurance_plan

# Register the person in hospital
def registrar():
    # total_option variable : to check if all options done
    total_option = 0
    # ask to enter ID
    id = str(input("Enter user ID to show information : "))
    # print person info from phase1
    display_phase1_info(id)
    # find person record in the file by calling function
    person_record = read_user_info(id)
    name = person_record[1]
    # check if person state is positive or negative
    first_test_result = person_record[7]
    if first_test_result == "negative":
        print("The first result of test is Negative, No need to visit the hospital. \n")
    # if person state is positive, the will register in hospital
    elif first_test_result == "positive":
        display_menu()
        exit = False
        while exit == False and total_option < 5:
            option = int(input("Enter an option number: "))
            if option == 1:
                total_option += 1
                # Return insurance and insurance_plan by calling the function
                insurance, insurance_plan = Insurance_check()
            elif option == 2:
                admission_date = str(input("Option 2: Date of Admission (dd/mm/yy):"))
                total_option += 1
            elif option == 3: 
                # Return stayingWay and room_no by calling the function
                stayingWay, reserved_place_no = staying_way()
                total_option += 1

            elif option == 4:    
                medicine_cost = float(input("Cost of medicine : "))
                medicine_name = str(input("Name of medicine : "))
                total_option += 1
            
            elif option == 5:
                meeting_date = date_now()
                doctors_name = str(input("doctors names : "))
                total_option += 1

            # Exit the program .
            elif option == 6:
                exit = True
        if total_option == 5:
            # if all options done, the write information to the file
            writeToFile(id, name, insurance, insurance_plan, admission_date, stayingWay, 
            reserved_place_no, medicine_cost, medicine_name, meeting_date, doctors_name)
        print("\nPhase# 2 information saved successfully!\n")
        print("=========================================")
