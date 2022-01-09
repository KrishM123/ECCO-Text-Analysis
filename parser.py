from util import *

def getSentence(link):
    sentence = ' '.join(getHTMLPage(link).split('<span class="kwic">')[1].split('</div>')[0].replace('<span class="hilite1">', '').replace('<span class="hilite2">', '').replace('<span class="hilite2">', '').replace('</span>', '').split(' ')[2:-2])
    return sentence

with open('elder.txt', 'w') as text:
    temp = getHTMLPage('https://quod.lib.umich.edu/e/ecco?type=boolean&rgn=works&q1=elder&op2=or&q2=old&op3=or&q3=senior&cite1=&cite1restrict=author&cite2=&cite2restrict=author&firstpubl1=1700&firstpubl2=1800&Submit=Search&size=2120').split('">Results details</a>')[:-1]
    print('Complete Step 1')
    pos = 0
    for link in [pos.split('"')[-1] for pos in temp]:
        try:
            text.write(getSentence(link) + '\n\n')
            pos += 1
            if pos == 5:
                print("WORKING")
                pos = 0
        except:
            print(link)
            pass
    text.close()