#! /usr/bin/env python
"""!
This module is used to handle database logging
"""
__author__ = "Ben Johnston"
__revision__ = "0.1"
__date__ = "Mon Apr 14 22:19:34 EST 2014"
__license__ = "GPL"


##IMPORTS#####################################################################
from logging import logger
import sqlite3
##############################################################################


class dbaseError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
        self.msg = msg


class dbase(object):
    """!
    Parent class for database objects
    """
    def __init__(self, dbase_name, debug_level=0):
        """!
        The constructor for the class
        @param self The pointer for the object
        @param dbase_name The name of the database file
        @param debug_level The debug level for operation of the database
        """
        ##@var debug_level
        #Controls debug functionality throughout the class
        self.debug_level = debug_level
        ##@var logger
        #The logger module for the class
        self.logger = logger(debug_level=self.debug_level)
        ##@var error_logger
        #The error logger module for the class.  Enforces debug_level=2
        #to ensure logging to file
        self.error_logger = logger(file_name='error.log',
                                   debug_level=2)
        ##@var name
        #The name of the sql file
        self.name = dbase_name
        self.open_dbase()

    def __create_dbase(self):
        """!
        Override this method with the instructions required to create
        and setup the appropriate database table structure
        """
        pass

    def __get_new_id(self, table):
        """!
        This function gets the current maximum id from <i>table</i> and
        returns the next id to be used within the table
        @param table The table within the database to contain the new id.
        @return The next id to be used within the table
        """
        msg = 'SELECT max(id) FROM %s' % table
        self.execute_SQL_statement(msg)
        max_id = self.d_cursor.fetchone()[0]
        #Increment the id counter.  If the table is entry create the first id
        if max_id is None:
            new_id = 0
        else:
            new_id = max_id + 1
        return new_id

    def execute_SQL_statement(self, statement):
        """!
        This method is used to execute an SQL statement and handle
        data logging / presentation
        @param statement A string containing the SQL statement to execute
        """
        self.logger.info(type(self).__name__ + " - " + statement)
        self.d_cursor.execute(statement)
        self.d_handle.commit()

    def execute_SQL_script(self, statement):
        """!
        This method is used to execute an SQL statement and handle
        data logging / presentation
        @param statement A string containing the SQL statement to execute
        """
        self.logger.info(type(self).__name__ + " - " + statement)
        self.d_handle.executescript(statement)

    def close_dbase(self):
        """!
        Close database file
        @param self The pointer for the object
        """
        self.d_handle.close()

    def open_dbase(self):
        """!
        Open the database file.  If the database file does not exist, one will
        be created.
        @param self The pointer for the object
        """
        ##@var d_handle
        #File handler for the sql database
        self.d_handle = sqlite3.connect(self.name)
        ##@var d_cursor
        #Cursor for the database file
        self.d_cursor = self.d_handle.cursor()
