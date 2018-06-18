count = 0
[n, m] = [int(input()) for _ in range(2)]
ts = [int(input()) for _ in range(m)]
song_max_length = n * 60
recording_song_sum = 0
for i in ts:
    recording_song_sum += i
    if recording_song_sum > song_max_length:
        break
    count += 1

answer = "OK" if count >= m else count
print(answer)
