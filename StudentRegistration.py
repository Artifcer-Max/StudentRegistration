# StudentRegistration.py
# This program processes student details to register them into a course then displays this information onto the console
# Author: Alexander Shepherd
# Date 2/12/2022

import tkinter as tk
from tkinter.simpledialog import askstring, askinteger, askfloat
def print_heading():
  print("---Holmesglen Institue---")
  print("ID\tName\t\tCourse\t\tFee")

def input_student_details():
  ids = askstring('Student Details', 'Input student id: \t\t\t\t')
  names = askstring('Student Details', 'Input student first and last name: \t\t\t\t')
  courses = askstring('Student Details', "Input student's course: \t\t\t\t")
  fees = askfloat('Student Details', "Input students fees: \t\t\t\t:")
  studentlist = [ids, names, courses, fees]
  return studentlist

def outputTotalFees(totalfees):
  print("Total fees: ${0:,}".format(totalfees))

numofstudents = askinteger('Student Details', "How many students would you like to input?")
i = 0
print_heading()
totalfees = 0
while i < numofstudents:
  studentdets = input_student_details()
  totalfees = totalfees + studentdets[3]
  print("{0}\t{1}\t{2}\t${3:,}".format(studentdets[0], studentdets[1], studentdets[2], studentdets[3]))
  i += 1
outputTotalFees(totalfees)