# Introduction-to-OOP-I---Classes

In this task, we’re going to be simulating an email message. Some of the logic has
been filled out for you in the email.py file.

  ● Open the file called email.py.
  ● Create a class definition for an Email which has four variables:
  has_been_read, email_contents, is_spam and from_address.
  ● The constructor should initialise the sender’s email address.
  ● The constructor should also initialise has_been_read and is_spam to false.
  ● Create a function in this class called mark_as_read which should change
  has_been_read to true.
  ● Create a function in this class called mark_as_spam which should change
  is_spam to true.
  ● Create a list called inbox to store all emails (note that you can have a list of
  objects).
  ● Then create the following functions:
      ○ add_email - which takes in the contents and email address from the
      received email to make a new Email object.
      ○ get_count - returns the number of messages in the store.
      ○ get_email - returns the contents of an email in the list. For this, allow
      the user to input an index i.e. get_email(i) returns the email stored
      at position i in the list. Once this has been done, has_been_read
      should now be true.
      ○ get_unread_emails - should return a list of all the emails that haven’t
      been read.
      ○ get_spam_emails - should return a list of all the emails that have been
      marked as spam.
      ○ delete - deletes an email in the inbox.
      Now that you have these set up, let’s get everything working!
  ● Fill in the rest of the logic for what should happen when the user inputs
  send/read/quit etc. so that all of the functions are utilised.. Some of it has
  been done for you.
