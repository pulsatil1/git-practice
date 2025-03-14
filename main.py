def login(username, password):
    return True

def main():
    if login("admin", "1234"):
	print("Login successfull!")
    else:
	print("Login failed!")

    print("Hello, World!")
    return 0

if __name__ = "__main__":
    main()
