class alltop(object):


    # need to add code to determine which URL to hit.
    URL = 'http://database.alltop.com/'
    #URL = newFunction(object):

    @staticmethod
    def get_results(*args):
        html = urllib2.urlopen(Alltop.URL)
        soup = BeautifulSoup(html)
        topular_ul = soup.find('ul', {'id': 'top-five'})
        results = []
        if len(topular_ul) > 0:
            #page has topular sites, for some topics it's empty
            for idx, entries in enumerate(topular_ul.find_all('li', {'class':  'hentry'})):
                a = entries.find('a')
                en = a.get_text().encode('ascii', 'ignore')
                hr = a.get('href')
            for entry in entries.find_all('div', {'class':  'full-post'}):
                site = entry.find('div', {'class':  'site-title'}).get_text().encode('ascii', 'ignore')
                date = entry.find('div', {'class':  'published'}).get_text().encode('ascii', 'ignore')
                desc = entry.find('div', {'class':  'entry-bound'}).get_text().encode('ascii', 'ignore')
                results.append({
                    'title': en,
                    'url': hr,
                    'desc': desc,
                    'date':'',  #took out date
                    'content_type':'Article',
                    'author': site,
                    'id': '',
                })
        return results


