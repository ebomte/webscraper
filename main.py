import requests
from bs4 import BeautifulSoup
import pandas as pd


# give it a page, put page into the url, inside the function
def extract(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
    url = f'https://ie.indeed.com/jobs?q=software+engineer+intern&l=Ireland&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup  # when we run this, get info, then return the whole soup
    # we have to store into variable and give to next function transform

    # return r.status_code #just to check it works by returning 200 in command line


def transform(soup):
    divs = soup.find_all('div', class_='job_seen_beacon')  # open up the page,pass thorugh and find instances div is is this
    # loop through each div, and get its respective information
    for item in divs:
        title = item.find('span').text.strip()

        # if title == 'new':
        #     continue
        company = item.find('span', class_='companyName').text.strip()  # strip, removes whitespaces
        summary = item.find('div', {'class': 'job-snippet'}).text.strip().replace('\n', '')

        job = {
            'TITLE': title,
            'COMPANY': company,
            'SUMMARY': summary
        }
        joblist.append(job)
    return
    # print(f'{title}: {company}')


joblist = []

for i in range(0, 10, 10):
    print(f'Getting page, {i}')
    c = extract(i)
    transform(c)
    print(joblist)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
