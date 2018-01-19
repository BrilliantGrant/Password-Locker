import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

		def setUp(self):
			self.new_credentials = Credentials("Tumblr","567")

		def tearDown(self):
			Credentials.credentials_list = []


		def test_init(self):
			self.assertEqual(self.new_credentials.account_name,"Tumblr")
			self.assertEqual(self.new_credentials.account_password,"567")
			

		def test_save_credentials(self):
			self.new_credentials.save_credentials()
			self.assertEqual(len(Credentials.credentials_list),1)

		# pass
		def test_save_multiple_credentials(self):
		    self.new_credentials.save_credentials()
		    test_credentials = Credentials("Instagram","5678")
		    test_credentials.save_credentials()
		    self.assertEqual(len(Credentials.credentials_list),2)

		

		def test_delete_credentials(self):
			self.new_credentials.save_credentials()
			test_credentials = Credentials("Instagram","5678")
			test_credentials.save_credentials()

			self.new_credentials.delete_credentials()
			self.assertEqual(len(Credentials.credentials_list),1)

		def test_find_credentials_by_name(self):
		        self.new_credentials.save_credentials()
		        test_credentials = Credentials("Instagram","5678") # new credentials
		        test_credentials.save_credentials()

		        found_credentials = Credentials.find_by_account_name("Instagram")

		        self.assertEqual(found_credentials.account_name,test_credential.account_name)

		def test_credentials_exists(self):
			self.new_credentials.save_credentials()
			test_credentials = Credentials("Instagram","5678")
			test_credentials.save_credentials()

			credentials_exists = Credentials.credentials_exist("Instagram")

			self.assertTrue(credentials_exists) 


		def test_display_all_credentialss(self):
			self.assertEqual(Credentials.display_credentialss(),Credentials.credentials_list)


		

		
		   

if __name__ == '__main__':
	unittest.main()