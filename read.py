data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)		
		count +=1 
		if count % 10000 ==0:
			print(len(data)) #共有_筆留言
print('finally finish printing, there are', len(data), 'data')
print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #加總每筆留言長度 
print('average=',  sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('there are', len(new), 'reviews are under 100 words')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('there are', len(good), 'reviews mention good')
print(good[0])