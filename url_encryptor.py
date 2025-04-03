from cryptography.fernet import Fernet
import sys
from os import remove

path_of_file = "encrypted.txt"


def encrypt_msg():
    key = Fernet.generate_key() # Creating a fernet key to encrypt
    fernet_object = Fernet(key)
    # Encoding the user input into a byte string using .encode() as .encrypt() accpets onlyl byte string
    message = fernet_object.encrypt(input("Enter the message you want to encrypt: ").encode()) 

    with open(path_of_file, "a") as file:
        file.write(f"{key.decode()} {message.decode()}\n") # Storing the key amn message decoded. Helps in formatting the input string while decrypting messages


def decrypt_msg():
    with open(path_of_file, "r") as file:
        for i, line in enumerate(file, start=1):
            key, message = line.split() # Split the line in file at a whitespace as the key and encrypted message aer stored with a whitespace between them

            fernet_object = Fernet(key.encode()) # Encoding the key into byte string format
            print(f"{i}. {fernet_object.decrypt(message).decode()}") # Encoding the message into byte string format


def remove_msg():
    decrypt_msg() # To display the list of currently present lines

    with open(path_of_file, "r+") as file: # Using "r+" mode to both read and write from the file
        lines_from_file = file.readlines() # Create a list of lines in the file

        line_num = int(input("Enter the serial number of the line/message you want to remove: ")) # Get the line no. to be removed
        del lines_from_file[line_num - 1] # Remove the specific line from the list of lines

        file.seek(0) # Place the cursor at the beginning of the file to truncate it.
        file.truncate()
        file.writelines(lines_from_file) # Write the new lines from the modified list of lines
    
    print("Line/mesasge successfully removed from the file.")


def file_path():
    print(f"The file containing the encrypted messages are stored at: {path_of_file}")


def file_delete():
    try:
        choice = input("Are you sure you want to peranently delete the file? (y / n)?") # Confirmation message

        if choice.lower().strip() == "y":
            remove(path_of_file)
            print("File successfully removed")
        elif choice.lower().strip() == "n":
            print("User Cancelled Deletion of File")
            exit(0)
        else:
            print("Wrong command, retry.")

    except Exception as e:
        print("Error: {e}")


def help_txt():
    help_txt = ("""
--encrypt - Allows you to encrypt a message and store it in a file
--decrypt - Allows you to decrypt all messages form the file and display it
--remove  - Removes the user specified message from the file
--filepath    - Displays the path of the file which stores the encrypted messages
--delete  - Deletes the file which stores the encrypted message
--help    - Displays the list of valid commands and their function (you're reading it right now)
""")
    print(help_txt)


def main():
    match sys.argv[1]: # Using sys.argv[] to access argv
        case "--encrypt":
            encrypt_msg()
        case "--decrypt":
            decrypt_msg()
        case "--remove":
            remove_msg()
        case "--filepath":
            file_path()
        case "--delete":
            file_delete()
        case "--help":
            help_txt()
        case _:
            print("Invalid command !! Type '--help' to get a list of valid commands.")


if __name__ == '__main__':
    main()
