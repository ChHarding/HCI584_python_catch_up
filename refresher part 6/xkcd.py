# copy the content of this file into flas_app.py in the mysite folder on pythonanywhere.com
# Don't forget to copy start_page_bootstrap.html and multiple_thumbs.html from
# your templates folder into mysite/templates! (folder may need to be created first)



# flask server to scrape a random number of image URL links from Xkcd
import requests, os, bs4
from random import randint

def get_xkcd_image_URL(n:int):  # type hint
    ''' return url to image of comix number n'''
    url = 'http://xkcd.com' # base url
    n_str = str(n)
    url += "//" + n_str + "//"  # full comic page URL
    #print('page URL:', url)

    # Download the page.
    res = requests.get(url)
    res.raise_for_status() # will stop if request did not get 200 (e.g. if it got 404)

    # Use BSoup to find the URL of the comic image.
    soup = bs4.BeautifulSoup(res.text,  "html.parser")
    comicElem = soup.select('#comic img') # grab the img tag inside the id=comic div
    if comicElem == []:
        print('Could not find comic image.')
    else:
        imgURL = "http:" + comicElem[0].get('src') # get the link URL
        return imgURL

from flask import Flask, request, render_template
app = Flask(__name__)

# create page with image thumbnails
@app.route('/show_thumbs/', methods=["GET"])
def show_thumbs():

    num_thumbs_str = request.args["num_imgs"] # get value for key/name "num_imgs"
    try:
        n = int(num_thumbs_str)
    except:
        return n + " is invalid! Hit Back on your browser and try again"

    # analyse comment
    cmt = request.args["comment"]
    print("*****************************\n" + cmt)
    print("Comment contains", len(cmt.split()), "words")
    print("*****************************")

    url_of_img_list = []
    for x in range(n):
        random_int = randint(1, 2000)
        img_url = get_xkcd_image_URL(random_int)
        url_of_img_list.append(img_url)

    html_str = render_template('multiple_thumbs.html',
                                num_thumbs=str(n),
                                url_list=url_of_img_list
                              )
    return html_str

# start page, served as root
@app.route('/')
def start_page():
    return render_template('start_page_bootstrap.html')

# run app only if NOT deployed on pythonanywhere.com's servers which
# all have liveweb in their hostname
from socket import gethostname
if 'liveweb' not in gethostname():
    app.run(debug=False, port=8080)

