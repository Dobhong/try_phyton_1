#printstatements
print("hello world")

#varible and datatypo
name= "aldo"
age= 25
height= 5.9
is_student= True
print(name, age, height, is_student)

#if-else_statement
age= 20
if age >= 18:
    print("you are an adult")
else:
    print("you are an young person")

#loop
for i in range(5):
    print(i)

#while loop
count = 4
while count < 5:
    print(count)
    count += 1

#fucntion
def greet(name):
    print(f"hello, {name}!")

greet("aldo")

#list
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
fruits.append("orange") #tabahanlist
list
print(fruits)

#dictionary
person = {"name": "aldo", "age":25}
print(person["name"])
person["height"] = 5.9
print(person)   

#error handling
try:
    result = 10 /0
except ZeroDivisionError:
        print("you cant devide zero division!")

#working with files
with open("example.txt","w") as file:
     file.write("hello world")
with open("example.txt","r") as file:
     content = file.read()
     print(content)

#library and modules
import math
print(math.sqrt(16))

#oop
class Dog:
     def __init__(self,name, breed):
          self.name = name
          self.breed = breed
     def bark(self):
         print(F"{self.name} says woof!")
my_dog = Dog("buddy", "Golden Retriver")
my_dog.bark()

#database_built
#import mysql.connector

#conn = mysql.connector.connect(
 #   host="localhost",
  #  user="root",
 #   password="",
 #   database=""
#)
#cursor = conn.cursor()
#rows = cursor.fetchall()

#for row in rows:
 #   print(row)
#conn.close()

#####################################
#test 1 done (
#database test
#import mysql.connector

#conn = mysql.connector.connect(
#    host="localhost",
#    user="root",
 #   password="",
 #   database="train_phyton"
#)
#cursor = conn.cursor()
#query = "INSERT INTO `train_oop_database` (name) VALUES (%s)"
#values = ('aldo',)


#cursor.execute(query, values)


#conn.commit()

#print(f"Inserted {cursor.rowcount} row(s) into the database.")


#conn.close()
#######################################

#######################################################################
#test 2 oop+database
#import mysql.connector  # Correct module name

#class STUDENT:
 #   def __init__(self, name, age, grade):
  #      self.name = name
   #     self.age = age
    #    self.grade = grade

    #@staticmethod
    #def connect_to_db():
        # Return a connection object with properly assigned values
     #   return mysql.connector.connect(
      #      host="localhost",
       #     user="root",
        #    password="",  # Ensure your MySQL root password is correct
         #   database="train_phyton"
        #)

    #def save(self):
     #   conn = self.connect_to_db()
      #  cursor = conn.cursor()
        # Correct spelling of "query"
       # query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
        #values = (self.name, self.age, self.grade)
        #try:
         #   cursor.execute(query, values)
          #  conn.commit()  # Commit the transaction
           # print(f"Student '{self.name}' added successfully!")
       # except mysql.connector.Error as err:
       #     print(f"Error: {err}")
       # finally:
       #     conn.close()  # Close the connection

    #@staticmethod
    #def fetch_all():
     #   conn = STUDENT.connect_to_db()
      #  cursor = conn.cursor()
       # query = "SELECT * FROM students"
        #try:
        #    cursor.execute(query)
         #   rows = cursor.fetchall()
          #  for row in rows:
           #     print(row)
       # except mysql.connector.Error as err:
        #    print(f"Error: {err}")
       # finally:
        #    conn.close()  # Close the connection


# Single input to gather all student details
#def add_student():
 #   user_input = input("Enter student details (name, age, grade) separated by commas: ")
  #  try:
   #     # Parse the input
    #    name, age, grade = map(str.strip, user_input.split(","))
     #   student = STUDENT(name, int(age), grade)
      #  student.save()
   # except ValueError:
    #    print("Invalid input format. Please enter details as 'name, age, grade'.")


# Example usage
#if __name__ == "__main__":
 #   while True:
  #      print("\n1. Add Student")
   #     print("2. View All Students")
    #    print("3. Exit")
     #   choice = input("Enter your choice: ")
        
      #  if choice == "1":
       #     add_student()
       # elif choice == "2":
       #     STUDENT.fetch_all()
       # elif choice == "3":
       #     print("Exiting the program.")
        #    break
       # else:
        #    print("Invalid choice. Please try again.")
#######################################################################

