def is_pangram(s):
	alphabet = set('abcdefghijklmnopqrstuvwxyz')
	s = set(s.lower())
	return s.intersection(alphabet) == alphabet

if __name__ == '__main__':
	from sys import argv
	is_pangram(argv[1])