import queue
from getTweepy import tweepy_get
from image2video import image_to_video
import multiprocessing
import time
import threading

def queue_1(keyNames, number_thread):
  def worker():
    i = 0
    while True:
      item = q.get()
      if item is None:
        print("Break ! Because queue is empty")
        break
      tweepy_get(item)
      image_to_video(item)
      i += 1
      print("==================Thread Done==================")
      q.task_done()

  q = queue.Queue()
  threads = []

  for i in range(number_thread):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

  for item in keyNames:
    q.put(item)

  q.join()

  for i in range(number_thread):
    q.put(None)

  for t in threads:
    t.join()
