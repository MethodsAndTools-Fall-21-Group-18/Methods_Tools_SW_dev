# Methods_And_Tools_Project
Project Overview
Introduction
Each CSE 2213 will participate in a group project. Groups will be 4-5 students (depending on class size).

Guidelines:
Projects may be in C++ or Python
Projects must be hosted on GitHub or GitLab
Each member must contribute through their own account, don't just have a master Group account as that doesn't show push data
Projects must be able to store data while the program isn't running
Groups have a choice on how this is done -- through Databases or external files
 

Requirements
Your job is to create a command-line e-commerce store. Your user must be able to login or create an account once the system begins. They cannot proceed without logging in, so make sure wrong choices are accounted for and there's a choice for them to quit if they don't want to log in. Only one user type need be accounted for (specifically, a customer).

Once logged in, your user needs to be able to interact with all the items, shop, and manage their account.

Here are the specific requirements once logged in:

Items
View all items in a category
View all items in the user's shopping cart
Add item from a category to their shopping cart
Remove an item from their shopping cart
Checkout the items currently in their cart
Removes items from the user's shopping cart
Edits stock information to lower the stock accordingly
Add an order to the user's order history
View the logged in user's order history
Edit the user's account
Edit the shipping information
Edit the payment information
Delete their account (and all the order history/shopping cart data associated with it)
Logout
 

Each 4-person group will have one category of inventory item (or their choice), while each 5-person group will have two categories of inventory items (of their choice). Make sure the inventory item(s) is well-rounded and has information relevant to being an inventory item (such as price and stock number, etc) and relevant to the item itself.

For 5-person groups: Assume each category of item would be handled independently. So, if you had books and movies as your two item categories you'd have the following for requirements:

View all books
Add book to cart
Remove book from cart
View all movies
Add movie to cart
Remove movie from cart
Checkout everything in cart
...etc
 
 
 
Design Assignment (due November 12 at 11:59pm)
Your project is required to have 4 classes (5 for 5-person groups). You'll also have a driver (main function) that will utilize all of your classes.

First, what classes are you going to have a why? Then, design a UML Detailed Class Diagram for each of your classes, making sure you account for all data/functions you believe will go into the project. Make sure you have a section that details what the functions are going to do and why they're present.

Second, you're going to have a good bit of menuing since this is a command-line environment. Design what this menuing would look like. What's the menu like when someone isn't logged in? Once they are logged in? Are there categories with nested menus? What general idea are you going for as far as navigation goes?

Finally, how are you going to store data? In a database? In individual text files? If files, what format are you going to put your data in?

** the only input/output to the screen should be handled in the driver, make sure you account for this in your design!

 

A sample document (along with a couple of required questions) can be found here: designBeginning.docx  Download designBeginning.docx 

Deliverables:

A PDF containing your groups design
 

Coding Assignment (due December 1 at 11:59pm)
Implement your group's design in the programming language of choice. Make sure you're implementing all the given requirements and showing all iterations on the proper Git repo.

Create a starting set of data (a preset number of users, inventory stock, etc). Then, in a screen recording, show a sample workflow. Make sure all requirements are shown.

 

Deliverables:

Video screen recording
.mkv, .mov, .mp4
Compressed folder containing all of your code
Your base files if you used files for information storage
 

Final Report (due December 1 at 11:59pm)
Along with their code, each group will be required to submit a final report associated with their project. Questions and formatting can be found here: finalReport-sample.docx  Download finalReport-sample.docx 

 

Deliverables:

A PDF containing the group's final report
 

 

 

Peer Reviews
Peer reviews will be given at the end of the project. Students are required to review their group members. Failure to submit a peer review will result in a 10-point deduction on the student's personal group project grade. Information on these will be posted later.
 
 
 
