'''
Created on 1 janv. 2019

@author: rachid
'''
import requests
from bs4 import BeautifulSoup as bs
from pytube import YouTube


class Scraper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.siteUrl = "https://www.youtube.com"
        self.baseUrl = self.siteUrl + "/results?search_query="
        self.videos = []

    def chercher(self, searchQuery):
        requete = requests.get(self.baseUrl+searchQuery)

        # extract the html of the search results page using BeautifulSoup
        page = requete.text
        soup=bs(page,'html.parser')
        
        # extract the links to the individual videos
        liens = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
        
        self.videos=[]
        for item in liens:
            mediaUrl = item['href']
            if mediaUrl.startswith("/watch?"):
                tmp = self.siteUrl + mediaUrl
                self.videos.append(tmp)

    def afficher(self):
        for item in self.videos:
            print(item)
        
    def telecharger(self, nombre = 0):
        count=0
        for item in self.videos:
         
            # increment counter:
            count+=1
            
            if count > nombre:
                break
         
            # initiate the class:
            yt = YouTube(item)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
         
            # have a look at the different formats available:
            #formats = yt.get_videos()
         
            # grab the video:
            #video = yt.get('mp4', '360p')
         
            # set the output file name:
            #yt.set_filename('Video_'+str(count))
         
            # download the video:
            #video.download('./')
                