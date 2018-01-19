class Credentials:


	def __init__ (self,account_name, account_password):
		self.account_name = account_name
		self.account_password = account_password

		credentials_list = []

	def save_credentials(self):
	    self.credentials_list.append(self)
	    
	def delete_credentials(self):
		"""delete _contact method deletes a saved contact from contact_list"""
		Credentials.credentials_list.remove(self)

	@classmethod

	def find_by_name(cls, account_name):
		"""Method that atkes in a number and returns that matches that number.

		Args: 

		account_name: user_name to search for

		Returns:
		user name that matches the number"""
		for credential in cls.credentials_list:
			if credential.account_name == account_name:
			    return credential

	@classmethod
	def credential_exists(cls, name):
		"""Method to check whether a credential exists
		Args:
		name: name of account to search whether it exists
		boolean: True or False depending if the contatc exists
		"""

		for credential in cls.credentials_list:
			if credential.account_name == name:
			    return True
		return False

	@classmethod
	def display_credentials(cls):
	    """Method which displays all current credentials"""
	    return cls.credentials_list







