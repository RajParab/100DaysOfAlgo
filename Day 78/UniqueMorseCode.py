#Questions - https://leetcode.com/problems/unique-morse-code-words

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseDict={
            'a':".-",'b':"-...",'c':"-.-.",'d':"-..",
            'e':".",'f':"..-.",'g':"--.",'h':"....",
            'i':"..",'j':".---",'k':"-.-",'l':".-..",
            'm':"--",'n':"-.",'o':"---",'p':".--.",
            'q':"--.-",'r':".-.",'s':"...",'t':"-",
            'u':"..-",'v':"...-",'w':".--",'x':"-..-",
            'y':"-.--",'z':"--.."
        }
        finalAns=[]
        for i in words:
            ans=''
            for letter in i:
                ans+=morseDict[letter]
            finalAns.append(ans)
            
        return len(set(finalAns))