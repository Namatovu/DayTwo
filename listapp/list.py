#function fizzbuzz
def fizzbuzz(a, b):
    if not isinstance(a, list) or not isinstance(b, list):
        return "Invalid input"
    if (len(a) == 0 and len(b) == 0):
        return "Empty lists"

    combined_length = len(a) + len(b)

    if (combined_length % 3 == 0 and combined_length  % 5 == 0):
        return "fizzbuzz"
    if combined_length  % 3 == 0:
        return "fizz"
    if combined_length  % 5 == 0:
        return "buzz"
   
    return combined_length

	


print(fizzbuzz([2,4,5],[1,3,4]))