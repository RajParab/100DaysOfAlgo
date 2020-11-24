#Question- 

import string 
import random 
  

class Codec:
    def __init__(self):
        self.arr={}
        
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 5)) 
        self.arr[res]=longUrl
        return 'http://tinyurl.com/'+res
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.arr[shortUrl[19:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))