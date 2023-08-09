from bs4 import BeautifulSoup
import requests
   

html_text = requests.get('https://ccse.kennesaw.edu/cs/about/faculty-staff.php')

# print(html_text.content)

soup = BeautifulSoup(html_text.content, 'lxml')

ul = soup.find('ul', {'class': 'fac_staff_listing'})



lis = ul.findAll('li')

txt = ''

for li in lis:

    name = li.find('h3')
    email = li.find('a')


    role = li.find('span', {'class': 'col_2'})
    name = name.get_text().strip() if name else ''
    role = role.get_text().strip() if role else ''
    email = email.get_text().strip() if email else ''

    more_info = li.find('div', {'class': 'more_info'})
    paras = more_info.findAll('p')

    # position = ''
    phone = ''
    location = ''

    for p in paras:

        text = p.get_text().lower()

        # if len(location) > 0 and 'location:' in text:
        #     idx = text.index('location:')
        #     text = text[:idx]

        # print(text)

        # if p is not None and 'location:' in text:

        #     idx = text.index('location:')

        #     location = text[idx:].replace('location:', '').strip()
            
            

        if p is not None and 'phone:' in text:

            # print('MSCS faculty')
            idx = text.index('phone:')

            phone = text[idx:].replace('phone:', '').strip()

    txt += "%s is %s and connected through %s\n  %s \n \n  \n \n" % (name, role, email, phone )
# with open('MSCS.txt','w') as f:
with open('MSCSdata.txt','w') as f:

    f.write(txt)
    f.write('=====================================================================================================================================================')
   

# loc= li.div.p.

