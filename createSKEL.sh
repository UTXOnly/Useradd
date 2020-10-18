#!/bin/bash

#add groups

addgroup cis245admins
addgroup cis245developers
addgroup cis245staff
addgroup cis245tempemps

# Uncomment this section if you are running this script on CentOS

#groupadd cis245admins
#groupadd cis245developers
#groupadd cis245staff
#groupadd cis245tempemps


#Change to home directory and make folders for each group
cd /home
mkdir Admins_folder
chgrp cis245admins Admins_folder
chmod 660 Admins_folder
mkdir Dev_folder
chgrp cis245developers Dev_folder
chmod 660 Dev_folder
mkdir Staff_folder
chgrp cis245staff Staff_folder
chmod 660 Staff_folder
mkdir Temp_folder
chgrp cis245tempemps Temp_folder
chmod 660 Temp_folder
mkdir company_public_folder
chmod 444 company_public_folder

#Change directories and create skeleton directories for each group
cd /etc/skel

mkdir AdminSKEL
mkdir DevSKEL
mkdir StaffSKEL
mkdir TempSKEL

#Add company policy documents to each employees skeleton directory
cd AdminSKEL
touch General_Policy.txt
touch Admin_Policy.txt
cd ..
cd DevSKEL
touch General_Policy.txt
touch Dev_Policy.txt
cd ..
cd StaffSKEL
touch General_Policy.txt
touch Staff_policy.txt
cd ..
cd TempSKEL
touch General_Policy.txt
touch Temp_policy.txt
