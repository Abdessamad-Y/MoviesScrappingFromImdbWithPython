# IMDB_TopMovies
Are you bored from bingewatching Netflix and you are looking to review old classic movies that are the top of the top 
I have the solution for that This code bellow will scrape imdb and giving you the top movies 



## 1-Dependencies
Make sure that you have the following dependecies intalled by using pip intall :

1. BeautifulSoup
2. requests
3. tqdm
## 2-Execution
``` python Imdb-top-movies-scrapper.py ```

### Let me explain the code below :
#### 1-Dependencies:
we use the python libraries:

-Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

-Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

-tqdm just to add loading bar 

#### 2-How the code works:
first of all you need to access the page that you want to scrape in the web mine is :
https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc
It should look like this 

![Alt text](Images/index%20page.JPG "index page")

next I want you to press ctrl+shift+i on your chrome webpage and you should see a page pop on the right side wich will give you the page similar to the following example:
![Alt text](Images/tags%20and%20images.png "code html to the side ")
where we can see the html tags that define each elements of the page 
```html
<h2>This is the code of the html page</h2>

<div class = "lister-list">
  <div class = "lister-item mode-advanced">
    .
    .
    <div class = "lister-item-content">
      <h3 class = "lister-item-header"> <!-- this is the elemnt we are looking for wich represent the title of the movie -->
        ...
        <a href = "/title/..."></a> --> Movie title
        ...
      </h3>
    </div>
    .
    .
  </div>
  <div class = "lister-item mode-advanced">
    .
    .
    .
  </div>
  <div class = "lister-item mode-advanced">
    .
    .
    .
  </div>
  .
  .
  .
</div>
```


``` python	code 

movies = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'}) # this code is used to scrape all the div elemnts from the websites wich contain a div with class lister-item mode-advanced
for div_item in tqdm(movies): #we are gonna loop all the div found earlier 
    div = div_item.find('div', attrs={'class': 'lister-item-content'}) # we get the class item contain lister 'item -content 
    header = div.findChildren('h3', attrs={'class': 'lister-item-header'}) # and finnaly we get the title of the movie

```
and that's how you scrape the website feel free to add to the code if you like 