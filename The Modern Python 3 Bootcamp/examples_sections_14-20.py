#===========================================
# Section 14: Dictionaries
#===========================================

# video 134 Spotify Playlist Example

# playlist = {
#     'title': 'patagonia bus',
#     'author': 'colt steele',
#     'songs': [
#         {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
#         {'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
#         {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
#     ]
# }

# total_length = 0
# for song in playlist['songs']:
#     total_length += song['duration']

# print(total_length)

#-----------------------------------------------------------------------------

# video 135 Dictionary Comprehension

num_list = [1,2,3,4,5,6]
even_or_odd = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}

#-----------------------------------------------------------------------------

#===========================================
# Section 16: Tuples and Sets
#===========================================

