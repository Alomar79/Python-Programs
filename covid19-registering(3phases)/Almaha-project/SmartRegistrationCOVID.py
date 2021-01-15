import Registration_in_hospital
import discharge_phase
import os

def menu():
    # Display menu
    print("\n Choose one of the following tasks :  ")
    print("----------------------------------")
    print("1. Testing phase registration")
    print("2. Registration in the hospital")
    print("3. Discharge summary ")
    print("4. Exit \n")
    print("Enter your choice: ", end='')

# Write function to file
def writeToFile(qatarId , personName , birthDate , address,
        Residents, externalSymptoms , symptomsComment , COVIDtest):    
    # format birth date as dd.MM.yy
    birthDate = birthDate.split(".")
    if int(birthDate[0]) < 10:
        day = "0" + str(birthDate[0])
    else:
        day =  str(birthDate[0])
    if int(birthDate[1]) < 10:
        monthNumber = "0" + str(birthDate[1])
    else:
        monthNumber =  str(birthDate[1])
    
    if int(birthDate[2]) < 10:
        year = "0" + str(birthDate[2])
    else:
        year =  str(birthDate[2])  
    birthDate = day + "."+ monthNumber + "." + year
    
    # check if the file exist before writing
    if not os.path.exists("phase1.txt"):
        out = open("phase1.txt", "w")
        # string variable to Display header names
        string = "qatarId \t personName \t birthDate \t address \t N-Residents \t ex-Symptoms \t symptomsComment \t COVIDtest\n"
        out.write(string)
    # open file to append new person
    out = open("phase1.txt", "a")
    out.write(qatarId) 
    out.write( "\t"+ personName)
    out.write("\t"+birthDate)
    out.write("\t"+ address)
    out.write("\t"+ str(Residents ))
    out.write("\t"+ externalSymptoms )
    out.write("\t"+ symptomsComment)
    out.write("\t"+ COVIDtest + "\n")
    out.close()
    out.close()

# Phase 1 (Testing Phase)    
def testing_phase():
    # Reading from the user
    qatarId = str(input("Enter QID for the person: "))
    personName = str(input("Enter Name of person: "))
    birthDate = str(input("Enter Date of Birth(dd.mm.yy): "))    
    address = str(input("Address: "))
    Residents = int(input("How many of people residing? : "))
    # Validate the input (integer input)
    while type(Residents) !=int:
        Residents = int(input("How many of people residing? : "))
    
    externalSymptoms = (str(input("Does he have external symptoms? (Y/N): "))).upper()
    # Entering the external symptoms
    if externalSymptoms == 'Y':
        symptomsComment = str(input("What the external Symptoms he has?: "))
    else:
        symptomsComment =" - "
    COVIDtest = str(input("Enter the result of COVID test (postitive or negative): "))
    # calling function to write the information to a file
    writeToFile(qatarId , personName , birthDate , address, Residents, externalSymptoms , symptomsComment , COVIDtest)
    # calling main() to display menu again
    main()

# Phase 2 (Registration Phase)
def reg_in_hospital():
    # Calling function in discharge_phase Module for Registration_in_hospital
    Registration_in_hospital.registrar()
    # calling main() to display menu again
    main()

# Phase 3 (Discharge Phase)
def discharge_summary():
    # Calling function in discharge_phase Module
    discharge_phase.make_discharge_summary()
    # calling main() to display menu again
    main()

def main():
    # calling menu function to Display menu driven
    menu()  
    # Read choice input from the user  
    inp = int(input())
    # Validate menu selection (4 choices)
    while  inp not in range(1,5):
        menu()
        inp = int(input())
    # working with user choice 
    if inp == 1:
        testing_phase()
    elif inp == 2:
        reg_in_hospital()
    elif inp == 3:
        discharge_summary()
    else:
        print("\n Exit program!\n")

# Calling main function
main()