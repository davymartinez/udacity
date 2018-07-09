# Adapted from Udacity CS101 Intro to Computer City online course,
# Class 5 - How to Repeat
# Lesson 30 - Quiz: Print All Links
# Found at: https://classroom.udacity.com/courses/cs101/lessons/48753036/concepts/487275580923
# Changed the get_page() given in the lesson as it didn't seem to work well with Python 3
# (original version of the method would return bytecode, not strings)

# opens an url into an utf-8 decoded text
def get_page(url):
    import urllib.request
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')  # decodes html content to utf-8, otherwise
            return html                             # it returns bytecode, not string
    except:
        print('none found')     # print this if no url's are found later on when called
        return ''

# gets every <a href= instance in the passed html page, returning the correspoding url link and
# ending quotation mark
def get_next_target(page):
    start_link = page.find('<a href=')  # first occurrence of <a href=
    if (start_link == -1):              # find() returns -1 if nothing found
        return None, 0
    else:
        start_quote = page.find('"', start_link)    # find the first quotation after start_link
        end_quote = page.find('"', start_quote + 1) # find the ending quotation after start_quote
        url = page[start_quote + 1:end_quote]       # slices the url using the two previous vars
    return url, end_quote

def print_all_links(page):
    while True:                             # while there are links in the html
        url, endpos = get_next_target(page) # run the get_next_target() method
        if url:                             # if an url is found
            print(url)                      # print it
            page = page[endpos:]    # set the ending position to continue searching for links
        else:
            break

print_all_links(get_page('https://udacity.github.io/cs101x/index.html'))
