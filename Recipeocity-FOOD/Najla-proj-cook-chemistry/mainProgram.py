
import create_load_profile
import edit_delete_userprofile
import view_userprofile
import generate_recipe_recommendations
import view_usermeals_health_info


def print_menu():
    print('\n|| Welcome to Recipeosity, your personal meal planner ||\n')
    print('-----------------------------------------------------')
    print('In this system, you can perform one of the following tasks:')
    print(' 1) Create or load a user profile')
    print(' 2) Edit or delete a user profile')
    print(' 3) View user profile')
    print(' 4) Generate recipe recommendations for the session')
    print(' 5) View user meals and generate health information')
    print(' 6) Exit the program \n')

def main():
    username = 'stranger'
    is_recipes_generated = False
    choice = 0 
    # loop for display menu again after finishing each task       
    while (choice != -1):
        print_menu()
        choice = int(input('To perform any of the previous functions, enter its number:'))
        if choice == 1:
            username = create_load_profile.create_load_profile(username)
            #user = option1_b("")
        elif choice == 2:
            # edit profile by passing username, and recieve new username
            username = edit_delete_userprofile.edit_delete_profile(username)

        # view user profile by username
        elif choice == 3:
            username = view_userprofile.view_userprofile(username)

        # Generate recipes
        elif choice == 4:
            username, is_recipes_generated = generate_recipe_recommendations.generate_recipe_recommendations(username,is_recipes_generated)
        
        # view usermeals
        elif choice == 5:
            username = view_usermeals_health_info.view_usermeals_health_info(username)
        
        # Exit
        elif choice == 6:
            print('\nExiting the program...\n')
            break
        else:
            print('\nError: try again.\n')
        print("")
                 

main()

