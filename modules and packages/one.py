
def func():
	print("FUNC() IN ONE.PY")

def func2():
	pass

print("TOP LEVEL IN ONE.PY")


if __name__ == '__main__':
	func()
	func2()