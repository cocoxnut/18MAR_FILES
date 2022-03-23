t = open('python_text.txt', 'r')
a = t.read()
if 'w' in a:
	print("Yes, text contains letter 'w'")
else:
	print("Text doesn't contain letter 'w'")

