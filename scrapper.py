from bs4 import BeautifulSoup
import requests
from collections import deque

file=open("google.txt","w")

def scrappingRecur(current,visited):
    if len(current)==0:
        return
    response=requests.get(current)
    soup=BeautifulSoup(response.text,'lxml')
    visited.add(current)
    for link in soup.findAll('a'):
        if link.get('href') not in visited and link.get('href') is not None and str(link.get('href')).startswith( 'http' ):
            #print(link.get('href'))
            file.write(link.get('href')+'\n')
            scrapping(link.get('href'),visited)

def scrappingIterative(current,unVisited):
    visited=set()
    unVisited.add(current)
    count=0
    while unVisited:
        val=next(iter(unVisited))
        response=requests.get(val)
        soup=BeautifulSoup(response.text,'lxml')
        for anchor in soup.findAll('a'):
            if anchor is None or anchor.get('href') is None:
                continue
            if not anchor.get('href').startswith('http'):
                continue

            if anchor.get('href') not in visited and anchor.get('href') not in unVisited:
                unVisited.add(anchor.get('href'))
                #print(anchor.get('href'))
                file.write(anchor.get('href')+'\n')
                count+=1
                print(count,end=' ')
        unVisited.remove(val)
        visited.add(val)

initialLink="https://www.google.com/"
visited=set()
scrappingIterative(initialLink,visited)
file.close()
