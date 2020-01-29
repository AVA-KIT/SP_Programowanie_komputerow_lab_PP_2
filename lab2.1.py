#1
hitsTitles =['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']

#2
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')

#3
hitsTitles.insert(2,'HOTEL CALIFORNIA')

#4
hitsTitles.insert(0,'THE SOUND OF SILENCE')

#5
v = hitsTitles.index('HOTEL CALIFORNIA')
print('Numer indeksu dla piosenki HOTEL CALIFORNIA: {}'.format(v))

#6
hitsTitles.remove('HOTEL CALIFORNIA')

#7
hitsTitles[0] = 'ENJOY THE SILENCE'

#8
hitsToRead =[]
hitsToRead.extend(hitsTitles)

#9
hitsToRead.reverse()

#10
hitsToRead.sort()

#11
print(hitsToRead.pop(0))
print(hitsToRead.pop(1))

#12
additionalSongs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']

#13
hitsToRead.extend(additionalSongs)

#14
x = hitsToRead.count('WISH YOU WERE HERE')
print('WISH YOU WERE HERE będzie zagrane: {} '.format(x))
y = hitsToRead.count('RIDERS ON THE STORM')
print('RIDERS ON THE STORM będzie zagrane: {}'.format(y))

#15
hitsToRead.clear()