# created Email class
class Email:

    def __init__(self,address,subject,contents,has_been_read=False,is_spam=False):
        self.address =address
        self.subject = subject
        self.contents = contents
        self.has_been_read = has_been_read
        self.is_spam = is_spam

    def mark_as_read(self):
        self.has_been_read = True
    
    def mark_as_spam(self):
        self.is_spam = True

#Inbox class 
class Inbox:
    
    def __init__(self):
        # Created an empty list
        self.box = [] 

    # Add an email method
    def new_email(self,address,subject,contents,has_been_read=False,is_spam=False):
        new_email = Email(address,subject,contents,has_been_read, is_spam)
        self.box.append(new_email)
        
    # List messages from  the sender 
    def list_messages_from_sender(self,sender_address):
        i = 0
        for email in self.box:
            if email.address == sender_address:
                print(f"{i}.{email.subject}\n")
                i+= 1

    # Get email from  the sender 
    def get_email(self, sender_address, idx):
        x = 0 
        for email in self.box: 
            if email.address == sender_address: 
                if x == idx:
                    email.mark_as_read()
                    return email
                x += 1
                
    def mark_as_spam(self, sender_address, idx):
        x = 0 
        for email in self.box:
            if email.address == sender_address: 
                if x == idx:
                    # call mark_as_spam from Email to mark as spam
                    email.mark_as_spam() 
                x += 1            
    
    # Getting unread emails 
    def get_unread_emails(self):
        for email in self.box:
            if email.has_been_read == False:
                print(f"{email.subject}\n")
    
    # Getting spam emails 
    def get_spam_emails(self):
        for email in self.box:
            if email.is_spam == True:
                print(f"{email.address},{email.subject},{email.contents},{email.has_been_read},{email.is_spam}\n")

    # Deleting emails
    def delete(self, sender_address, idx):
        x = 0
        for email in self.box:
            if email.address == sender_address:
                if x == idx:
                    self.box.remove(email)
                    break
                x += 1

# An Email Simulation
inbox = Inbox()
inbox.new_email("joshua@gmail.com", "hello", "how are you doing")
inbox.new_email("joshua@gmail.com", "hi", "Howzit my china" )
inbox.new_email("joshua@gmail.com", "hey", "lets meet")
inbox.new_email("joe@gmail.com", "yo buddy","Haven't seen you in awhile")
    
user_choice = ""

while True:
    usage_message = """
    Welcome to the email system! What would you like to do?

    s - send email.
    l - list emails from a sender.
    r - read email.
    m - mark email as spam.
    gu - get unread emails.
    gs - get spam emails.
    d - delete email.
    e - exit this program.
    """
    user_choice = input(usage_message).strip().lower()
    
    if user_choice == "s":
        # Sending an email 
        sender_address = input("enter the address of the sender\n:")
        subject = input(" enter the subject of the email\n:")
        contents = input(" enter the contents of the email\n:")
        inbox.new_email(sender_address, subject, contents)
        print("Email has been added to inbox.")
        
    elif user_choice == "l":
        # List all emails from the sender
        sender_address = input(" enter the address of the sender\n:")
        inbox.list_messages_from_sender(sender_address)
        
    elif user_choice == "r":
        # Read an email from sender
        sender_address = input(" enter the address of the sender of the email\n:")
        inbox.list_messages_from_sender(sender_address)
        email_idx = int(input(" enter the number of the email that you want to read\n:"))
        email = inbox.get_email(sender_address, email_idx)
        print(f"""{email.address} {email.subject} {email.contents}""")
        
    elif user_choice == "m":
        # Mark an email from a sender at a specific index as spam
        sender_address = input(" enter the address of the sender of the email\n:")
        inbox.list_messages_from_sender(sender_address)
        email_idx = int(input(" enter the number of the email to be marked as spam\n"))
        inbox.mark_as_spam(sender_address, email_idx)
        print("Email has been marked as spam")
    
    elif user_choice == "gu":
        # List of all unread emails 
        inbox.get_unread_emails()
    
    elif user_choice == "gs":
        # List of all spam emails
        inbox.get_spam_emails()
        
    elif user_choice == "e":
        print("Goodbye")
        break
    
    elif user_choice == "d":
        # Deleting an email from a  specific sender 
        sender_address = input("enter the address of the sender  email\n:")
        inbox.list_messages_from_sender(sender_address)
        index = int(input("enter the number of the email you want to delete \n:"))
        inbox.delete(sender_address, index)
        print("Email has been deleted")
        
    else:
        print("Oops - incorrect input")