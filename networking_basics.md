### Basic networking concepts

Computers on the internet have addresses that allow them to be found. These numbers are called IP addresses, and look something like this:

173.194.205.100
31.13.76.68
128.228.38.47

See if you can figure out who these IP addresses belong to. Try copying them out and pasting them in the URL bar in your browser.

The domain names we're familiar with, like google.com, are like masks. They cover these unfriendly-looking numbers, making them easier for humans to read and remember. A complicated mapping system called DNS is responsible for resolving domain names into IPs and vice versa.


### Servers and requests

Every time you enter a domain (or IP) in your browser, you're requesting information from another computer that's connected to the internet. The procedure (or "protocol") for these requests is called HTTP.  The two most common types of HTTP request are GET and POST. GET allows you to receive information from another computer, and POST allows you to send information to another computer.

At the other end of every request that you make is a server. A server is a program that listens for some kind of input and performs some action when that input is detected. Servers on the internet take GET and POST requests and return HTML markup. Your browser then takes that markup and renders it.

Open up your terminal and run:

```
GET https://en.wikipedia.org/wiki/The_Starry_Night
```

You should see HTML as the output. Awesome...you just talked to a server! Of course, we talk to servers every day, but let's not spoil the moment.

[Next >>> What's a Web Framework?](frameworks.md)
