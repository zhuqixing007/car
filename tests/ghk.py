import re


pattern = re.compile('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
ip = 'turtyu'
print(re.match(pattern, ip))
