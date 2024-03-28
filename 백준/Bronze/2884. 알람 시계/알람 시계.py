h, m = map(int, input().split())

new_m = m-45
if new_m<0:
 new_m = 60+new_m
 new_h = h-1
 if new_h<0:
  new_h = 24+new_h
  print(new_h, new_m)
 else:
  print(new_h, new_m)
else:
 print(h, new_m)