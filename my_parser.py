from colorama import init, Fore
import requests
from bs4 import BeautifulSoup as Bs
init()
def banner(): #Create banner
  a = '''
  __  __          _  ___    _  _____ _    _          
 |  \/  |   /\   | |/ / |  | |/ ____| |  | |   /\    
 | \  / |  /  \  | ' /| |  | | (___ | |__| |  /  \   
 | |\/| | / /\ \ |  < | |  | |\___ \|  __  | / /\ \  
 | |  | |/ ____ \| . \| |__| |____) | |  | |/ ____ \ 
 |_|  |_/_/    \_\_|\_\\____/|_____/|_|  |_/_/    \_\
                                                     
                                                                                                                      
  '''
  print(Fore.YELLOW,a)
  
def get_url(): #main function
  url = input('Enter url: ')
  r = requests.get(url) #get site url
  soup = Bs(r.content, 'lxml') #create class obj for parse
  tag = input('Enter tag: ') #input tag
  text_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'p', 'title']
  tag_html = soup.find_all(tag) #create parser for some element
  while True: 
    
    if tag in text_tags: #if tag is text
      do_text = input('Do this to text? Y or N: ')
      
      if do_text == 'Y' or do_text=='y':
        for el in tag_html:
          print(el.text) #write tag how text
      else: #else
        for el in tag_html:
          print(el) #write element
    elif tag == 'stp': #if tag is stop
      url = input('Enter url: ') #restart porgram for new url
      r = requests.get(url)
      soup = Bs(r.content, 'lxml')
    else: #else
      for el in tag_html:
        print(el) 
    tag = input('Enter tag (stp - stop): ') #input in while 
    tag_html = soup.find_all(tag)
banner()
get_url() #run functions