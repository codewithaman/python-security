# main code

SECURE = (('s', '$'),('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'), ('I', '|'), ('E', '€'), ('C', '('), ('K', '|<'))

def securecode(code):
	for a,b in SECURE:
		code = code.replace(a, b)
	return code

if __name__ == "__main__":
	code = input("Enter your weak code to convert it into stronger one:\n")
	code = securecode(code)
	print(f"Your secure code is\n{code}\n")

# just a feedback code :)
input("Please enter your feedback: ")
print("Thank you for your feedback")


########################	code genetrted by the program ########################
# 1.ruby$h@rm@(@r if you forget what you wrote here just run the cracker.py and paste your made code.