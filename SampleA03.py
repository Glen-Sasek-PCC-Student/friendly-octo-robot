#******************************************************************************
# Author:           Gayathri Iyer
# Assignment:       A03 Sample
# Date:             Sep 22, 2022
# Description:      This program is a sample for Assignment 3.  It is a program with parallel arrays for Stem Majors and their Salaries. 
# Input:            Stem Major names and Salaries
# Output:           The Major with the largest salary and the Major with the lowest salary.
# Sources:          None.
#******************************************************************************

# main function
def main():
  major = []
  salary = []
  flag = 'error'
  #call the welcome function
  welcome()
  option = 'y'
  while(option != 'n'):
    flag = 'error'
    majorName = input("Enter major name: ")
    major.append(majorName)
    majorSalary = input("Enter major salary: ")
    while(flag == 'error'):
      try:
        majorSalary = int(majorSalary)
      except ValueError:
        flag = 'error'
        majorSalary = input("Invalid Salary!! Enter major salary: ")
      else:
        if(majorSalary <= 0 ):
          flag = 'error'
          majorSalary = input("Invalid Salary!! Enter major salary: ")
        else:
          flag = 'good'
    salary.append(majorSalary)
    option = input("Do you want to add more? (y/n) ")
  #to do some data analysis
  max = salary[0]
  majorMaxName = major[0]
  min = salary[0]
  majorMinName = major[0]
  print(salary)
  print(major)
  for x in range(len(salary)):
    if(max < salary[x]):
      max = salary[x]
      majorMaxName = major[x]
    if (min > salary[x]):
      min = salary[x]
      majorMinName = major[x]
      
  print("Highest salary is: $", max, " and the major is ", majorMaxName, sep = '')
  print("Lowest salary is: $", min, " and the major name is ", majorMinName, sep = '')

#displays a welcome message to the user
def welcome():
  print("Welcome to my STEM salary comparison program.")
  print("Enter a list of major names and salary when prompted.")
  print("The program will display the major with the highest salary and the major with the lowest salary.")

main()
