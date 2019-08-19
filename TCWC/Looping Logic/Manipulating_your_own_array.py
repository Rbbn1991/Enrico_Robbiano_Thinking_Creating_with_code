favourite_songs=['Batman soundtrack',
                 'Pollon','Tigerman'
                 ,'Pokemon']


favourite_songs.sort()

print(favourite_songs[0])
print(favourite_songs[1])
print(favourite_songs[2])
print(favourite_songs[3])    

favourite_songs.append('Zorro Soundtrack')

song_count=len(favourite_songs)
print("There are %n songs",song_count)

favourite_songs.pop(2)

print(favourite_songs)

print(len(favourite_songs))