#!/usr/bin/env python
#*******************************************************************************
#msh_ang_deg_rad.py
#*******************************************************************************

#Purpose:
#Given a CSV file containing unique identifiers and corresponding angles in
#degrees, this program creates a new csv file containing the same identifiers
#and the angles converted to radians.
#Author:
#Cedric H. David, 2019-2019


#*******************************************************************************
#Import Python modules
#*******************************************************************************
import sys
import csv
import math


#*******************************************************************************
#Declaration of variables (given as command line arguments)
#*******************************************************************************
# 1 - msh_deg_csv
# 2 - msh_rad_csv


#*******************************************************************************
#Get command line arguments
#*******************************************************************************
IS_arg=len(sys.argv)
if IS_arg != 3:
     print('ERROR - 2 and only 2 arguments can be used')
     raise SystemExit(22) 

msh_deg_csv=sys.argv[1]
msh_rad_csv=sys.argv[2]


#*******************************************************************************
#Print input information
#*******************************************************************************
print('Command line inputs')
print('- '+msh_deg_csv)
print('- '+msh_rad_csv)


#*******************************************************************************
#Check if files exist 
#*******************************************************************************
try:
     with open(msh_deg_csv) as file:
          pass
except IOError as e:
     print('ERROR - Unable to open '+msh_deg_csv)
     raise SystemExit(22) 


#*******************************************************************************
#Reading input file
#*******************************************************************************
print('Reading input file')

IV_ang_tot_id=[]
ZV_ang_tot_dg=[]
with open(msh_deg_csv,'rb') as csvfile:
     csvreader=csv.reader(csvfile)
     next(csvreader)
     for row in csvreader:
          IV_ang_tot_id.append(int(row[0]))
          ZV_ang_tot_dg.append(float(row[1]))

IS_ang_tot=len(IV_ang_tot_id)
print('- There are '+str(IS_ang_tot)+' angles')


#*******************************************************************************
#Converting angles
#*******************************************************************************
print('Converting angles')

ZV_ang_tot_rd=[-9999]*IS_ang_tot
for JS_ang_tot in range(IS_ang_tot):
     ZV_ang_tot_rd[JS_ang_tot]=math.radians(ZV_ang_tot_dg[JS_ang_tot])

print('- Done')


#*******************************************************************************
#Writing output file
#*******************************************************************************
print('Writing output file')

with open(msh_rad_csv, 'wb') as csvfile:
     csvwriter = csv.writer(csvfile, dialect='excel')
     csvwriter.writerow(['station_id', 'angle_radians'])
     for JS_ang_tot in range(IS_ang_tot):
          csvwriter.writerow([IV_ang_tot_id[JS_ang_tot],                       \
                              ZV_ang_tot_rd[JS_ang_tot]]) 

print('- Done')


#*******************************************************************************
#End
#*******************************************************************************
