import one

print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ == '__main__':
	print("TWO.PY IS BEIGN RUN DIRECTLY")

else:
	print("one.py has been imported")