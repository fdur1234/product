# product


products = []
while True:
	name = input('請輪入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入品價格：')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])