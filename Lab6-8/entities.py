from exceptions import *

class Student:
    def __init__(self, SId, name, group,inst):
        if SId is None:
            raise NoID_S("Student ID can't be none")
        self._SId = SId
        self._Name = name
        self._Group = group
        self._Inst = inst

    @property
    def SId(self):
        return self._SId

    @property
    def Name(self):
        return self._Name

    @property
    def Group(self):
        return self._Group

    @Name.setter
    def Name(self, value):
        if len(value) < 3 or value is None:
            raise NameError('Name should have at least 3 characters')
        self._Name = value

    @Group.setter
    def Group(self, value):
        if value < 911 or value > 918 or value is None:
            raise GroupError('Group should be in the interval [912,917]')
        self._Group = value

    @property
    def Inst(self):
        return self._Inst

    @Inst.setter
    def Inst(self, value):
        self._Inst = value

    def __str__(self):
        return "Student's Id: " + str(self.SId) + ' ; Name: ' + self.Name + ' ; Group: ' + str(self.Group)


class Assignment:
    def __init__(self, AId, desc, dead):
        if AId is None:
            raise NoID_A("Assignment ID cannot be none")
        self._AId = AId
        self.Desc = desc
        self.Dead = dead


    @property
    def AId(self):
        return self._AId

    @property
    def Desc(self):
        return self._desc

    @property
    def Dead(self):
        return self._dead

    @Desc.setter
    def Desc(self, value):
        if len(value) < 3 or value is None:
            raise LengthError('The description of the assignment should have at least 3 characters')
        self._desc = value

    @Dead.setter
    def Dead(self, value):
        self._dead = value

    def __str__(self):
        return 'AssignmentID: '+str(self.AId)+'; Description: '+self.Desc+'; Deadline: Week '+str(self.Dead)



class Grade:
    def __init__(self,sId,aId,gradev):
        if sId is None:
            raise NoID_G('Student id cannot be none')
        if sId is None:
            raise NoID_G('Assignment id cannot be none')
        self._sId=sId
        self._aId=aId
        self.GradeV = gradev

    @property
    def SId(self):
        return self._sId

    @property
    def AId(self):
        return self._aId

    @property
    def GradeV(self):
        return self._gradeV
    @GradeV.setter
    def GradeV(self,value):
        if value <0 or value >10 or value is None:
            raise GradeError('Grade cannot be outside the interval [0,10]')
        self._gradeV=value
    def __str__(self):
        if self.GradeV==0:
            return 'The Student with the ID ' + str(self.SId) + ' has to do Assignment ID ' + str(self.AId) + '; he is curently ungraded'
        else:
            return 'The Student with the ID '+str(self.SId)+' has to do Assignment ID '+str(self.AId)+'; his curent grade is '+str(self.GradeV)

