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
    name= ''
    id= ''
    grade= ''
    getCourses= []
    getGrades= []
    # properties should be listed first

    def __init__(self, name, id, grade): # You will need to create your own input parameters for all methods
        self.name = name
        self.id = id
        self.grade = grade


    def __del__(self):
        #idk what to put here
        pass

    def average(self):

        self.gradeList.sort()
        numgrades= self.gradeList.count()
        numgrades= numgrades(int)
        a= self.gradelist[0]
        b= self.gradeList[1]
        c= self.gradeList[2]
        d= self.gradeList[3]
        e= self.gradeList[4]
        f= self.gradeList[5]
        g= self.gradeList[6]
        h= self.gradeList[7]
        i= self.gradeList[8]
        j= self.gradeList[9]
        K= self.gradeList[10]
        l= self.gradeList[11]
        m= self.gradeList[12]

        answer1= a+b+c+d+e+f+g+h+i+j+k+l+m
        answer2= answer1/numgrades
        return answer2
        print("The average of the studnets top five grades is"+ answer2)

    def getHonorRoll(self):
        self.gradeList.sort()
        a= self.gradeList[-1]
        a= a(int)
        b= self.gradeList[-2]
        b= b(int)
        c= self.gradeList[-3]
        c= c(int)
        d= self.gradeList[-4]
        d= d(int)
        e= self.gradeList[-5]
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
            return False

        else:
            return False

    def getCourses(self, courseList):
        self.getCourses= courseList
    

    def getGrades(self, gradeList):
        self.getGrades= gradeList
        
        # gradeList is a list of all the grades


    def showCourses(self, courseList):
        print(self.courseList)


    def showGrade(self):
        z= input("Enter a class")
        z= z(int)
        x= self.courseList.index(z)
        print("Class is," + self.courseList[x]+ '' + "and the grade in that class is," + self.gradeList[x])

        



def main():
    # This contains test data that will be used by the autograder.
    # do not modify this function

    st1 = student("Anita Bath","91334",11)
    st1.getCourses( ["English","Math","PE","Computers","History","Biology","Japanese"] )
    st1.getGrades( [91, 94, 87, 99, 82, 100, 73])

    st2 = student("Joe Lunchbox","12346",11)
    st2.getCourses( ["English","Math","Physics","Computers","Geography","Chemistry","French"] )
    st2.getGrades( [71, 98, 93, 95, 68, 81, 71])


main()


