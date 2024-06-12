products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	products.append([name,price])  #二維清單
print(products)

products[0][0]