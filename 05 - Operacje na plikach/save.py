items = ['latarka', 'woda', 'namiot', 'źdźbło', 'gąbeczka']
with open('example.txt', 'w') as fopen:
       fopen.write('\n'.join(items))