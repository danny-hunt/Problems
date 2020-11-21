"""
You are going on a road trip, and would like to create a suitable music playlist.
The trip will require N songs, though you only have M songs downloaded, where M < N.
A valid playlist should select each song at least once, and guarantee a buffer of B songs between repeats.

Given N, M, and B, determine the number of valid playlists.
"""

# each song played at least once

# A  B  C  D  A  B  C  D  A  B  C  DABCD
# 26 25 24 23 23 23 23

def count_playlist(N, M, B):
    running_total = 1
    available_songs = M
    for x in range(N):
        running_total *= available_songs
        if available_songs > M - B:
            available_songs -= 1

    # This does not honour the restraint that each song must be played at least once
    return running_total


