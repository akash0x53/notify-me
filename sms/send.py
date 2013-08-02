import urllib2 as ulib
import cookielib
import random 


class SendSms:
    
    def __init__(self):
        UA=[('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'),
            ('Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1e; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
        ]
        self.link=""
        self.cookies=cookielib.CookieJar()
        self.opener=ulib.build_opener(ulib.HTTPCookieProcessor(self.cookies),
                                      ulib.HTTPHandler(),
                                      ulib.HTTPRedirectHandler()
                                      )
        self.opener.addheaders=[('User-agent',UA[random.randint(0,1)])]
        self.isLoggedIn=False
               
        
    def Login(self,user,passwd):
        
        if len(self.cookies)>0:
            self.cookies.clear()
            
        res=self.opener.open("http://sms.fullonsms.com/login.php", "MobileNoLogin="+user+"&LoginPassword="+passwd)
        res=res.read()
        print res.find("login")
        
        if res.find("login")==-1 :
            self.isLoggedIn=True
            print 'Logged In Successfully'
        else:
            print 'Username password didn\'t match'
            
    def send_sms(self,send_to,msg):
        
        if self.isLoggedIn:
            res=self.opener.open("http://sms.fullonsms.com/home.php", "MobileNos="+send_to+"&Message="+msg)
            if res.read().find("MsgSent")>-1 :
                print 'Message Sent.'
            else:
                print 'Problem was encountered while send Message.'
        else:
            print 'You haven\'t logged in yet, please re-check credentials that you provided.'
    
        
#if __name__=="__main__":
#    a=SendSms()
    
#    a.Login("8055737517","abc321")
#    a.send_sms("8055737517","temp msg")
    
    
    

