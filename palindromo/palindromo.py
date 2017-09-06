def palindromo(s):
	s = s.replace(' ', '')
	for i in range(int(len(s)/2)):
		if s[i] != s[-i-1]:
			return False
	return True

if __name__ == '__main__':
	assert palindromo('anna')
	assert palindromo('i topi non avevano nipoti')
