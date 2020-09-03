from pydub import AudioSegment
import sys

input_music = sys.argv[1]
input_tracklist = sys.argv[2]


AudioSegment.ffmpeg = "./ffmpeg"


raw_mp3 = AudioSegment.from_mp3(input_music)

a = open(input_tracklist).read().split("\n")
songs = []


def addTimeAndTitleToDict(strng, songs):
    songs.append(strng.split(" - "))
    return songs


def timeStampToSeconds(timestamp):
    if not isinstance(timestamp, str):
        return timestamp
    h, m, s = timestamp.split(":")
    return (int(h) * 3600 + int(m) * 60 + int(s)) * 1000


for sn in a:
    songs = addTimeAndTitleToDict(sn, songs)

title = ".mp3"
start_time = 0
end_time = 0

for s in range(len(songs)):
    start_time = songs[s][0]
    try:
        end_time = songs[s+1][0]
    except:
        end_time = len(raw_mp3)
    start_time = timeStampToSeconds(start_time)
    end_time = timeStampToSeconds(end_time)
    title = songs[s][1]

    cropped_data = raw_mp3[start_time:end_time]
    cropped_data.export("{}.mp3".format(title), format="mp3")
    print("Exported", title)
