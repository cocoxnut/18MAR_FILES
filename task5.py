'''with open('database.txt', 'w') as dbase:
	dbase.writelines(['Users_logins = ['yrysova', 'cocoxnut', 'kafarkhad', 'mnatalka','miranda65', 'zaza77']
'User_passwords = ['12345', '45678', 'fdacs', "asasdf", "nana123", "mimi456"]])

'''
welcome = input("Please select - Y for sign in or N for new user: ")
if welcome == 'Y':
	while True:
		log = input("Enter your login: ")
		passw = input("Enter your password: ")
		with open('database.txt', 'r') as dbase:
			x = dbase.read()   
			if log in x and passw in x:
        			print("Access is granted")
			break
if welcome == 'N':
	x = open("database.txt" , "a+") 
	f = (x.read().split())
	login2 = input("Enter new login: \n")
	if login2 in f:
		print('Such login already exists!!!')
	if login2 not in f:
		x.write(login2).
	password2 = input("Enter new password: ")
	password3 = input('Verify new password: ')  
	if password2 == password3:
		x.write(" ")
		x.write(password2)
		print("Congratulations !!! \n You have successfully registered!!!")
	else:
		print("Wrong password!!!")
		x.close()
	
	 
