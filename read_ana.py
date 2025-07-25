

count = 0
data = []
with open('reviews.txt', 'r') as f:
    for line in f:                # line是字串 file是整個清單
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


# ==================留言的篩選==================
# 例如：篩選出留言數量小於100的留言

new = []
for d in data:
    if len(d) < 100:  # 如果留言長度小於100
        new.append(d)  # 就加入到new清單中

print('一共有', len(new), "筆留言長度小於100")
print(new[0])  # 印出第一筆留言
print(new[1])  # 印出第二筆留言


# ==================單字的篩選==================
good = []
for d in data:
    if 'good' in d:  # 如果留言中有good這個單字
        good.append(d)  # 就加入到good清單中 所以append的d是運算式的結果(d 為篩選過後的字串)
print('一共有', len(good), "筆留言中有good這個單字")
# print(good[0])  # 印出第一筆留言

# ==================列表生成式==================
good = [d for d in data if 'good' in d]  # 等同43~46 (list comprehension)
# 第一個d為運算式，此處的意思為append到good清單中的append的d
# print(good)
print('一共有', len(good), "筆留言中有good這個單字")


bad = ['bad' in d for d in data]
print(bad)
