# imports modules.
import create_or_load_userprofile
import edit_or_delete_userprofile
import view_userprofile
import generate_book_recommendations
import view_userbooks_generate_budgeting_info


def main():
    username = 'stranger'
    # Constants for the menu choices
    CREATE_LOAD_USER_PROFILE = 1
    EDIT_DELETE_USER_PROFILE = 2
    VIEW_USER_PROFILE = 3
    GENERATE_BOOK_RECOMMENDATIONS = 4
    VIEW_USER_BOOKS_GENERATE_BUDGETING_INFO = 5
    QUIT_CHOICE = 6
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice  = 0
    is_recomendation_generated =False
    while choice != QUIT_CHOICE:
        # display the menu.
        display_menu()
        # Get the user's choice.
        choice = int(input('To perform any of the previous functions, enter its number:'))
        # Perform the selected action.
        if choice == CREATE_LOAD_USER_PROFILE:
            # using module to create or load profile then return username
            username = create_or_load_userprofile.create_or_load_profile(username)            
            
        elif choice == EDIT_DELETE_USER_PROFILE:
            # passing username into module to edit or delete profile then return new username
            username = edit_or_delete_userprofile.edit_delete_profile(username)

        elif choice == VIEW_USER_PROFILE:
            # if first_selection = 1:
            username = view_userprofile.view_userprofile(username)
            
        elif choice == GENERATE_BOOK_RECOMMENDATIONS:
            username, is_recomendation_generated = generate_book_recommendations.generate_book_recommendations(username,is_recomendation_generated)
            #View user books and generate budgeting information 
        elif choice == VIEW_USER_BOOKS_GENERATE_BUDGETING_INFO:
            print("-")
            
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')

# The display_menu function displays a menu.
def display_menu():
    print('+------------------------------------------------------------------------+')
    print('|+----------------------------------------------------------------------+|')
    print('|| Welcome to Bookable, your budget-friendly book recommendation system ||')
    print('|+----------------------------------------------------------------------+|')
    print('+------------------------------------------------------------------------+')
    print('In this system, you can perform one of the following tasks')
    print(' 1) Create or load a user profile')
    print(' 2) Edit or delete a user profile')
    print(' 3) View user profile')
    print(' 4) Generate book recommendations for the user')
    print(' 5) View user books and generate budget information ')
    print(' 6) Exit the program \n')
    

# Call the main function.
main()

            




