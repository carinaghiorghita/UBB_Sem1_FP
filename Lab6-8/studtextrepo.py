from repo import *
from entities import Student

'''
Implement a new kind of car repository
What do we want?
    1. Program uses it in the same way as existing Repo
        - has the same method, and they do the same thing
        - program can use both types of repos
        => repos are interchangeable and independent

    2. Use text-file based persistence
        - save/load cars from a text file
        - keep program status between runs
'''


class StudTextRepository(StudentRepo):
    def __init__(self, fileName):
        StudentRepo.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def store(self, obj):
        # 1. call repository.store to validate and store the obj
        StudentRepo.store(self, obj)

        # Repo.store call ends in one of two ways:
        #   1. obj is stored to repo and should be saved to file
        #   2. RepoException raised, obj is not saved in repo, file should
        # not change, exception has to be propagated to outer layer

        self._saveFile()

    def _saveFile(self):
        '''
        1. Open text file for writing 'w'
        2. for each car in the repository:
            a. transform it into one-line string
            b. write it to the file
        3. close file
        '''
        filepath = self._fileName
        f = open(filepath, 'w')

        line = ""
        for s in CarTextRepository.getAll(self):
            line += str(car.id) + "," + str(car.license) + "," + str(car.make) + "," + str(car.model) + "\n"
            f.write(line)

        f.close()

    def _loadFile(self):
        '''
        This function is private, so you are not allowed to call it from outside
        this class. Why?

        1. It does something that is internal to the class, which is undocumented
        2. If it is private, it can be changed at any time
        3. If we call this directly, the memory-based repo wil not work
        4. If you have a SQL repo, that will also not work
        5. files, sql, memory are what we use to store data, services should not care about that
        '''

        # 1. open the input file fo reading
        # 2. for each line in the input file
        #   a. split line into comma-separated values (CSV)
        #   b. create a Car object using the parameters
        #   c. call repo.store to add to list
        # 3. close the file
        '''
                f = open(self._fileName)

                while True:
                    line = f.read()
                    line = line.split(",")
                    print(line)
                    if line == "":
                        break
        '''

        filepath = self._fileName

        try:
            f = open(filepath, "r")
            line = f.readline().strip()
            while len(line) > 0:
                line = line.split(",")
                Repository.store(self, Car(int(line[0]), line[1], line[2], line[3]))
                line = f.readline().strip()
            f.close()
        except IOError as e:
            """
                Here we 'log' the error, and throw it to the outer layers 
            """
            print("An error occured - " + str(e))
            raise e

        '''
        filepath = self._fileName
        with open(filepath) as f:
            line = f.readline()
            cnt = 1
            while line:
                line.strip()
                line.rstrip("\n")

                elements = line.split(',')
                print(elements)
                line = f.readline()
                cnt += 1
        '''

    def deleteStringStudent(self, str):

        pass




