from collections import namedtuple
struct = namedtuple	

data = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

path_dir = struct("path_dir", "name dirs")

def find_longest_path(data):
	data = data.split("\n")
	root = None
	#transforming data into sth the computer can understand :D
	for i in range(0, len(data)):
		lvl = find_level(data[i])
		name = get_name(data[i])
		if i == 0:
			root = path_dir(name, [])
		else:
			cnt = 1
			current_dir = root
			while(cnt < lvl):
				cnt += 1
				current_dir = current_dir.dirs[-1:][0]
			current_dir.dirs.append(path_dir(name, []))
	
	#Now we find the longest path in characters possible. 
	hi = ""

	#I dunno how to do it.. shit happens..
	#Fuck off...
	#I dont know how to do it efficiently, so, I'm not interested in doing it not efficient.
	#If I think of a way to make it more efficient I'll do it right away :D

	return hi

def find_level(data):
	cnt = 0
	while(data.startswith("\t")):
		cnt = cnt + 1
		data = substring(data, 1, len(data)-1)
	return cnt

def get_name(data):
	while(data.startswith("\t")):
		data = substring(data, 1, len(data)-1)
	return data

def is_file(data):
	return (data.split(".") > 1)

def substring(s, i0, i1):
    s = s[i0 : i0 + i1-i0+1]
    return s

print(find_longest_path(data))