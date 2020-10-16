#!/bin/bash

cd /etc/skel

mkdir AdminSKEL
mkdir DevSKEL
mkdir StaffSKEL
mkdir TempSKEL

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
