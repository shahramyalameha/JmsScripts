""" This module contains all of the exceptions that are used in the chemistry
    package
"""

class ChemError(Exception):
   def __init__(self, msg='Error'):
      self.msg = msg
   def __str__(self):
      return self.msg

class ReadError(Exception):
   """ Error when files cannot be properly read """
   def __init__(self, msg='Read error.'):
      self.msg = msg

class MoleculeError(Exception):
   """ Error when molecule is illegally defined """
   def __init__(self, msg='Illegal definition of Molecule.'):
      self.msg = msg

class FileError(Exception):
   """ Error when something illegal is done with files """
   def __init__(self, msg='Illegal file manipulation'):
      self.msg = msg

class FlagError(Exception):
   """ Error when a FLAG is manipulated in readparm.amberParm """
   def __init__(self, msg='Bad flag'):
      self.msg = msg
