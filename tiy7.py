guests=['Michelle', 'Chad', 'Chris']
print("Hey I found a bigger table",guests)
guests.insert(0, 'Joseph')
guests.insert(1, 'Millah')
guests.insert(2, 'Katy')
guest_removed = guests.pop()
print("Sorry they can't come for dinner:",guest_removed)
guest_removed = guests.pop()
print("Sorry they can't come for dinner:",guest_removed)
guest_removed = guests.pop()
print("Sorry they can't come for dinner:",guest_removed)
guest_removed = guests.pop()
print('Please come over for dinner',guests[0])
print('Please come over for dinner',guests[1])
del guests[0]
del guests[0]
print(guests)