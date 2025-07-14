

count = 0
data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        # if len(data) % 1000 == 0:
        #     print(len(data))
print(f"全部總共有{len(data)}筆資料")


# 每一筆留言的平均字數 = 每一筆留言長度的總和/資料筆數
sum_len = 0
for d in data:    # d為字串 求字串長度
    sum_len = len(d) + sum_len
    # print(sum_len)

print(sum_len)
print(f'留言的平均長度為{sum_len / len(data)}個字')


# print(data)
# print(line)
#
# print(data[10000])
