from getTweepy import tweepy_get
from image2video import image_to_video
from systemQueue import queue_1
import multiprocessing
import time
import threading
import queue
import os

def test_twitter_get():
  keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
  for key in keyNames:
    pass

def test_image_to_video():
  keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
  for key in keyNames:
    pass
    
def test_queue():
  keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
  number_thread = 4
