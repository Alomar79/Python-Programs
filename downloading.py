from pafy import new
url = input('enter you link here:')
video = new(url)
stream = video.streams
for i in stream:
    print(i)
stream[0].download()