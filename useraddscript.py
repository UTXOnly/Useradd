#AddUser Script

#Import os module for python to pass commands to our operating system from our python script
import os

# Open text files and make their contents readable
imported_file_1 = open("listofnames2.txt","r")
imported_file_2 = open("listofnames1.txt","r")

# Create a class for employees to store all their data in objects
class Employees:
    def __init__(self, first, last, group):
        self.firstname = first
        self.lastname = last
        self.group = group
        self.user_id = self.firstname[0]+"."+self.lastname[0:4]

    def __str__(self):
        return '{}-{}'.format(self.user_id,self.group)
        
        

# Declare and initiialize counter variable
i = 0

# Decalre and initialize lists to seperate employees by group
list_of_names = []
admins = []
developers = []
staff = []
temp = []
list_of_user_obj = []

# Iterate through each line of imported text file objects and append each line into our master list of names
for lines in imported_file_1:
    list_of_names.append(lines.upper())
for lines in imported_file_2:
    list_of_names.append(lines.upper())

# Define a function to create new users based on which group they belong to

def createuser(firstname,lastname,group):
    
    name = Employees(firstname,lastname,group)
    list_of_user_obj.append(name)

    # Create an admin user, add them to the admin and sudo group, set password, do not create group for user, set username to the user ID created
    if name.group == 'admin':
        print('added',name.user_id)
        os.system("useradd -m -G cis245admins,sudo -p changeme -N "+ name.user_id)
    # Create developer user, add to developers group, change default shell to C shell,set password, do not create group for user, set username to user ID created
    if name.group == 'developer':
        print('added',name.user_id)
        os.system("useradd -m -G cis245developers -s /bin/csh -p changeme -N "+ name.user_id)
    # Create staff user, add to staff group, set password, do not create group for user, set username to user ID created
    if name.group == 'staff':
        print('added',name.user_id)
        os.system("useradd -m -G cis245staff -p changeme -N "+ name.user_id)
    # Create temp user, add to temp group, set password, set username to user ID created
    if name.group == 'temp':
        print('added',name.user_id)
        os.system("useradd -m -G cis245tempemps -p changeme -N "+ name.user_id)

# A function to delete all users. This was helpful when testing and troubleshooting my script.
def delete_all_users():
    for user in list_of_user_obj:
        os.system("deluser --remove-home "+ user.user_id)


# Iterate through list of names to seperate them into groups based on their position on the list.
for names in list_of_names :
    
    if i <= 20:
        admins.append(names)
    if i > 20 and i <= 40:
        developers.append(names)
    if i > 40 and i <= 100:
        staff.append(names)
    if i > 100:
        temp.append(names)
    i += 1

# Iterate through list of admins create a new user for each entry
for admin in admins:
    splitad = admin.split()
    firstname = splitad[0]
    lastname = splitad[-1]
    group = 'admin'
    
    createuser(firstname,lastname, group)

# Iterate through list of developers create a new user for each entry
for developer in developers:
    splitdev = developer.split()
    firstname = splitdev[0]
    lastname = splitdev[-1]
    group = 'developer'
    createuser(firstname,lastname, group)

# Iterate through list of staff create a new user for each entry
for staff in staff:
    splitstaff = staff.split()
    firstname = splitstaff[0]
    lastname = splitstaff[-1]
    group = 'staff'
    createuser(firstname,lastname, group)

# Iterate through list of temps create a new user for each entry
for temp in temp:
    if temp != '':
        splittemp = temp.split() 
        firstname = splittemp[0]
        lastname = splittemp[-1]
        group = 'temp'
        createuser(firstname,lastname, group) 
        


#delete_all_users()

    
    
