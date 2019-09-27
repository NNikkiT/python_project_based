# 3.4
invite = ['angela','harper','eve','davy','walter']
i=0
for i in invite:
	print (i +' please eat dinner with me')

# 3.5
print(invite[2] + " can't eat dinner with me")
invite[2] = 'a'
print(invite)

for i in invite:
	print (i +' please eat dinner with me')

# 3.6
invite.append('liuyuan')
for i in invite:
	print ( i + ' please eat dinner with me again')

invite.insert(0,'hualong')
for i in invite:
	print( i +  ' please eat with me')

# 3.7
print(invite)
print(invite.pop(0) + ' sorry for can not eat dinner with you')

for i in invite[:]:
    if i != 'a':
        invite.remove(i)
    else:
        print(i)

print(invite)

invite.append('b')
print(invite)
for i in invite:
	print(i + ' please eat lunch with')

del invite[:]
print(invite)