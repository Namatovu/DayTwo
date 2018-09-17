vowelString=[]
vowels=['a','e','o','u']
def vowel(String):
	
	for i in String:
		if i in vowels:
			vowelString.append(i)
	vowelString.append(len(vowelString))
	
		
	return vowelString
print(vowel('damdam'))