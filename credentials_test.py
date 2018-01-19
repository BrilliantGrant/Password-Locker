import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase): 
	def setup(self):
	self.new_credentials = Credentials("Instagram","12345")




if __name__ == '__main__':
    unittest.main()


