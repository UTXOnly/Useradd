#!/bin/bash

#Change to home directory and make folders for each group
cd /home
mkdir Admins_folder
mkdir Dev_folder
mkdir Staff_folder
mkdir Temp_folder

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
