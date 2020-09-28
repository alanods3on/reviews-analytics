data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %用於求餘數藉此可以設計每多少筆並進行印出
			print(len(data))
print(len(data))
print(data[0]) #[0]index索引
print('-------------------------')
print(data[1])