#! /usr/bin/env python
"""
A boiler plate class for state machines
"""
__author__ = "Ben Johnston"
__revision__ = "0.1"
__date__ = "Mon Apr 14 22:19:34 EST 2014"
__license__ = "GPL"


##IMPORT#####################################################################

#############################################################################


class state(object):
    _SUCCESS = 0
    _ERROR = 1
    _RUNNING = -1
    _FIRST_BRANCH = 2
    _SECOND_BRANCH = 3

    def __init__(self, function, state_name=None):
        """!
        The constructor for the class
        @param self The pointer for the object
        @param function A handle for the function to be executed by the
        state
        @param state_name A string containing the name of the state
        """
        ##@var state_name
        #The name of the state
        self.state_name = state_name
        ##@var function
        #The handle for the function to be executed by the state
        self.function = function
        ##@var next_state
        #An array containing the next states to be executed
        self.next_state = []

    def set_next_state(self, next_state):
        """!
        Set the next state to be executed
        @param self The pointer for the object
        @param next_state An array containing the state objects of the next
        states to be executed by state_machine.  The first object in the list
        is to be the state that is executed upon a successful execution of the
        current state.  The second object is the error state, while the
        third and fourth are the first and second branches etc.
        """
        for i in next_state:
            self.next_state.append(i.state_name)

    def executeState(self, kwargs):
        """!
        The method to be used to execute the processes required by the state
        @param self The pointer for the object
        @param kwargs A dictionary containing the data for the state.
        @return A dictionary containing the data for the state
        """
        return self.function(**kwargs)

    def getStateName(self):
        """!
        A method used to get the name of the state
        @return A string containing the name of the state
        """
        return self.stateName


class StateMachine(object):
    """!
    This class is used to construct a state machine template
    """
    ##@var _COMPLETE_STATE
    #Defines the name of the complete state
    _COMPLETE_STATE = 'COMPLETE'
    ##@var _ERROR_STATE
    #Defines the name of the error state
    _ERROR_STATE = 'ERROR'

    def __init__(self):
        """!
        The constructor for the class
        @param self The pointer for the object
        """
        ##@var stack
        #A stack of states to be executed by the state machine
        self.stack = {}

    def add_state(self, state):
        """!
        This method adds states to the state machine.  The first state
        that is loaded is set by default to be the initial state i.e.
        the first state to be executed.
        @param self The pointer for the object
        @param state The state_machine.state object to be added to the state
        machine
        """
        if self.stack.__len__() == 0:
            ##@var initial_state
            #The first state to be loaded by the state machine
            self.initial_state = state.state_name
            ##@var current_state
            #The state currently being executed by the state machine.
            self.current_state = state.state_name
        #Add the state to the stack
        self.stack[state.state_name] = state

    def run(self):
        """!
        This method is used to run the state machine.  Overwrite this
        method in the child class to control the execution of the
        state machine.
        @param self The pointer for the object
        """
        pass
