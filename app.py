import requests, sys, os
from urllib import request
from bs4 import BeautifulSoup
def down(url,sl): 
    file_name = url.split('?')[1].split('&')[2].split('=')[1]+'_'+url.split('?')[1].split('&')[1].split('=')[1]
    if sl==5:
        file_name = 'lec'+url.split('?')[1].split('&')[2].split('=')[1]+'.pdf'
    with open(file_name, "wb") as f:
            print("Downloading %s" % file_name)
            res = requests.get(url , stream=True)
            l = res.headers.get('content-length')
            if l is None:
                print("downloading...")
                f.write(res.content)
            else:
                dl = 0
                l = int(l)
                for data in res.iter_content(chunk_size=1024):
                    dl += len(data)
                    f.write(data)
                    done=int(50*dl/l)
                    sys.stdout.write("\r[%s%s] %s%%" % ('█' * done, ' ' * (50-done),(done*2)) )    
                    sys.stdout.flush()
link =" https://nptel.ac.in/courses/nptel_download.php?subjectid=106106182"
link = str(input("Please enter NPTEL download_page URL : ")) 
print("Fetching URL...")
r = request.urlopen(link)
bytecode = r.read()
htmlstr = bytecode.decode()
soup = BeautifulSoup(htmlstr, "html.parser")
mp4=[] 
flv=[]
f3gp=[]
pdf=[]
mp3=[]
urls = soup.find_all('a', href=True)
print("done.") 
i=0 
while i<len(urls):
    if urls[i].text=='MP4 Download':
        mp4.append(urls[i]['href'])
    elif urls[i].text=='FLV Download':
        flv.append(urls[i]['href'])
    elif urls[i].text=='3GP Download':
        f3gp.append(urls[i]['href'])
    elif urls[i].text=='Download MP3':
        mp3.append(urls[i]['href'])
    elif urls[i].text=='English(PDF)':
        pdf.append(urls[i]['href'])
    else:
        pass
    i+=1
print('[1]MP4 : %s files available \n[2]FLV : %s files available \n[3]3GP : %s files available \n[4]MP3: %s files available \n[5]PDF : %s files available' % (len(mp4), len(flv), len(f3gp),len(mp3),len(pdf)))
sl=int(input('\nplease choose file type(1/2/3/4/5) : '))
path_loc=str(input("Enter Path : "))
if not os.path.exists(path_loc):
    os.makedirs(path_loc)
os.chdir(path_loc)
lis=[mp4,flv,f3gp,mp3,pdf]
for url in lis[sl-1]:
    if sl!=5:
        url="https://nptel.ac.in"+url
    down(url,sl)
    print('file downloaded')



