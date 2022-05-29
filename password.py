password_real = 'a123456'
x = 2
while True:
	password = input('密碼: ')
	if password == password_real :
		print('成功登入')
		break
	elif password != password_real :
		print('還有', x,'機會')
		x = x-1
		if x == -1 :
			break

