import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from selenium import webdriver
driver = webdriver.Chrome("/home/mj/Documents/scrape/selscrape/chromedriver")

pages=set()
extract={}
baseurl="https://www.quora.com"


flag=1
def get_topic_list(pagenum,word):
    n=len(pagenum)
    temp=0
    i=0
    for i in range(0,n):

        linktoclick=pagenum[i]
        html=urlopen(linktoclick)
        bsobj=BeautifulSoup(html)
        maindiv=bsobj.find("div",{"class":"ContentWrapper"})
        ls=maindiv.find("a",href=re.compile("(/topic/)"))
        if word.lower()>ls.get_text().lower():
        	temp=i

        elif word.lower()<ls.get_text().lower() and word.lower() not in ls.get_text().lower():
        	flag=-1
        	break

    if i==temp:
        try:
          linktoclick=pagenum[i]
          html=urlopen(linktoclick)
          bsobj=BeautifulSoup(html)
          maindiv=bsobj.find("div",{"class":"ContentWrapper"})               
          ls=maindiv.findAll("a",href=re.compile("(/topic/)"))
          if word.lower()>ls[0].get_text().lower() and word.lower()<=ls[len(ls)-1].get_text().lower() :
             for k in ls :
                m= re.search( r'topic/(.*)',k.attrs["href"], re.M|re.I)
                m=m.group(1)
                extract[k.get_text().lower()]=m
        except:
          pass



    else:        
	    for j in range(temp,i):
	        linktoclick=pagenum[j]
	        html=urlopen(linktoclick)
	        bsobj=BeautifulSoup(html)
	        maindiv=bsobj.find("div",{"class":"ContentWrapper"})               
	        ls=maindiv.findAll("a",href=re.compile("(/topic/)"))
	        for k in ls :
	            m= re.search( r'topic/(.*)',k.attrs["href"], re.M|re.I)
	            m=m.group(1)
	            extract[k.get_text().lower()]=m
       	       

            














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
        get_topic_list(pagenum,word)
        
        if (pagen[len(pagen)-1].get_text()!="Next" or flag==-1):
        	return extract

        linktoclick=pagenum[len(pagenum)-1]
        driver.get(linktoclick)
        pagenum=[]

     

def binary_search(word,ls):
    l=0;
    r=len(ls)-1
    mid=l+(r-l)//2
    while l<=r:
        if ls[mid].lower()==word:
            return mid
        elif ls[mid].lower()>word:
            r=mid-1
        else:
            l=mid+1
        mid=l+(r-l)//2
    return -1

    

   
   
# ,href=re.compile("(/{wo}/)".format(wo=word))
ans={}
ansl=[]
    
def getLinks(pageUrl,word):
    k=0
    
    global  pages
    html=urlopen(pageUrl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.findAll("a",{"class":"question_link"}):
        if 'href' in link.attrs:
            if link.attrs['href'] not in  pages:

                newPage=link.attrs['href']
                pages.add(newPage)
                ansl.append(newPage)
    # for link in bsObj.findAll("span",{"class":"count"}):
    	
    # 	ans[ansl[k]]=link.get_text()
    # 	k=k+1








def go_to_topic(word):
	word=word.lower()
	di=begin("/sitemap/alphabetical_topics/",word)
	ls=sorted(di.keys())
	
	ind=binary_search(word,ls)
	if ind!=-1:
		topic_url=di[ls[ind]]
		linktoclick="https://www.quora.com/topic/{t}".format(t=topic_url)
		driver.get(linktoclick)
		getLinks(linktoclick,word)
		# for i in ans.keys():
		# 	print(i,"--->",ans[i],"\n\n")
		for i in ansl:
			print(baseurl+i,"\n")



	else:
		print("Not found!!\n\nSuggested Searches:\n\n")
		for i in ls:
			print(i,"\n")


 


go_to_topic("data")

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
