# norrisa
# 2.t1 - python program
# program works 

def option_1():
    print("Your prescription is ready for pickup.")

def option_2():
    print("Your prescription will be cancelled.")

def main():
    while True:
        print("\nMenu:")
        print("1. Pickup prescription")
        print("2. Cancel prescription")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()