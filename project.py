'''import requests
base_url="http://stackoverflow.com/tags?" 
url_list = ["{}page={}&tab=popular".format(base_url, str(page)) for page in range(1, 28)]

for url in url_list:
	response=requests.get(url)
	with open('stack_overflow_data.txt','a') as stack_overflow:
		stack_overflow.write(response.text)
'''


from bs4 import BeautifulSoup
with open('stack_overflow_data.txt','r') as stack_overflow:
	html_soup=BeautifulSoup(stack_overflow, 'html.parser')

tags=[]
votes=[]
today=[]
day=[]
week=[]

tag_containers=html_soup.find_all('div', class_ = 's-card')

vote_containers=html_soup.find_all('div', class_ = 'mt-auto grid jc-space-between fs-caption fc-black-300')

today_containers=html_soup.find_all('div',class_='grid--cell s-anchors s-anchors__inherit')

for i in tag_containers:
	tags.append(i.a.text)

for i in vote_containers:
	votes.append(i.div.text.strip('questions'))
	
for i in today_containers:
	today.append(i.text)

for i in today:
	container=[]
	container=i.split(',')
	if container[0].endswith('asked today'):
		day.append(container[0].strip('asked today'))
	else:
		day.append('0')
	if len(container)>1:	
		if container[1].endswith('this week'):
			week.append(container[1].strip('this week'))
		else:
			week.append('0')
	else:
		week.append('0')
		
data= "{:<35}  | {:^30} | {:^10} | {:^10}".format("Tag Name","Number Of Queries","Per day","Per week")
print(data)
print()

for i in range(0,len(tags)):
	data= "{:<35}  | {:^30} | {:^10} | {:^10}".format(tags[i],votes[i],str(day[i]),str(week[i]))
	print(data)

import matplotlib
import matplotlib.pyplot as plt
import numpy as np



labels = tags[:10]
per_day = day[:10]
per_week = week[:10]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, per_day, width, label='Per Day')
rects2 = ax.bar(x + width/2, per_week, width, label='Per Week')



# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Questions')
ax.set_title('Tags vs Questions')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()



fig.tight_layout()

plt.show()


import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = tags[:15]
energy = votes[:15]

x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, energy, color='green')
plt.ylabel("Tags")
plt.xlabel("Questions Asked")
plt.title("Tags vs Questions Asked")

plt.yticks(x_pos, x)

plt.show()



'''labels = tags[:10]
sizes = votes[:10]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()'''






