print('Xin mời nhập tên:')
name = input()
if name == 'Long':
    print('Xin chào '+ name)
elif name =='':
    print('Bạn không có tên à?')
else:
    print('Chào '+name)

print('Xin hãy nhập tuổi của bạn:')
age = input()
if age == '':
    print('Bạn không nhâp tuổi à?')
elif int(age) > 100:
    print('Tầm này bạn sắp xuống lỗ hoặc bạn bất tử :))')
elif int(age) < 0:
    print('Đừng nhập số âm, bạn đã chết quái đâu -,-!')
elif int(age) < 18:
    print('Bạn chưa đủ tuổi công dân!')
elif int(age) > 18:
    print('Bạn đã đủ tuổi công dân!')
