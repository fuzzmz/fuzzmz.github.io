title: Geek at the gym
date: 2015-01-18 21:22
slug: geek-at-gym
category: debug
tags: python, coding

What happens when a geek wants to go to a specific gym class but always finds it fully booked? Well, I decided to abuse their reservation page and write a quick and dirty script which tries to make a reservation.

Before we dive in the code I want to warn you again that this was a very quick project built for one specific gym class, so there are a lot of hardcoded things in it. It could use a clean-up and better structure, but hey, it worked for what I needed it for.

---

#The flow
The flow of the script is the following:

1. `login` - based on the user email and pin log in to the site
2. `grab session cookie` - the reservation request requires a valid session cookie
3. `make reservation` - actually make the reservation for the specific class

Basically, this can be written as:

```python
def main():
    memberemail = "random@random.com"
    memberpin = 1234
    classid = 7890
    cookie = login(memberemail, memberpin)

    make_reservation(cookie, classid, memberemail, memberpin)
```
The `classid` for a specific class can be found by going to the reservation page for your particular gym location and looking at the source code. Also note the `centerid` string corresponding to your gym.

For example, the monday morning cycling class has the following info:

```html
<input type="hidden" value="37752" name="classId"></input>
<input type="hidden" value="402" name="centerId"></input>
```

The easiest way to get this info is to just search for `classId` in the page source and match that with the class you want to attend.

---

##1. Login
In order to log in to the site we perform a post request to `http://www.worldclass.ro/includes/ajax/login-user.php` with the username and password and from the response we steal the session cookie.

```python
import urllib
import urllib2
```

We need the `urllib` and `urllib2` libraries in order to perform requests against the Worldclass gym website.

```python
def login(memberemail, memberpin):
    page = "http://www.worldclass.ro/includes/ajax/login-user.php"
    email = memberemail
    pin = memberpin
```

Our login function in which we define the login page url and the user email and password (pin) used to authenticate.

In order to get the session cookie we need to pass the email and pin to the login page. To do this we uncode them and do a post request against the page.

```python
    raw_params = {'email': email, 'pin': pin}
    params = urllib.urlencode(raw_params) # encode the params
    req = urllib2.Request(page, params) # form the request
    page = urllib2.urlopen(req) # open the page with our parameters
```

---

##2. Get session cookie
The post returns more than just what we need (the session id cookie), so we'll need to perform some aditional steps to get it.

```python
    cookies = page.info()['Set-Cookie'] # grab all returned cookies
    page.close()
    start = cookies.index('=') # find start of the PHPSESSID cookie
    end = cookies.index(' ') # find the end of the PHPSESSID cookie
    return cookies[start + 1:end - 1] # return our session cookie
```

---

##3. Make reservation
Now that we have the session cookie we can make the reservation to our desired class (defined by the `classid` variable).

```python
def make_reservation(cookie, classid, email, pin):
    page = 'http://www.worldclass.ro/includes/ajax/_book_class.php'
    classid = classid
    centerid = 402
    memberemail = email
    memberpin = pin
    outlook = "undefined"
    clubname = "Health Academy at the Grand"
```

As you can see, the request for the booking page needs a bit more information than the login one. The only things that you should change directly are the `centerid` and `clubname` variables.

Once this is done we can start building our request:

```python
    raw_params = {'classId': classid,
                  'centerId': centerid,
                  'memberEmail': memberemail,
                  'memberPin': memberpin,
                  'outlook': outlook,
                  'clubName': clubname}
```

Before performing the request we need to also add the session cookie to prove that we're indeed an actual user; after that we can perform the request.

```python
    cookies = urllib.urlencode({'PHPSESSID': cookie}) # encode the cookie
    params = urllib.urlencode(raw_params) # encode the parameters
    headers = {'Cookie': cookies} # add our cookie to the request header

    req = urllib2.Request(page, params, headers) # form our request
    page = urllib2.urlopen(req) # perform the reqest
    print page.read() # print the output to see if things are ok
```

That's it. Now all you have to do is put this script in crontab to be run every night starting from a fwe minutes before the bookings open until a few minutes after they start.

---

#TODO and :fa-github: code repository
The script could be improved to simplify ease of use. The following changes could make things easier:

1. Automatically match the `classid` and `centerid` based on user selection from a list instead of having the user look in the page source code;
2. Check if the booking was succesful and if not try again;
3. Instead of relying on the crontab/task scheduler to run the script every x minutes, move that logic in the script. That way it just needs to be started once and it'll keep running and retrying until the reservation is correct or a set timeout is reached.

Feel free to fork and submit pull requests. You can find the code on [:fa-github:fuzzmz/WorldclassGymBooking](https://github.com/fuzzmz/WorldclassGymBooking).
