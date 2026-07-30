
import subprocess

def main():
    while True:
        print("\nOptions:")
        print("1. Run TXF Risk Calculator")
        print("2. Run Something Else")
        print("3. Run Another Thing")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                subprocess.run(['python', 'txf_risk_calculator.py'], check=True)
            except FileNotFoundError:
                print("txf_risk_calculator.py not found.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred: {e}")
            else:
                print("TXF Risk Calculator executed successfully.")
        elif choice == "2":
            print("Option 2 is working...")
        elif choice == "3":
            print("Option 3 is working...")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
