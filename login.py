# Sample user accounts and passwords
user_accounts = {
    "user1": "password1",
    "user2": "password2",
}

# User sessions
active_user = None

# Simulate user registration
def register_user():
    username = input("Enter a username: ")
    password = input("Create a password: ")
    user_accounts[username] = password
    print("Registration successful.")

# Simulate user login
def login_user():
    global active_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_accounts and user_accounts[username] == password:
        active_user = username
        print(f"Login successful. Welcome, {active_user}!")
    else:
        print("Login failed. Invalid credentials.")

# Simulate user logout
def logout_user():
    global active_user
    active_user = None
    print("Logout successful.")

# User interface with login and registration
def user_interactions_with_login():
    while True:
        if active_user:
            print(f"Logged in as: {active_user}")
        else:
            print("Not logged in")

        print("1. Browse AI services")
        print("2. Purchase AI services")
        print("3. List AI services")
        print("4. Check owned AI services")
        print("5. Check balance")
        print("6. View transaction
