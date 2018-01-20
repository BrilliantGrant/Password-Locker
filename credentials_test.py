import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
			"""Test class that defines test cases for the Credentials class behavior
	    	"""

	def setUp(self):
		"""Set up method to run befor before each test case"""
		self.new_credentials = Credentials("Tumblr","567")

	def tearDown(self):
		'''
        tearDown method that does clean up after each test case has run.
        '''
		Credentials.credentials_list = []


	def test_init(self):
		'''
    	test_init test case to test if the object is initialized properly
    	'''
		self.assertEqual(self.new_credentials.account_name,"Tumblr")
		self.assertEqual(self.new_credentials.account_password,"567")
		

	def test_save_credentials(self):
		"""Method that tests whether the new_credentials have been instantiated correctly"""
		self.new_credentials.save_credentials()
		self.assertEqual(len(Credentials.credentials_list),1)

	# pass
	def test_save_multiple_credentials(self):
		 """Method that saves multiple credentials to credentials_list"""
	    self.new_credentials.save_credentials()
	    test_credentials = Credentials("Instagram","5678")
	    test_credentials.save_credentials()
	    self.assertEqual(len(Credentials.credentials_list),2)

	

	def test_delete_credentials(self):
		'''
        test_delete_credentials to test if we can remove a contact from our contact list
        '''
		self.new_credentials.save_credentials()
		test_credentials = Credentials("Instagram","5678")
		test_credentials.save_credentials()

		self.new_credentials.delete_credentials()
		self.assertEqual(len(Credentials.credentials_list),1)

	def test_find_credentials_by_name(self):
		"""Test to check if we can find credentials and display information"""
		self.new_credentials.save_credentials()
		test_credentials = Credentials("Instagram","5678") # new credentials
		test_credentials.save_credentials()

		found_credentials = Credentials.find_by_account_name("Instagram")

		self.assertEqual(found_credentials.account_name,test_credentials.account_name)

	def test_credentials_exists(self):
		self.new_credentials.save_credentials()
		test_credentials = Credentials("Instagram","5678")
		test_credentials.save_credentials()

		credentials_exists = Credentials.credentials_exist("Instagram")

		self.assertTrue(credentials_exists) 


	def test_display_all_credentialss(self):
		"""TestCase to test whether all contacts can be displayed"""
		self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


	

		
		   

if __name__ == '__main__':
	unittest.main()