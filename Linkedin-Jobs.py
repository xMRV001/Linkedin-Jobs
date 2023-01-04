# linkedin jobs
import os
try:
  import requests
  from bs4 import BeautifulSoup
  from sty import fg, bg, ef, rs
  import time
except ImportError:
  print("Installing requirements to run.".capitalize)
  lis = ('requests', 'bs4', 'sty')
  for i in lis:
    os.system(f'py -m pip install {i}')

print(fg(0, 255, 51) + " Yay! , You have everything Ready" + fg.rs)
print(fg.red + " ~ This code was written by @xMRV001 " + fg.rs)
work = input('What Are You Looking for : ')
place = input('What Country : ')
url = f"https://www.linkedin.com/jobs/search?keywords={work}&location={place}"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'bcookie="v=2&7378c491-8f1d-4939-8d93-b105318c26e7"; bscookie="v=1&202301040027223d66972e-b043-41a0-850c-23432184124fAQFox_TgFxSEj-VGmjVKAHr-wzerQ6AL"; G_ENABLED_IDPS=google; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; aam_uuid=36388895031035993022919358053889930363; _gcl_au=1.1.1821253020.1672792626; timezone=Asia/Shanghai; li_theme=light; li_theme_set=app; _guid=33e52a31-2ea0-49a5-b9e4-f7bdf030d283; li_sugr=71806bb7-d4a6-4367-8e6b-92a51aa4d503; UserMatchHistory=AQInjMIAhjuscgAAAYV6Nec17IXczdxHSLbCQSZSNQLI5QtyzA36XrOlqh6Uo6-ERVA7qTXgBN1KwI1VjTbDjPgXvFNCsj13YAz14BXKDIH1HJS3RpvBZ0pvYwIN5iO0-Ik_MKlSW8KFXRzkIiFN-R_lTZAkRBIP4vFhD8_fej_7lUXs5b_ug_bk4aRcDx15eXEdwiUPgP_PpqFF61gsxcFq5eZ7PnXXwN6g6B4mDYetUsE-ZIfi-Ts3utHElV20sNQzc3v4p3OWirhpldAEsOjs6f-sfAy61laHqd0; AnalyticsSyncHistory=AQKtvpM9i1rCmAAAAYV6Nec1jn-yGtw-jyPDH3iaildRJkqIaoTRJZSHCJs8OLBHYJ7uLzysl2Fp773_RJF6kw; lms_ads=AQHgdOSy7SBDJgAAAYV6Nef3tg866DLRxMpsy5OPB0ItiDtFML5lT3FUVL9fjM53_9n8Gd6oQXZiFJ_e-d_2mwPRTQCHvqih; lms_analytics=AQHgdOSy7SBDJgAAAYV6Nef3tg866DLRxMpsy5OPB0ItiDtFML5lT3FUVL9fjM53_9n8Gd6oQXZiFJ_e-d_2mwPRTQCHvqih; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19362%7CMCMID%7C36526320771474188932903849318974359472%7CMCAAMLH-1673397432%7C6%7CMCAAMB-1673397432%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1672799832s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C1399497307; li_rm=AQEZXFebP1E5-AAAAYV6N4opIie3MMTXK399UqRKGVk9tZetwXH0P3KZTsVpFq6jhu6I6G_WBXN3UvrdiDIgUIb4VKzMpicBkVx3wHRYiofcRbOLoevXcd_x; li_g_recent_logout=v=1&true; visit=v=1&M; JSESSIONID=ajax:0592569932292334488; lang=v=2&lang=en-us; lidc="b=VGST04:s=V:r=V:a=V:p=V:g=2807:u=1:x=1:i=1672792741:t=1672879141:v=2:sig=AQGHI3uqVstHMHkBEBe74sN7D25y6yNQ"; recent_history=AQHwTY5KxvneewAAAYV6OIbG2Xn7Yzq3vmFZNdAL60FYaIwoN9etsMn0MgV0HF0DQ0PL34qxW4zMi2BdOQdIoc-g1jfJibwWq0avOqPq4fb3-rf01lgMt3xT9kIjgiJauMSZonVQOi3p17d8y9iuhbavYAAMk7T2WLW5WVbCPmhcuz3uaYD8zLG8-rPq9g3RByD0qQh6icuTmQ8xKFB2fXSa4Sg7DMF_qoG_3Ups2e36HPVGD_0wYFN4_hqbjWRdOl1aoIdUM3fPBpOdpkpAx11vqpm5Gay55TAHFGEHYL3xCKxkPnFBCRUroPwpgU7isbGL8E6fFzFzMZnES0p_jpsHBi2FRpZVvuUo2g',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

login = requests.get(url, headers=headers)


soup = BeautifulSoup(login.text, "html.parser")


link = soup.find_all("a",{"class":"base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]"})
try:
    with open('jobs.txt', 'w') as f:
        for i in link:
            z = i.get("href")
            print(z)
            time.sleep(0.5)
            f.write(str(z + '\n'))
except Exception as e:
    print(e)
