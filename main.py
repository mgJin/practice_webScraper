from extractors.saramin import search_saramin
import datetime

dt = datetime.datetime.now()
keyword = input("what are you searching for ?")

results = search_saramin(keyword)

file = open(f"searching_{keyword}_job_in_{dt.date()}.csv","w",encoding="utf-8-sig")
file.write("Title,Link,Location,Career,Education,Worktime,Deadline,Company_link,Company_name\n")

for result in results:
  file.write(f"{result['title']},{result['link']},{result['location']},{result['career']},{result['education']},{result['worktime']},{result['deadline']},{result['company_link']},{result['company_name']}\n")

file.close()

