import pyperclip

class Credentials:
    """
    Class that generates new instances of credentialss.
    """
    credentials_list = [] # Empty credentials list

    def __init__(self,account_name,account_password):

      # docstring removed for simplicity

      self.account_name = account_name
      self.account_password = account_password
    



    def save_credentials(self):
        Credentials.credentials_list.append(self)

    
    def delete_credentials(self):

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account_name(cls,name):

        for credentials in cls.credentials_list:
            if credentials.account_name == name:
                return credentials
   
    @classmethod
    def credentials_exist(cls,name):
      for credentials in cls.credentials_list:
        if credentials.account_name == name:
          return True
      return False

    @classmethod
    def display_credentials(cls):
      return cls.credentials_list  

   