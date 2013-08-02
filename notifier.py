import urllib2 as ulib
from time import sleep
from md5 import md5



class GenHash:
    
    def __init__(self,link):
        self.link=link
        self.initial_hash=self.extract_header()
    
    def header_hash(self):
        header=ulib.urlopen(self.link).headers
        contetn_len=header.values()[0]
        hash=md5(contetn_len).hexdigest()
        return hash
                 
           
    
    
    
    
    



