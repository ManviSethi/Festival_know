
bot_template = "BOT : {0}"
user_template = "USER : {0}" 
#function Declaration 
def newyear():
    print(bot_template.format("New Year is the time or day at which a new calendar year begins and the calendar's year count increments by one."))
def makrskn():
    print(bot_template.format("The festival of kites is here. Makar Sankranti is one of the most popular Hindu festivals"))
def republicday():
    print(bot_template.format("Republic Day is a national holiday in India.\n It honours the date on which the Constitution of India came into effect on 26 January 1950"))
def pongal():
    print(bot_template.format("The three days of the Pongal festival are called Bhogi Pongal, Surya Pongal and Maattu Pongal\nthe festival marks the end of winter solstice, and the start of the sun's six-month-long journey northwards (the Uttaraayanam) when the sun enters the zodiac Makara (Capricorn)."))
def shivratri():
    print(bot_template.format("Maha Shivaratri is a Hindu festival celebrated annually in honour of Lord Shiva. The name also refers to the night when Shiva performs the heavenly dance."))
def Valentine():
    print(bot_template.format("Valentine Day is celebrated annually on February 14,people exchange cards, candy or flowers with their special “valentine.”"))
def holi():
    print(bot_template.format("Holi is a popular ancient Hindu festival, also known as the Indian festival of spring, the festival of colours or the festival of love"))
def Baisakhi():
    print(bot_template.format("Baisakhi is a historical and religious festival in Sikhism and Hinduism. It is usually celebrated on 13 or 14 April every year, and celebrates the start of the month of Vaisakha. For Sikhs, [5][6][7][8] the day commemorates the formation of Khalsa panth of warriors under Guru Gobind Singh"))
def Bihu():
    print(bot_template.format("Bihu  is Mainly celebrated in east india . Indian State ASSAM "))
def poram():
    print(bot_template.format("Pooram  is an annual festival, which is celebrated in temples dedicated to goddesses Durga or Kali held especially in Valluvanadu area and other adjoining parts of north-central Kerala after the summer harvest."))
def eidulfitr():
    print(bot_template.format("Eid ul-Fitr also called the Festival of Breaking the Fast, is a religious holiday celebrated by Muslims worldwide that marks the end of the month-long dawn-to-sunset fasting of Ramadan."))
def rathyatra():
    print(bot_template.format("Ratha Yatra (also called as Car Festival or Chariot Festival) is a Hindu festival associated with Lord Jagannath held at Puri in the state of Odisha, India."))
def rakhi():
    print(bot_template.format("the tie or knot of protection where Raksha stands for the protection and Bandhan signifies the verb to tie.The bonding between a brother and a sister is simply unique and is beyond description in words"))
def aug_15():
    print(bot_template.format("August 15 , independence dayis the celebration of the freedom we won from the British rule on August 15, 1947. On this day, India witnesses a huge celebration of independence with tricolor flag hoisting, parades and cultural functions across the country. "))
def krishna():
    print(bot_template.format("Janmashtami or Gokulashtami, is an annual Hindu festival that celebrates the birth of Krishna, the eighth avatar of Vishnu."))
def ganesh():
    print(bot_template.format("Ganesh Chaturthi is also known as Vinayaka Chaturthi. It is one of the most significant Hindu festival dedicated to Lord Ganesha, son of Lord Shiva and Goddess Parvati."))
def onam():
    print(bot_template.format("Onam is an annual holiday and festival celebrated in Kerala, India. It is also a harvest festival, and falls on the 22nd nakshatra Thiruvonam in the Malayalam calendar month of Chingam, which in Gregorian calendar overlaps with August–September"))
def durga():
    print(bot_template.format("Durga Puja , also called Durgotsava , is an annual Hindu festival originating in the Indian subcontinent which reveres and pays homage to the Hindu goddess, Durga.\n It is particularly popular in the Indian states of West Bengal, Assam, Bihar, Tripura, and Odisha"))
def dussehra():
    print(bot_template.format("Vijayadaśamī, also known as Dussehra,  is a major Hindu festival celebrated at the end of Navaratri every year. It is observed on the tenth day in the Hindu calendar month of Ashvin or Kartik"))
def Diwali():
    print(bot_template.format("Deepavali is the Hindu festival of lights,Diwali symbolizes the spiritual victory of light over darkness, good over evil, and knowledge over ignorance"))
def Gurupurab():
    print(bot_template.format("A Gurpurab in Sikh tradition is a celebration of an anniversary of a Guru's birth marked by the holding of a festival"))
def Christmas():
    print(bot_template.format("Christmas (or Feast of the Nativity) is an annual festival commemorating the birth of Jesus Christ, observed primarily on December 25 as a religious and cultural celebratio"))
def eve ():
    print(bot_template.format("New Year's EVE,the last day of the year, is on 31 December. In many countries, it is celebrated at evening parties, where many people dance, eat, drink, and watch or light fireworks.")) 
def main_part ():
    print(bot_template.format("Type us any month to know about the festivals :- \n\t 1 for January \n \t 2 for february \n\t 3 for march "))
    print("\t 4 for April \n \t 5 for May \n\t 6 for June \n\t 7 for July \n\t 8 for August \n\t 9 for September")
    print("\t 10 for October \n\t 11 for November \n\t 12 for December " )
    a = int(input("USER :- "))
    if a == 1 : 
        print(bot_template.format("January and festivals are :- \n\t 1: New Year 2: Makarsakranti 3: Pongal 4: Republic Day "))
        print (bot_template.format("\nEnter your Choice:--> "))
        ch = int(input("USER :- "))
        if ch == 1 :
            newyear()
        elif ch == 2 :
            makrskn()
        elif ch == 3 :
            pongal()
        elif ch == 4 : 
            republicday()
        else: print(bot_template.format("No More Festivals!"))
    elif a==2:
        print(bot_template.format("February : 1. MahaShivratri \n\t\t 2. Valentine Day "))
        ch = int(input ("USER :- "))
        if ch==1: shivratri()
        elif ch==2: Valentine()
        else : input("USER :-  Your Question Please ")		
    elif a==3: 
        print(bot_template.format("March :- Holi "))
        holi()
    elif a==4 : 
        print(bot_template.format("April : 1. Baisakhi  2. Bihu"))
        ch = int(input ("USER :- "))
        if ch==1:
            Baisakhi()
        elif ch==2 :
            Bihu()
    elif a==5 : 
        print(bot_template.format("May :  1. Thrissur Pooram  2. Eid -Ul Fitr"))
        ch = int(input ("USER :- "))
        if ch==1: poram()
        elif ch==2: eidulfitr()
    elif a==6: 
        print(bot_template.format("June  :-  Ratha Yatra "))
        rathyatra()
    elif a ==7:
        print(bot_template.format("July :- no festivals :("))
    elif a == 8 :
        print(bot_template.format(" August  :- 1.Rakhshabhandhan  2.Janamashthami  3.Independenced Day   4.Onam  5.Ganesh Chathurthi"))
        print (bot_template.format("Enter your Choice:--> "))
        ch = int(input("USER :- "))
        if ch == 1 : rakhi()
        elif ch == 2 : krishna()
        elif ch == 3 : aug_15()
        elif ch == 4 : onam()
        elif ch == 5 : ganesh()
    elif a == 9:
        print(bot_template.format("September :- no festivals :("))
    elif a== 10 :
        print(bot_template.format("October :- 1. Durga Pooja  2. Dussehra"))
        ch = int(input ("USER :- "))
        if ch==1: durga()
        elif ch==2: dussehra()
    elif a== 11 : 
        print(bot_template.format("November :- \t1.Diwali \t2. Gurupurab"))
        ch = int(input ("USER :- "))
        if ch==1: Diwali()
        elif ch==2: Gurupurab()
    elif a== 12 : 
        print(bot_template.format("December :- 1. Christmas  2. New Year's Eve "))
        ch = int(input ("USER : "))
        if ch==1: Christmas()
        elif ch==2: eve() 
    else : 
        print(bot_template.format("End of months !! Any other Query? \n if yes let us know:- "))
        query = input()
bot_template = "BOT : {0}"
input("USER:  ")
print(bot_template.format("Hi...! Welcome !  \n  We can assist you with the knowledge of festivals! "))
main_part()
while True:
    var = input("\nYou want to continue , if yes type Y or y !")
    if var == 'y' or var == 'Y':
        main_part()
    else:
        print(bot_template.format("\t -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.\n  Thank you I think you enjoyed!! the time with us\n    \n"))
        exit(0)