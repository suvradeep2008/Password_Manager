import time
password_1 = None
username_1 = None
attempts = 3
vault = {}

# SIGN UP FUNTION


def sign_up():
    username_1 = input("Create a username: ")
    password_1 = input("Create a password: ")
    password_2 = input("Confirm your password: ")

    if password_1 == password_2:
        print("\nSign up successful!")
        return username_1, password_1
    else:
        print("\nPasswords do not match. Please try again.")
        return None, None

# SIGN IN FUNCTION


# username_1 and password_1 are passed as arguments to the function
def sign_in(saved_username, saved_password):
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    if username == saved_username and password == saved_password:
        return True
    else:
        return False

# DATABASE FUNCTION


def database():
    while True:
        print("\n---Menu---")
        print("1. Add site and account")
        print("2. View saved sites and accounts")
        print("3. Delete site and account")
        print("4. Exit")

        user_choice = input("\nEnter your choice: ")
        if user_choice == "1":
            service_name = input("Enter service name: ").strip().lower()
            user_password = input("Enter password: ")
            vault[service_name] = user_password
            print(
                f"Credentials for {service_name.title()} added successfully.")
            continue

        elif user_choice == "2":
            if len(vault) == 0:
                print("\nNo data found in database. Please add a site first.")
            else:
                print("\nSaved accounts and passwords: ")
                for service_name, user_password in vault.items():
                    print(
                        f"Service: {service_name.title()} || Password: {user_password}")

        elif user_choice == "3":
            service_to_delete = input(
                "Enter service name you want to delete: ").strip().lower()
            if service_to_delete in vault:
                del vault[service_to_delete]
                print(
                    f"Credentials for {service_to_delete.title()} deleted successfully.")
            else:
                print(
                    f"Service {service_to_delete.title()} not found in database.")
        elif user_choice == "4":
            print("\nSecuring database...")
            print("Exiting database...")
            time.sleep(2)
            break
        else:
            print("\nInvalid choice. Please try again.")


# MENU BLOCK


while True:
    print("\nWelcome to Secure Vault")
    print("---Menu---")
    print("1. Sign up")
    print("2. Sign in")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        username_1, password_1 = sign_up()

    elif choice == "2":
        if password_1 is None or username_1 is None:
            print("\nNo account found in database. Please sign up first.")
            print("Redirecting to sign up...")
            time.sleep(2)
            continue
        else:
            while attempts > 0:
                # sign_in returns either True or False
                login_success = sign_in(username_1, password_1)

                if login_success:  # basically, if login_success == True
                    print(f"\nAccess granted. Welcome back, {username_1}!")
                    attempts = 3  # Reset attempts after successful login
                    database()
                    break
                else:
                    attempts = attempts - 1
                    if attempts <= 0:
                        for seconds_left in range(10, 0, -1):  # timer
                            print(
                                f"Too many failed attempts. Try again after {seconds_left} seconds", end="\r")
                            time.sleep(1)

                        print()
                        attempts = 3  # Reset attempts after lockout
                        break

                    else:
                        print(f"\nWrong username or password.")
                        print(f"Access denied. {attempts} attempts left.")

    elif choice == "3":
        print("\nExiting Secure Vault...")
        time.sleep(2)
        break

    else:
        print("\nInvalid choice. Please try again.")
