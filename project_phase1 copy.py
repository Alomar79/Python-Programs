import os.path

def menu():
    # Display menu driven
    print("\n Choose one of the following tasks: \n ")
    print("1. Testing phase registration")
    print("2. Registration in the hospital")
    print("3. Discharge summary ")
    print("4. Exit \n")
    print(" Enter your choice: ", end='')

def writeToFile(qatarId , personName , birthDay , birthMonth , birthYear, address,
        NumberOfResidents, externalSymptoms , symptomsComment , COVIDtest):
    # format birth date as dd.MM.yy
    birthDate = str(birthDay)+"."+ str(birthMonth)+"." + str(birthYear)[0:2]
    # Display header names
    if not os.path.exists("phase1.txt"):
        out = open("phase1.txt", "w")
        string = "qatarId".ljust(16)+"personName".ljust(16)+"birthDate".ljust(16) \
            +"address".ljust(16)+"N-Residents".ljust(16) \
            +"ex-Symptoms".ljust(16)+"symptomsComment".ljust(20)+"COVIDtest\n"
        out.write(string)
    # open file to append new person
    out = open("phase1.txt", "a")
    out.write("{0:16}".format(qatarId) )
    out.write("{0:16}".format(personName))
    out.write("{0:16}".format(birthDate))
    out.write("{0:16}".format(address))
    out.write("{0:16}".format(str(NumberOfResidents )))
    out.write("{0:16}".format(externalSymptoms ))
    out.write("{0:20}".format(symptomsComment))
    out.write("{0:1}".format(COVIDtest) + "\n")
    out.close()

def testing_phase():    
    qatarId = str(input("Enter QID for the person: "))
    personName = str(input("Enter Name of person: "))
    birthDay = int(input("Enter Day of Birth: "))
    while birthDay not in range(1,32) or type(birthDay) !=int:
        birthDay = int(input("Enter Day of Birth: "))
    birthMonth = int(input("Enter Birth Month: "))
    while birthMonth not in range(1,13) or type(birthMonth) !=int:
        birthMonth = int(input("Enter Birth Month: "))
    birthYear = int(input("Enter Birth year: "))
    while birthYear not in range(1900,2061) or type(birthYear) !=int:
        birthYear = int(input("Enter Birth year: "))
    address = str(input("Address: "))
    NumberOfResidents = int(input("How many of people residing? : "))
    while type(NumberOfResidents) !=int:
        NumberOfResidents = int(input("How many of people residing? : "))
    externalSymptoms = (str(input("Does he have external symptoms? (Y/N): "))).upper()
    if externalSymptoms == 'Y':
        symptomsComment = str(input("What the external Symptoms he has?: "))
    else:
        symptomsComment =" - "
    COVIDtest = str(input("Enter the result of COVID test (postitive or negative): "))
    # calling function to write the information in a file
    writeToFile(qatarId , personName , birthDay , birthMonth , birthYear, address,
        NumberOfResidents, externalSymptoms , symptomsComment , COVIDtest)
    """   return qatarId , personName , birthDay , birthMonth , birthYear, address, \
    NumberOfResidents, externalSymptoms , symptomsComment , COVIDtest  """
    main()

def reg_in_hospital():
    # we will update in future
    print("\nstart Registration in the hospital")
    print("we will update in future \n")
    main()

def discharge_summary():
    # we will update in future
    print("\nDischarge summary phase")
    print("we will update in future \n")
    main()

def main():
    # calling menu function to Display menu driven
    menu()    
    inp = int(input())
    # validate menue selection
    while  inp not in range(1,5):
        menu()
        inp = int(input())

    if inp == 1:
        testing_phase()
    elif inp == 2:
        reg_in_hospital()
    elif inp == 3:
        discharge_summary()
    else:
        print("\n Good bye!\n")

main()
