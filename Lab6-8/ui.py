from service import *
from undocontroller import *
from tests import *
class UI:
    def __init__(self,service,undoRedo):
        self._service=service
        self.undoRedo=undoRedo
    def printMenu(self):
        print('')
        print('Menu: ')
        print('1.Manage student or assignment')
        print('2.Give assignment')
        print('3.Grade student')
        print('4.Statistics')
        print("5.Undo")
        print('6.Redo')
        print('0.Exit')

    def printManageStud(self):
        print('')
        print('1.Add')
        print('2.Remove')
        print('3.Update name')
        print('4.Update group')
        print('5.List')

    def printManageAssign(self):
        print('')
        print('1.Add')
        print('2.Remove')
        print('3.Update description')
        print('4.Update deadline')
        print('5.List')

    def printGive(self):
        print('')
        print('1. Give an assignment to a student')
        print('2. Give an assignment to a group of students')

    def printStatistic(self):
        print('')
        print('1.List students with their assignments')
        print('2.List all students who received a given assignment, ordered by average grade for that assignment.')
        print('3.List all students who are late in handing in at least one assignment')
        print('4.List students with the best school situation')

    def addStud(self):
        id=input("Insert the ID for the new student: ")
        name=input("Insert the name of the new student: ")
        group=input("Insert the group of the new student: ")
        try:
            s.service_addS(id,name,group)
        except Exception as E:
            print(str(E))
    def removeStud(self):
        id=input("Insert the ID of the student you want to remove:")
        try:
            s.service_removeS(id)
        except  Exception as x:
            print(str(x))
    def updateStudName(self):
        id=input("Insert the Id of the student you want to update:")
        name=input("Insert the new name of the student: ")
        try:
            s.service_updaten(id,name)
        except  Exception as x:
            print(str(x))
    def updateStudGroup(self):
        id=input("Insert the Id of the student you want to update:")
        group=input("Insert the new group of the student: ")
        try:
            s.service_updateg(id,group)
        except  Exception as x:
            print(str(x))

    def addAssign(self):
        id=input("Insert the Id for the new assignment: ")
        desc=input("Insert the description of the new assignment: ")
        dead=input("Insert the deadline of the new assignment")
        try:
            s.service_addA(id,desc,dead)
        except Exception as E:
            print(str(E))
    def removeAssign(self):
        id=input("Insert the Id of the assignment you want to remove:")
        try:
            s.service_removeA(id)
        except  Exception as x:
            print(str(x))
    def updateAssignDesc(self):
        id=input("Insert the Id of the assignment you want to update:")
        desc=input("Insert the new description for the assignment: ")
        try:
            s.service_updatedesc(id,desc)
        except  Exception as x:
            print(str(x))
    def updateAssignDeadline(self):
        id=input("Insert the Id of the assignment you want to update:")
        dead=input("Insert the new deadline for the assignment: ")
        try:
            s.service_updatedead(id,dead)
        except  Exception as x:
            print(str(x))
    def giveStud(self):
        id1=input('Insert the id of the assignment you want to give ')
        id2 = input('Insert the id of the student you want to receive the assignment ')
        try:
            s.givestud(id1,id2)
        except Exception as x:
            print(str(x))
    def giveGroup(self):
        id=input('Insert the id of the assignment you want to give ')
        gr=input('Insert the group that you want to receive the assignment')
        try:
            s.givegroup(id,gr)
        except Exception as x:
            print(str(x))
    def grade(self):
        ids=input("Insert the id of the student you want to grade")
        ida=input('Insert the id of the assignment you are giving a grade to')
        gr=input('Insert the grade ')
        try:
            s.service_gradestud(ids,ida,gr)
        except Exception as x:
            print(str(x))
    def listStudGrade(self):
        ida=input('Insert the id of the assignment')
        try:
            v=(s.service_liststud(ida))
            print('The list of students sorted by their grade on assignment:'+ida)
            print('')
            for i in v:
                print(str(i))

        except Exception as x:
            print(str(x))
    def listLate(self):
        week=input('Insert the current week: ')
        try:
            v=(s.service_late(week))
            print("The list with students that are late with at least one of their assignments")
            for i in v:
                print(i)
        except Exception as x:
            print(str(x))
    def listBest(self):
        try:
            r=s.service_best()
            print("The students sorted in descending order by average grade")
            for i in r:
                print(str(i))
        except Exception as x:
            print(str(x))
    '''
    def randfunct(self):
        cmd=[self.addStud,self.removeStud,self.updateStudName,self.updateg_ui,
             self.adda_ui,self.aremove_ui,self.updatedesc_ui,self.updatedead_ui,self.givestud_ui,
             self.givegroup_ui,self.gradestud_ui,self.liststudents_ui,self.late_ui,self.best_ui]

        for i in range(6):
            r = random.randint(0, 13)
            if r==0:
                print("Add a student")
                id = random.randint(11,100)
                name = s.RandomName()
                group = s.RandomGroup()
                try:
                    s.service_addS(id, name, group)
                except Exception as E:
                    print(str(E))
            elif r==1:
                print("Remove a student")
                id = random.randint(0,100)
                try:
                    s.service_removeS(id)
                except Exception as x:
                    print(str(x))
            elif r==2:
                print("Update student name")
            elif r==3:
                print("Update student group")
            elif r==4:
                print("Add an assignment")
            elif r==5:
                print("Remove an assignment")
            elif r==6:
                print("Update assignment description")
            elif r==7:
                print("Update assignment deadline")
            elif r==8:
                print("Give assignment to a student")
            elif r==9:
                print("Give assignment to a group")
            elif r==10:
                print("Grade student")
            elif r==11:
                print("List of students sorted by their grade on a given assignment")
            elif r==12:
                print("List of students who are late on at least one assignment")
            elif r==13:
                print("List of students with the best school situation")
    '''



    def Start(self):
        '''
        s.initS()
        s.initA()
        '''
        while True:
            self.printMenu()
            opt=input("Your option:")
            if opt=='1':
                print('1. Manage students')
                print('2. Manage assignments')
                opt1=input('>')
                if opt1 =='1':
                    self.printManageStud()

                    opt2=input('>')
                    if opt2 =='1':
                        self.addStud()
                    elif opt2=='5':
                        s._students.listS()
                    elif opt2=='2':
                        self.removeStud()
                    elif opt2=='3':
                        self.updateStudName()
                    elif opt2=='4':
                        self.updateStudGroup()
                    else:
                        print("Invalid command")
                elif opt1=='2':
                    self.printManageAssign()
                    opt2 = input('Your option:')
                    if opt2 == '1':
                        self.addAssign()
                    elif opt2 == '5':
                        s._assign.listA()
                    elif opt2 == '2':
                        self.removeAssign()
                    elif opt2 == '3':
                        self.updateAssignDesc()
                    elif opt2 == '4':
                        self.updateAssignDeadline()
                    else:
                        print("Invalid command")
                else:
                    print("Invalid command")
            elif opt =='2':
                self.printGive()
                opt1=input('Your option:')
                if opt1 =='1':
                    self.giveStud()
                elif opt1=='2':
                    self.giveGroup()
                else:
                    print("Invalid command")
            elif opt=='3':
                self.grade()
            elif opt=='4':
                self.printStatistic()
                opt1=input('Your option:')
                if opt1=='1':
                    s._grades.listG()
                elif opt1=='2':
                    self.listStudGrade()
                elif opt1=='3':
                    self.listLate()
                elif opt1=='4':
                    self.listBest()
                else:
                    print('Invalid command')
            elif opt=='5':
                    self.undoRedo.undo()
            elif opt =='6':
                try:
                    self.undoRedo.redo()
                except Exception as va:
                    print(va)

            elif opt=='0':
                return
            else:
                print("Invalid command")

Teststudent()
Testassigment()
Teststudentrep()
Testassigmentrep()

ud=UndoController()

print('Choose Repo:')
print('1.TextRepo')
print('2.BinaryRepo')
opt=input('Your option:')
if opt=='1':
    s=Service(ud,'students.txt','assignments.txt','grades.txt')
else:
    s=Service(ud,'students.pickle','assignments.pickle','grades.pickle')

ui=UI(s,ud)
ui.Start()

