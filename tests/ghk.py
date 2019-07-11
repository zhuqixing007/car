import re


pattern = re.compile(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
ip = 'turtyu'
print(re.match(pattern, ip))

pattern2 = re.compile(r'[0-9]{1,5}$')
port = '33'
print(re.match(pattern2, port))