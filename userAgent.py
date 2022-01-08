# pip install my_fake_useragent

from my_fake_useragent import UserAgent as u


while True:
    ua=u(family='chrome', os_family='windows')
    re=ua.random()
    
    fin={'User-Agent':f'{re}'}
    print(fin)
    
    
    