import unittest
from user import user

class Testuser(unittest.TestCase):
	
	def setup(self):
		self.new = user("Newuser","12345")



if __name__ == '__main__':
    unittest.main()
