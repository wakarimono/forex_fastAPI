from requests_html import HTMLSession

class Scraperates():

    def scrapedatarates(self):
        url = f'https://docs.google.com/spreadsheets/d/e/2PACX-1vT8WeyHFH8o7o4T0g_x0Fuchzb0Bw3Bf90Qs8X55LgrP3jUDJ4GG5hFsLGLZo397nT8rtdBUEF3ylis/pubhtml'
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)

        qlist = []

        forex = r.html.find('div.ritz')
        print(forex)
        for q in forex:
            item = {    
                'iso': q.find('td.s0', first=True).text.strip(),
                'taux': q.find('td.s1', first=True).text.strip(),
            }
            print(item)
            qlist.append(item)
        
        return qlist
            


forex = Scraperates()

forex.scrapedatarates()
