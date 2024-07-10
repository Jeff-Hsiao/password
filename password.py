pwd = 'a123456'
time = 3

while time > 0:	
	time -= 1
	input_pass = input('請輸入密碼: ')
	if input_pass == pwd:
		print('登入成功!!!')
		break
	else:
		print('密碼錯誤!')
		if time > 0:
			print('還有', time,'次機會')
		else:
			print('沒機會了!!')