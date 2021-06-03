# picoCTF Cookies

## Problem Description
Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:54219/

## Background Knowledge
To solve this problem, you'll have to understand what a HTTP cookie is and will need the ability to view your current cookie. 

### Did Someone Say Cookies?
HTTP cookies are key-value pairs that are used to identify your device as you browse a website. A cookie is unique to a user's session.

### How To View Your Cookie
You have a few different options to view your current cookie. I chose to use [EditThisCookie](http://www.editthiscookie.com/). 
It's a browser extension that allows you to view and modify cookie properties. To read more about cookie properties, click [here](http://www.editthiscookie.com/blog/2014/03/cookie-properties/).

## The Solution
When you view your cookie on the main page, your cookie will have a value of *-1*. 
You'll also see that "snickerdoodle" is the default text in the searchbar. Submit "snickerdoodle" to the website, and check the cookie on the */check* page once you're redirected.
It'll have a value of *0*. 

At this point, I made the assumption that iteration would eventually lead me to the flag. So, I tried to find the max range for the cookies. 
I did this by guessing. I started with 30, then 25, and iterated up to *28*. There are 29 possible cookies (0-28). One of them contains the flag. 

I wrote a BASH script to iterate through the possible cookies and identify which one had the flag. The code is below. 
Save the script as "cookie.sh"

```bash
    #!/bin/bash
    for i in {0..28}
    do
        curl --cookie "name=$i" "http://mercury.picoctf.net:54219/check"
    done
```
    
To run the above script, execute the following in your Linux CLI: `chmod +x cookie.sh && ./cookie.sh | grep -oE "picoCTF{.*}" > flag.txt`

The flag will be saved in a text file called *flag.txt.*

## Flag
##### picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}
