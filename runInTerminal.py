import sys
with open('output.log', 'w') as fs:
	fs.write(sys.executable)

print('Done')
