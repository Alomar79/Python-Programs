# imports modules.
import create_or_load_userprofile
import edit_or_delete_userprofile
import view_userprofile
import generate_recipe_recommendations
import view_usermeals_generate_health_info


# The main function.
def main():
    username = 'stranger'
    # Constants for the menu choices
    CREATE_LOAD_USER_PROFILE = 1
    EDIT_DELETE_USER_PROFILE = 2
    VIEW_USER_PROFILE = 3
    GENERATE_RECIPE_RECOMMENDATIONS = 4
    VIEW_USER_MEALS_GENERATE_HEALTH_INFO = 5
    QUIT_CHOICE = 6

    is_session_recipes_generated = False
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice  = 0
    while choice != -1:
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
            username = edit_or_delete_userprofile.edit_or_delete_profile(username)

        elif choice == VIEW_USER_PROFILE:
            # if first_selection = 1:
            username = view_userprofile.view_userprofile(username)
            
        elif choice == GENERATE_RECIPE_RECOMMENDATIONS:
            username , is_session_recipes_generated = generate_recipe_recommendations.generate_recipe_recommendations(username,is_session_recipes_generated)
            
        elif choice == VIEW_USER_MEALS_GENERATE_HEALTH_INFO:
            username = view_usermeals_generate_health_info.view_usermeals_generate_health_info(username)
            #view_usermeals_generate_health_info.generate_health_info()
            
        elif choice == QUIT_CHOICE:
            print('\nExiting the program...\n')
            username = "stranger"
            break
        else:
            print('\nError: choice must be between 1 , 6.')
        print("\n")
        


# The display_menu function displays a menu.
def display_menu():
    print('+------------------------------------------------------+')
    print('|+----------------------------------------------------+|')
    print('|| Welcome to Recipeosity, your personal meal planner ||')
    print('|+----------------------------------------------------+|')
    print('+------------------------------------------------------+')
    print('In this system, you can perform one of the following tasks')
    print(' 1) Create or load a user profile')
    print(' 2) Edit or delete a user profile')
    print(' 3) View user profile')
    print(' 4) Generate recipe recommendations for the session')
    print(' 5) View user meals and generate health information')
    print(' 6) Exit the program \n')
    

# Call the main function.
main()

            




