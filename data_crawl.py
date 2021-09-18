#import some libraries
import pandas as pd # create and store dataframe
import urllib.request, json # get json from website
from urllib.request import Request, urlopen
#Name the columns
df = pd.DataFrame(columns=["schoolYear","stt","studentCode","TOAN","VAN","LY","HOA","SINH","SU","DIA","GDCD","NGOAINGU","CODE_NGOAINGU","groupCode","groupName","HKTN","HKXH","A00","B00","C00","D01","A01"])
#run all students according to their ID code continuously
for i in range(0,1000):
  #handle exception for ID not found
  try:
    #expand number
    i_str = str(i);
    while (len(i_str) < 5):
      i_str = '0'+i_str
    print("crawling number "+i_str+"...")
    #link and get request
    my_url = "https://d3ewbr0j99hudd.cloudfront.net/search-exam-result/2021/result/020"+i_str+".json"
    req = Request(my_url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'})
    with urlopen(req) as url:
        data = json.loads(url.read().decode('utf-8'))
        temp_df = pd.json_normalize(data)
        df = df.append(temp_df,ignore_index=True)
  except urllib.error.HTTPError:
    continue
#drop down some unnecessary columns
df.drop(["schoolYear","stt","studentCode","groupName"],axis=1,inplace=True)
#export to CSV
df.to_csv('hcm.csv', encoding='utf-8',na_rep='NA')
print("Done")