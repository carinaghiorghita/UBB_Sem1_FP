class UndoController:
    def __init__(self):
        # History of the program's undoable operations
        self._history = []
        # Keep the position in the redo/undo list
        self._index = 0
        # True if we are during an undo/redo operation
        self._duringUndo = False
        self._lastUndo = False
        self._dif = 0

    def recordOperation(self, operation):
        '''
        Record an operation in the history for undo/redo
        :param
            operation: the operation that was carried out
        :return:
            none
        '''
        if self._duringUndo is True:
            return
        if self._lastUndo is True:
            while self._index != len(self._history):
                del self._history[len(self._history)-1]
        self._history.append(operation)
        self._index += 1
        self._lastUndo = False

    def pop(self):
        if self._duringUndo is True:
            return
        self._index -= 1
        obj = self._history[self._index]
        self._history.pop(self._index)
        return obj

    def undo(self):
        if self._index == 0:
            raise ValueError('No more undos!')
        self._duringUndo = True
        self._index -= 1
        self._history[self._index].undo()
        self._duringUndo = False
        self._lastUndo = True

    def redo(self):
        if self._lastUndo is True:
            if self._index == len(self._history):
                raise ValueError('No more redos!')
            self._duringUndo = True
            self._history[self._index].redo()
            self._index += 1
            self._duringUndo = False
        else:
            raise Exception("Cannot perform redo without last operation undo!")


# 1. Keep a reference to a function and its parameters
# We use the command design pattern
class FunctionCall:
    def __init__(self, function, *parameters):
        # * because we don t know how many parameters we will have
        self._function = function
        self._params = parameters

    def __call__(self):
        self.call()

    def call(self):
        # self._params - tuple
        # * expands the tuple into actual parameters
        # without * it self._params is only one parameter which is a tuple
        self._function(*self._params)


class Operation:
    '''
    Store the function reference and params for both undo and redo
    '''

    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction

    def undo(self):
        self._undo()
        # self._undo.call()

    def redo(self):
        if self._redo is None:
            return
        self._redo()


class CascadedOperation:
    def __init__(self, *operations):
        self._oper = operations
        self._oper = list(self._oper)

    def undo(self):
        for o in self._oper:
            o.undo()

    def redo(self):
        for o in self._oper:
            o.redo()

    def add(self, o):
        self._oper.append(o)
