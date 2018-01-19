class user:

	"""Create class for users"""

	def__init__(self, user_name, password):
		self.user_name = user_name
		self.password = password
	user_list = []

	def save_user(self):
		self.user_list.append(self)


if__name__=='__main__':
	main()