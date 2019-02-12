
import somePackage.wow

def do_something():
	for i in range(2):
		print(i)
	somePackage.wow.say_wow()
	print('bye')

print('Application launched successfully')

do_something()
