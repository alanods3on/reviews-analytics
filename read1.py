data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: # %用於求餘數藉此可以設計每多少筆並進行印出
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

wc = {}

for d in data:
	words = d.split() #split內部打預設分隔條件為空白鍵，且會無視連續空白鍵
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請輸入你想查找的字: ')
	if word == 'q':
			break
	if word in wc:
		print(word, '出現的次數為: ', wc[word])
	else:
		print('很抱歉 你輸入的字無法查詢到! 請再次輸入')	
print('感謝您使用本查詢功能')		