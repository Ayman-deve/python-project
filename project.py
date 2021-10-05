# Importing YouTube Module from pytube library

from pytube import YouTube

link = 'https://www.youtube.com/watch?v=hSsuPBUxn3Y'

myvideos=YouTube(link)

#get the video Discribtion
print(myvideos.title)

print(f"video title Title is:\n{myvideos.title}\n---------------")

print(f"video title Title is:\n{myvideos.views}\n---------------")

print(f"video title Title is:\n{myvideos.length}\n---------------")

print(f"video title Title is:\n{myvideos.rating}\n---------------")

#get the video information 

for Stream in myvideos.streams:
    print(Stream)

print(myvideos.streams.get_highest_resolution())

print(myvideos.streams.get_lowest_resolution())

#complition function 

def done():
    print(" Your download is now ready " )


#Download call function 

myvideos.streams.get_highest_resolution().download()

#finish up the project
myvideos.register_on_complete_callback(done())


""" 

#or Stream in myvideos.streams.filter(progressive=True):
    #print(Stream)
# Prompting user for Youtube Video link


 """