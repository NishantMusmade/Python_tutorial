import sys

def main():
    print("This will print.")
    sys.exit("Exiting with an error message.")  # Prints message to stderr and exits with status 1

if __name__ == '__main__':
    main()
