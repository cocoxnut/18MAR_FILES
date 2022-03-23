login = input("Enter your credentials: ")
passw = input("Enter your password: ")

with open('users.txt', 'w') as data:
	data.writelines([f'User login {login} and password {passw}'])
	
