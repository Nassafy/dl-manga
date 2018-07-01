#!/bin/python
from dl import *
import subprocess

def read_current_chapter():
    with open("chapter.txt", 'r') as f:
        chapter = f.read()
    return chapter

def write_current_chapter(chapter):
    with open("chapter.txt", 'w') as f:
        f.write(str(chapter))

def notify(chapter):
    message = f"One piece chapter {chapter} downloaded"
    subprocess.run(['notify-send', message])

if __name__ == '__main__':
    chapter = read_current_chapter()
    if check_chapter(chapter):
        dl_chapter(chapter)
        notify(chapter)
        write_current_chapter(int(chapter) + 1)
