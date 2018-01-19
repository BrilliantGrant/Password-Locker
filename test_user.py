import unittest
from user import User

class Testuser(unittest.TestCase):
	
	def setUp(self):
		"""Set up method to run before eaach test cases"""
		self.new_user = User("Newuser","567")

	def test_init(self): 
		"""test_init test case to test if the object is initialized properly"""
		self.assertEqual(self.new_user.user_name, "Newuser")
		self.assertEqual(self.new_user.password, "567")

	def test_save_user(self):
		"""test_save_user test case to test if the user object is saved into the user list"""
		self.new_user.save_user()
		self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()
