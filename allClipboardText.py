import pyperclip

oldClip=""
while(1==1):
    clip = pyperclip.paste()
    if(oldClip != clip):
        print(clip)
        oldClip = clip
    if(clip.lower() == 'exit'):
        break
 
