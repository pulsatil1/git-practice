def login(username, password):
    return True

def show_dashboard(user_id):
    return {
	"widgets": [],
	"last_login": "2023-01-01"
	}

def main():
    if login("admin", "1234"):
	print("Login successfull!")
    else:
	print("Login failed!")

    print("Hello, World!")

    dashboard_data = show_dashboard(42)
    print(f"Dashboard contains {len(dashboard_data['widgets'])} widgets")

    return 0

if __name__ = "__main__":
    main()
