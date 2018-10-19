list1=[] #initializing empty lists
list2=[]
def fizzbuzz(list1,list2):
	length1=len(list1)
	length2=len(list2)
	combined_length=length1+length2 #getting the combined length
	if combined_length%3==0: #testing if its divisible by 3 
		return "Fizz"
	elif combined_length%5==0: #testing if its divisible by 5
		return "Buzz"
	elif combined_length%3==0 and combined_length%5==0:  #testing if its divisible by both
		return "FizzBuzz"
	else:
		return "not applicable"
print(fizzbuzz([2,4,5],[1,3,4]))
	
	 
	 
	 
	 
		 
	
		
	
		
	
		

	
	
		
	
		
	
		
	
		
	
		
	

	
		
	
	
