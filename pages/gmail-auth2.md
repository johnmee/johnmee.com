title: How to use Google's API to send an email
published: 2014-10-20
comments: False
tag: technical


A simple question with a complex answer...


# How to send an email through gmail without enabling "insecure access"

> `"Upgrade to a more secure app that uses the most up to date security measures"`

Just seen this error message instead of sending emails?

Google are pushing to improve the security of script access to their gmail smtp servers.  I have no problem with that.  In fact I'm happy to help.
But they're not making it easy.  We've all got a lot of code that look like this and no suggestions what to replace it with:

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    server.sendmail(FROM, TO, MESSAGE)
    server.close()

Turning on "Access for less secure apps" let's us leave it there, but that's not the solution they're really going for.
This was painful, but I seem to have worked it out for now...


## Navigating the Google website is half the battle

No doubt, over time, this will change.  Ultimately you need to download a `client_secret.json` file.  You can only 
(probably) do this setting up stuff via a web browser:

1. You need a google account - either google apps or gmail. So, if you haven't got one, go get one.
1. Get yourself to the [developers console](https://console.developers.google.com/)
1. Create a new project, and wait 4 or 400 seconds for that to complete.
1. Navigate to `API's and Auth` -> `Credentials`
1. Under `OAuth` select `Create New Client ID`
1. Choose **`Installed Application`** as the application type and **Other**
1. You should now have a button `Download JSON`. Do that.  It's your `client_secret.json`—the passwords so to speak

But wait that's not all!

**You have to give your application a "Product Name"** to avoid some really weird errors
which might seem completely unrelated to this, but actually are.  (I really suffered for this ;-)

1. Navigate to `API's & auth` -> `Consent Screen`
1. Choose your email
1. Enter a PRODUCT NAME.  It doesn't matter what it is. "Foobar" will do fine.
1. Save

Yay. Now we can update the emailing script.


### Python3 is not supported (yet)

I don't think it will be too hard to attain, as I was stumbling through converting packages without hitting anything 
massive: just the usual 2to3 stuff.  Yet after a couple of hours I got tired of swimming upstream.  At time of writing, 
I couldn't find a published package for public consumption for Python 3.  The python 2 experience was straight-forward 
(in comparison).

## Python 2

You need to run the script interactively the first time.  It will open a web browser on your machine and you'll grant 
permissions (hit a button).  This exercise will save a file to your computer `gmail.storage` which contains a reusable 
token.  I don't know if it is transferable to a machine which has no browser functionality. Maybe you can answer that 
in the comments for us.

First you need some libraries:

    pip install --upgrade google-api-python-client
    pip install --upgrade python-gflags

And finally! some code:
Obviously you need to change the to and from addresses.

```{.python}
import base64
import httplib2

from email.mime.text import MIMEText

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run


# Path to the client_secret.json file downloaded from the Developer Console
CLIENT_SECRET_FILE = 'client_secret.json'

# Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/gmail.compose'

# Location of the credentials storage file
STORAGE = Storage('gmail.storage')

# Start the OAuth flow to retrieve credentials
flow = flow_from_clientsecrets(CLIENT_SECRET_FILE, scope=OAUTH_SCOPE)
http = httplib2.Http()

# Try to retrieve credentials from storage or run the flow to generate them
credentials = STORAGE.get()
if credentials is None or credentials.invalid:
  credentials = run(flow, STORAGE, http=http)

# Authorize the httplib2.Http object with our credentials
http = credentials.authorize(http)

# Build the Gmail service from discovery
gmail_service = build('gmail', 'v1', http=http)

# create a message to send
message = MIMEText("Message goes here.")
message['to'] = "yourvictim@goes.here"
message['from'] = "you@go.here"
message['subject'] = "your subject goes here"
body = {'raw': base64.b64encode(message.as_string())}

# send it
try:
  message = (gmail_service.users().messages().send(userId="me", body=body).execute())
  print('Message Id: %s' % message['id'])
  print(message)
except Exception as error:
  print('An error occurred: %s' % error)
```

Hopefully that gets us all started.  Not as simple as the old way, but does look a lot less complicated now I can see it in the flesh.


Head for [stackoverflow for the latest on this discussion](http://stackoverflow.com/questions/25944883/how-to-send-an-email-through-gmail-without-enabling-insecure-access).
