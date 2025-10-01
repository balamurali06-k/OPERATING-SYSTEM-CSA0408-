import os

def copy_file():
    # Ask user for file names
    source = input("Enter source file name or path: ")
    destination = input("Enter destination file name or path: ")

    # Check if source file exists
    if os.path.exists(source):
        try:
            with open(source, 'r') as src, open(destination, 'w') as dest:
                for line in src:
                    dest.write(line)
            print("File copied successfully!")
        except IOError:
            print("Error occurred while reading or writing files.")
    else:
        print(f"Source file '{source}' not found.")

# Run the program
copy_file()
