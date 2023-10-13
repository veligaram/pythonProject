import pytube
vedio_url=input('Enter url: ')
vedio_instance=pytube.YouTube(vedio_url)
stream=vedio_instance.streams.get_highest_resolution()
stream.download()