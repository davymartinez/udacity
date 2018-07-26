# Define a procedure, crawl_web(), that takes as input a seed page URL, and
# outputs a list of all the URLs that can be reached by following links starting
# from the seed page.

# opens an url into an utf-8 decoded text
def get_page(url):
    import urllib.request
    try:
        with urllib.request.urlopen(url) as response:
            # decodes html to utf-8, otherwise it returns bytecode, not string
            html = response.read().decode('utf-8')
            return html
    except:
        # print this if no url's are found later on when called
        print('none found')
        return ''

# gets every <a href= instance in the passed html page, returning the
# correspoding url link and ending quotation mark
def get_next_target(page):
    start_link = page.find('<a href=')  # first occurrence of <a href=
    if (start_link == -1):              # find() returns -1 if nothing found
        return None, 0
    else:
        # find the first quotation after start_link
        start_quote = page.find('"', start_link)
        # find the ending quotation after start_quote
        end_quote = page.find('"', start_quote + 1)
        # slices the url using the two previous vars
        url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links_list = []
    while True:                             # while there are links in the html
        url, endpos = get_next_target(page) # run the get_next_target() method
        if url:                     # if an url is found
            links_list.append(url)    # push it into list
            page = page[endpos:]    # set the ending position to continue
                                    # searching for links
        else:
            break
    return links_list

# start with to_crawl = [seed]
# crawled = []
# while there are more pages to_crawl:
#     pick a page from to_crawl
#     add that page to crawled
#     add all the link targets on this page to to_crawl
# return crawled

def crawl_web(seed):
    to_crawl = [seed]
    crawled = []
    while (to_crawl):
        page = to_crawl.pop()
        links = get_all_links(get_page(page))
        if (page not in crawled):
            # 1. update the value of to_crawl to reflect
            #    all the new links that are found on page
            # 2. update the value of crawled to keep track
            #    of the pages that have been crawled
            union(to_crawl, links)
            crawled.append(page)
    return crawled

print(crawl_web('https://udacity.github.io/cs101x/index.html'))
