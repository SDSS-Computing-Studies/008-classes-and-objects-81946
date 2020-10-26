#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grade - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:

    # properties should be listed first

    def __init__(name, id, grade, courses, grades): # You will need to create your own input parameters for all methods
        self.name = name
        self.id = id
        self.grade = grade
        self.courses = courses
        self.grades = grades

    def __del__(self):
        pass
        print('')
        print("The student fell into a blackhole... oops.")
        print('')

    def average(self):

        gradeList.sort()
        numgrades= gradeList.count()
        numgrades= numgrades(int)
        a= gradelist[0]
        b= gradeList[1]
        c= gradeList[2]
        d= gradeList[3]
        e= gradeList[4]
        f= gradeList[5]
        g= gradeList[6]
        h= gradeList[7]
        i= gradeList[8]
        j= gradeList[9]
        K= gradeList[10]
        l= gradeList[11]
        m= gradeList[12]

        answer1= a+b+c+d+e+f+g+h+i+j+k+l+m
        answer2= answer1/numgrades
        print("The average of the studnets top five grades is"+ answer2)

    def getHonorRoll(self):
        gradeList.sort()
        a= gradeList[-1]
        a= a(int)
        b= gradeList[-2]
        b= b(int)
        c= gradeList[-3]
        c= c(int)
        d= gradeList[-4]
        d= d(int)
        e= gradeList[-5]
        e= e(int)
        answer1= a+b+c+d+e
        answer2= answer/5
        if answer2>86 or answer2==86:
            print('')
            print("You are in HonourRoll!")
            print('')
            return True

        if answer2<86:
            print('')
            print("You are not in HonourRoll")
            print('')
            return false

    def getCourses(self, courseList):
        courseList= getCourses

    def getGrades(self,gradeList ):
        gradeList= getGrades
        # gradeList is a list of all the grades


    def showCourses(self, courseList):
        print(courseList)


    def showGrade(self):
        z= input("Enter a class")
        z= z(int)
        x= courseList.index(z)
        print("Class is," + courseList[x]+ '' + "and the grade in that class is," + gradeList[x])

        



def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346", 11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])




main()
