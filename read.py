data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %用於求餘數藉此可以設計每多少筆並進行印出
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #sum_len += len(d)
print('每筆留言平均長度為', sum_len/len(data))