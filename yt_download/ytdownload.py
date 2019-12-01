from pytube import YouTube

vid_url = input('PASTE VIDEO URL HERE: ')
# dest_folder = input('PASTE DESTINATION FOLDER: ')

yt = YouTube(vid_url)

stream = yt.streams.first()
stream.download()