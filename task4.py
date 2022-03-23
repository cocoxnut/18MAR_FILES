t_words = []
with open('python_text.txt', 'r') as data:
	t = data.read()
for i in t.split():
	if 't' in i or 'T' in i:
		t_words.append(i)
print(t_words)
	 
