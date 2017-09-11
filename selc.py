import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
driver = webdriver.Chrome("/home/mj/Documents/scrape/selscrape/chromedriver")

pages=set()
baseurl="https://www.quora.com"
def getLinks(pageUrl):
    global  pages
    html=urlopen(baseurl+pageUrl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.findAll("a",{"class":"question_link"},href=re.compile("(/data/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in  pages:

                #We have    encountered a   new page
                newPage=link.attrs['href']
                print(newPage)
                pages.add(newPage)
                if len(pages)==10:
                    return
                getLinks(newPage)
                if len(pages)==10:
                    return
          
# getLinks("")

def binary_search(word,ls):
    l=0;
    r=len(ls)-1
    mid=l+(r-l)//2
    while l<=r:
        if ls[mid].get_text().lower()==word:
            return mid
        elif ls[mid].get_text().lower()>word:
            r=mid-1
        else:
            l=mid+1
        mid=l+(r-l)//2
    return -1


def get_topic_url(pagenum,word):
    n=len(pagenum)
    for i in range(0,n):

        linktoclick=pagenum[i]
        html=urlopen(linktoclick)
        bsobj=BeautifulSoup(html)
        maindiv=bsobj.find("div",{"class":"ContentWrapper"})
        ls=maindiv.findAll("a",href=re.compile("(/topic/)"))
        for i in ls :
            print(i.get_text())
            m= re.search( r'topic/(.*)',i.attrs["href"], re.M|re.I)
            m=m.group(1)
            print(m)

        print("\n\n")
        break    
            














def begin(pageUrl,word):
    pagenum=[]
    linktoclick=baseurl+pageUrl+word[:2].lower()  
    pagenum.append(linktoclick)
        
        
    while 1:
        html=urlopen(linktoclick)
        bsobj=BeautifulSoup(html)
        maindiv=bsobj.find("div",{"class":"ContentWrapper"})
        pages_head=maindiv.find("h2")
        cur=pages_head.find("strong").get_text()
        pagen=pages_head.findAll("a")
        
        
        for i in pagen:
     
                if i.get_text()!="Next" and i.get_text()!="Previous" and int(i.get_text())>int(cur) :
                    pagenum.append(baseurl+i.attrs["href"])
        #print(pagenum)

        get_topic_url(pagenum,word)
        break
        # if got_topic!=-1:
        #     print(got_topic)
   
        #     break
        
        if pagen[len(pagen)-1].get_text()!="Next":
            break
        linktoclick=pagenum[len(pagenum)-1]
        driver.get(linktoclick)
        pagenum=[]
     

    

   
   

    

 
    # else:



    # else:
    #     print(0)





    # driver.get(baseurl+pageUrl+word[:2]+"?page_id=15")

    




begin("/sitemap/alphabetical_topics/","data")

# # driver function
# def main():
 
#     # Input keys (use only 'a' through 'z' and lower case)
#     keys = ["the","a","there","anaswe","any",
#             "by","their"]
#     output = ["Not present in trie",
#               "Present in tire"]
 
#     # Trie object
#     t = Trie()
 
#     # Construct trie
#     for key in keys:
#         t.insert(key)
 
#     # Search for different keys
#     print("{} ---- {}".format("the",output[t.search("the")]))
#     print("{} ---- {}".format("these",output[t.search("these")]))
#     print("{} ---- {}".format("their",output[t.search("their")]))
#     print("{} ---- {}".format("thaw",output[t.search("thaw")]))
