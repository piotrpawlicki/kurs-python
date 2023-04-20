bin_num = 1001111
bin_num = str(bin_num)

str_len = len(bin_num)
str_len = str_len - 1

a0 = 2^0 * int(bin_num[str_len])
a1 = 2^1 * int(bin_num[str_len-1])
a2 = 2^2 * int(bin_num[str_len-2])
a3 = 2^3 * int(bin_num[str_len-3])
a4 = 2^4 * int(bin_num[str_len-4])
a5 = 2^5 * int(bin_num[str_len-5])
a6 = 2^6 * int(bin_num[str_len-6])

conv_bin_num = a0 + a1 + a2 + a3 + a4 + a5 + a6
print(conv_bin_num)


