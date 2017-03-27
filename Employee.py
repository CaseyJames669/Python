class Employee:
   def __init__(self,tmpID,tmpLastName,tmpFirstName,tmpSal):
          self.employeeID = tmpID
          self.lastName = tmpLastName
          self.firstName = tmpFirstName
          self.sal = tmpSal
   def getID(self):
          return self.employeeID
   def getFirstName(self):
          return self.firstName
   def getLastName(self):
          return self.lastName
   def getSal(self):
          return self.sal
   def setFirstName(self,tmpFirstName):
          self.firstName = tmpFirstName
   def setLastName(self, tmpLastName):
          self.lastName = tmpLastName
   def setSal(self, tmpSal):
         self.age = tmpAge
   def setID (self, tmpID):
         self.employeeID = tmpID
