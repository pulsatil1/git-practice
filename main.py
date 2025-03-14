def show_dashboard(user_id):
    return {
	"widgets": [],
	"last_login": "2023-01-01"
	}

def main():
    print("Hello, World!")

    dashboard_data = show_dashboard(42)
    print(f"Dashboard contains {len(dashboard_data['widgets'])} widgets")

    return 0

if __name__ = "__main__":
    main()
