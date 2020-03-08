import subprocess

def image_to_video(twitterUsr):
  fileName = "img/" + twitterUsr + "%01d" + ".png"
  normalVideo = "output/" + twitterUsr + "normal.avi"
  betterVideo = "output/" + twitterUsr + "better.mp4"  
  subprocess.call(['ffmpeg', '-framerate', '0.3', '-i', 
    fileName, 
    normalVideo])
  subprocess.call(['ffmpeg', '-i', normalVideo, '-c:a', 'copy', 
    '-c:v', 'copy', '-r', '30', '-s', 'hd720', '-b:v', '2M', 
    betterVideo])
