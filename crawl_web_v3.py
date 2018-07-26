#
# This question explores a different way (from the previous question) to limit
# the pages that it can crawl.
#
#######

# THREE GOLD STARS #
# Yes, we really mean it! This is really tough (but doable) unless you have
# some previous experience before this course.

# Modify the crawl_web procedure to take a second parameter, max_depth, that
# limits the depth of the search. We can define the depth of a page as the
# number of links that must be followed to reach that page starting from the
# seed page, that is, the length of the shortest path from the seed to the
# page. No pages whose depth exceeds max_depth should be included in the crawl.
#
# For example, if max_depth is 0, the only page that should be crawled is the
# seed page. If max_depth is 1, the pages that should be crawled are the seed
# page and every page that it links to directly. If max_depth is 2, the crawl
# should also include all pages that are linked to by these pages.
#
# Note that the pages in the crawl may be in any order.
#
# The following definition of get_page provides an interface to the website
# found at http://www.udacity.com/cs101x/index.html

# The function output order does not affect grading.

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
        elif url == "http://top.contributors/velak.html":
            return ('<a href="http://top.contributors/jesyspa.html">'
        '<a href="http://top.contributors/forbiddenvoid.html">')
        elif url == "http://top.contributors/jesyspa.html":
            return  ('<a href="http://top.contributors/elssar.html">'
        '<a href="http://top.contributors/kilaws.html">')
        elif url == "http://top.contributors/forbiddenvoid.html":
            return ('<a href="http://top.contributors/charlzz.html">'
        '<a href="http://top.contributors/johang.html">'
        '<a href="http://top.contributors/graemeblake.html">')
        elif url == "http://top.contributors/kilaws.html":
            return ('<a href="http://top.contributors/tomvandenbosch.html">'
        '<a href="http://top.contributors/mathprof.html">')
        elif url == "http://top.contributors/graemeblake.html":
            return ('<a href="http://top.contributors/dreyescat.html">'
        '<a href="http://top.contributors/angel.html">')
        elif url == "A1":
            return  '<a href="B1"> <a href="C1">  '
        elif url == "B1":
            return  '<a href="E1">'
        elif url == "C1":
            return '<a href="D1">'
        elif url == "D1":
            return '<a href="E1"> '
        elif url == "E1":
            return '<a href="F1"> '
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

# ANALYZE THIS:
def crawl_web(seed,max_depth): # max_depth parameter keeps track of search depth
    tocrawl = [seed]    # tocrawl list contains the seed page (depth == 0)
    crawled = []        # crawled list will hold already crawled links
    next_depth = []     # next_depth list will hold next level/depth of links
    depth = 0           # init depth variable to 0
    # check that tocrawl contains a url and that depth doesn't exceed max_depth
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()    # take a url from tocrawl and assign to page var
        if page not in crawled: # if the previous url hasn't been crawled yet:
            # join the next_depth and links lists with union()
            # (the links list is returned by get_all_links())
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)    # insert the crawled url into crawled
        # if the tocrawl list is empty (means that level/depth is finished):
        if not tocrawl:
            # assign next_depth to tocrawl and "empty" the next_depth list
            tocrawl, next_depth = next_depth, []    # this is a "swap"
            depth = depth + 1   # increase the depth variable by one
    return crawled

print(crawl_web("http://www.udacity.com/cs101x/index.html",0))
#>>> ['http://www.udacity.com/cs101x/index.html']

print(crawl_web("http://www.udacity.com/cs101x/index.html",1))
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html']

print(crawl_web("http://www.udacity.com/cs101x/index.html",50))
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']

print(crawl_web("http://top.contributors/forbiddenvoid.html",2))
#>>> ['http://top.contributors/forbiddenvoid.html',
#>>> 'http://top.contributors/graemeblake.html',
#>>> 'http://top.contributors/angel.html',
#>>> 'http://top.contributors/dreyescat.html',
#>>> 'http://top.contributors/johang.html',
#>>> 'http://top.contributors/charlzz.html']

print(crawl_web("A1",3))
#>>> ['A1', 'C1', 'B1', 'E1', 'D1', 'F1']
#(May be in any order)
