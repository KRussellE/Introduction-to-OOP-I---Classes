import re

print("\033[0;32m\n\t\t\tEMAIL\033[0;37m\n")

# a class definition for an Email
class Email:

    #  class definition for an Email which has four variables: has_been_read, email_contents, is_spam and from_address.
    def __init__(self,from_address, email_contents):
        self.from_address = from_address
        self.email_contents = email_contents
        self.has_been_read = False
        self.is_spam = False

    # This function changes "has_been_read" variable from false to true
    def mark_as_read(self):
        self.has_been_read = True

    # This function allows us to print the email, especially when the user wants to read
    def __str__(self):
        return f"From: {self.from_address} \nContent: {self.email_contents} "

    # This function changes "is_spam" variable from false to true
    def mark_as_spam(self):
        self.is_spam = True

# This variable store user input, the choice they choose from the menu
user_choice = ""

inbox = []
spam = []
def add_email(message, email):      # takes in the contents and email address from the received email to make a new Email object
    send = Email(email, message)
    inbox.append(send)

# Number of messages in the store are returned via this function
def get_count(inbox):
    return len(inbox)       #  returns the number of messages in the store

# Email content is returned by this function
def get_email(index):           # returns the contents of an email in the list
    message = inbox[index]
    message.mark_as_read()      # this has been done, has_been_read will now be true.
    print(message)
    

def add_spam(index):
    messages = inbox[index]
    inbox.remove(inbox[index])
    messages.mark_as_spam()
    print("Email added to spam")

# Non read emails from the list are returned via this function
def get_unread_emails():
    messages =[]
    for n, i in enumerate(inbox):
        if not i.has_been_read:
            message = inbox[n]
            messages.append(message)
            print(message)
            print(message.email_contents)   # will return a list of all the emails that haven’t been read
            return messages     

# This function returns a list of all the emails that have been marked as a spam
def get_spam_emails():
    print()
    messages =[]
    for n, i in enumerate(inbox):
        if not i.is_spam:
            message = inbox[n]
            messages.append(message)
            print(f"Spam: {message.email_contents}")    # will return a list of all the emails that have been marked as spam.
            return messages     

# Delete function deletes an email from the inbox
def delete(index):
    try:
        inbox.remove(inbox[index])
        print("\033[0;31mEmail deleted successfully\033[0;37m")
    except:
        print("\033[0;31mError: couldn't delete email\033[0;37m")
            
# Initial email
init_emails = [
'Hi I will be leaving work later than usual,roxi456@googlemail.com',
'Hi please take the dogs for a walk,Marvinthemartian@space.com'
]

for i in init_emails:
    message, email = i.split(',')
    add_email(message,email)

#This is the menu the user will be prompted to enter a choice
while user_choice != "quit":
    user_choice = input("\n\033[0;32mWhat would you like to do?\tread\n\t\t\t\tmark spam\n\t\t\t\tsend\n\t\t\t\tdelete\n\t\t\t\tquit\n\033[0;37m").lower()
    if user_choice == "read":       # If user chooses read then this if will run.
        if get_count(inbox) != 0:
            print("\n\t\t\033[0;33mList of unread email\033[0;37m\n")
            for y in range (0, get_count(inbox)):       # First of all the user will see all of their emails and contents
                print(f"{y+1}. {inbox[y]}")
            
            while True:
                try:
                    num = int(input("\n\033[0;33mEnter number of email you want to read: \033[0;37m"))  # The program will ask the user to type the number of the email that they want to read.
                    if num > get_count(inbox):
                        print("\033[0;31mError: you do not have so many emails.\033[0;37m")     # The get_count(inbox) function tells the total number of emails. 
                        #If the user enteres a larger number than emails exists then the program will send an error message to them.
                    elif num <= 0:
                        print("\033[0;31mError: you entered invalid number.\033[0;37m") # if the user types 0 or less than zero than the program will send a message because the user can not read a not existing email.
                    else:
                        print("\n")
                        
                        get_email(num-1)    # By the get_count function the program will print out the right email and content on the screen.
                        
                        inbox.remove(inbox[num-1])
                        False
                        break
                except ValueError:
                    print("You entered invalid number.")    # If the user types not an integer number, the program will send this message.
        else:
            print("\033[0;31mError: You do not have any unread email\033[0;37m")
    elif user_choice == "mark spam":
        if get_count(inbox) != 0:
            print("\n\t\t\033[0;33mList of unread emails\033[0;37m\n")
            for y in range (0, get_count(inbox)):        # First of all the user will see all of their emails and contents
                print(f"{y+1}. {inbox[y]}")
            x = get_count(inbox)
            while True:
                try:
                    num = int(input("\n\033[0;33mEnter number of email you want to spam: \033[0;37m"))  # The program will ask the user to type the number of the email what they want to mark spam.
                    if num > get_count(inbox):
                        print("\033[0;31mError: you do not have so many emails.\033[0;37m") # The get_count(inbox) function tells the total number of emails. If the user entered larger number than email exists then the program will send an error message to them.
                    elif num <= 0:
                        print("\033[0;31mError: you entered invalid number.\033[0;37m") # if the user type 0 or less than zero than the program will send a message because the user can not read a not existing email.
                    else:
                        add_spam(num-1)     # The program will add the right email to the spam by the add_spam function.
                        get_spam_emails()   # The program will print out the email what just got set as spam.
                        False
                        break
                except ValueError:
                    print("You entered invalid number.")    # If the user types not an integer number, the program will send this message.
        else:
            print("\033[0;31mError: You do not have any unread email\033[0;37m")
    elif user_choice == "send":
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'      # I created a variable called regex what stores the datas what need to be check if the user will type valid email at the from_address variable
        while True:
            from_address = input("\n\033[0;33mEnter your email address: \033[0;37m")       # Program asks the user to type an email address and will store it into a variable called from_address.
            if(re.fullmatch(regex, from_address)):  # If the email is fully match with the regex variable then the email is valid
                email_contents = input("\033[0;33mEnter email content: \033[0;37m")     # The program will asks the user to type the content of the email.
                add_email(email_contents, from_address)     # By the add_email function the email will be added to the inbox.
                print("\033[0;31mEmail sent successfully!\033[0;37m")       # Finally the program will send a message that the email sent successfully.
                break
            else:
                print("Invalid Email")  # If the email is not fully match with the regex variable then the email is valid 
    elif user_choice == "delete":
        if get_count(inbox) != 0:
            print("\n\t\t\033[0;33mList of emails\033[0;37m\n")
            for y in range (0, get_count(inbox)):        # First of all the user will see all of their letters (emails and contents)
                print(f"{y+1}. {inbox[y]}")
            while True:
                try:
                    num = int(input("\n\033[0;33mEnter number of email to delete: \033[0;37m")) # The program will ask the user to type the number of the email what they want to delete.
                    if num > get_count(inbox):
                        print("\033[0;31mError: you do not have so many emails.\033[0;37m") # The get_count(inbox) function tells the total number of emails. If the user entered larger number than email exists then the program will send an error message to them.
                    elif num <= 0:
                        print("\033[0;31mError: you entered invalid number.\033[0;37m") # if the user type 0 or less than zero than the program will send a message because the user can not read a non existing email.
                    else:
                        delete(num-1)   # by the delete function the program will delete the right email.
                        False
                        break
                except ValueError:
                    print("You entered invalid number.")    # If the user types a non integer number, the program will send this message.
        else:
            print("\033[0;31mError: You do not have any email\033[0;37m")
    elif user_choice == "quit":
        print("\033[0;33mGoodbye\033[0;37m")
        exit()
    else:
        print("Oops - incorrect input")
