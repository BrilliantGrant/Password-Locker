import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase): 
	def setup(self):
	self.new_credentials = Credentials("Instagram","567")

	def test_credentials_instance(self):
		self.assertEqual(self.new_credentials.account_name,"Instagram")
		self.assertEqual(self.new_credentials.account_password, "567")

	def test_save_credentials(self):
        """Method that tests whether the new credential created has been saved"""
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """Method that saves multiple credentials to credentials_list"""
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Tumblr", "5678")
        new_test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_find_credential_by_name(self):
        self.new_credentials.save_credentials()
        new_test_credential = Credentials("Tumblr", "5678")
        new_test_credential.save_credentials()

        found_credential = Credentials.find_by_name("Tumblr")

        self.assertEqual(found_credential.account_name, new_test_credential.account_name)

    def test_display_all_credentials(self):
        """TestCase to test whether all contacts can be displayed"""
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)








if __name__ == '__main__':
    unittest.main()


