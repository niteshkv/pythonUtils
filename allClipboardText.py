import pyperclip

lineNumber=1
oldClip=""
while(1==1):
    clip = pyperclip.paste()
    if(oldClip != clip):
        print("-------------------------------------- Clip Item % 2d ---------------------------------" %(lineNumber))
        print(clip)
        oldClip = clip
        lineNumber = lineNumber + 1
    if(clip.lower() == 'exit'):
        break
        
