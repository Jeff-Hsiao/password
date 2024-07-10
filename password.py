pwd = 'a123456'
time = 3

while time > 0:	
	input_pass = input('請輸入密碼: ')
	if input_pass == pwd:
		print('登入成功!!!')
		break
	else:
		time -= 1			
		print('密碼錯誤! 還有', time,'次機會')