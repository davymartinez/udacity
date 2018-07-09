# Adapted from Udacity CS101 Intro to Computer City online course,
# Class 11 - How to Manage Data
# Lessons 34-37
# Found at: https://classroom.udacity.com/courses/cs101/lessons/48727569/concepts/486926830923

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

links = get_all_links(get_page('http://xkcd.com/353'))
print(links)