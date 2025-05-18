from DeadlineConnect import DeadlineCon

def test_deadline_connection():
    """
    A simple script to test the connection to the Deadline Web Service.
    """
    try:
        deadline_connection = DeadlineCon()
        print("Successfully connected to the Deadline Web Service!")

        # You can try a simple API call to further verify
        repository_info = deadline_connection.GetRepositoryInfo()
        if repository_info:
            print(f"Deadline Repository Name: {repository_info.RepositoryName}")
        else:
            print("Warning: Could not retrieve repository information.")

        deadline_connection.Close()

    except ImportError:
        print("Error: DeadlineConnect module not found. Ensure the Deadline Python API is accessible.")
    except Exception as e:
        print(f"Error connecting to Deadline Web Service: {e}")

if __name__ == "__main__":
    test_deadline_connection()