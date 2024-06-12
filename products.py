products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	products.append([name,price])  #二維清單
print(products)

products[0][0]

for p in products:
	print(p) #會印出小清單
	print(p[0], '的價格是：', p[1])
