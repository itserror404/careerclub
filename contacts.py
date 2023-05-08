#!/usr/bin/python3

import cgi

print("Content-type: text/html \n\n")

fdata = cgi.FieldStorage()  # uses cgi module to extract key=value from form (dict)

def htmlhead():
    print('''

    <!DOCTYPE HTML>
    <html>
    <head>
    <title> Contact Form </title>

    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.3);
            width: 400px;
        }

        .title {
            text-align: center;
        }

    </style>

    </head>
    <body>
    <div class="container">
        <h1>Thank You for Signing Up</h1>
        <hr>
    ''')

def getvalues():

    # get ALL THE DATA AT ONCE FROM DICTIONARY using for loop
    print("<p> Here is the submitted information: ")
    
    for key in fdata.keys():
        if key == "password":
            print("<p>" + key + ": " + "*" * len(fdata[key].value))
        elif key == "industry":
            industry_values = fdata.getlist(key)
            print("<p>Industry Preferences: " + ", ".join(industry_values))
        else:
            print("<p>" + key + ": " + fdata[key].value)

def htmlfooter():
    print('''
    </div></body></html>
    ''')

def main():
    
    htmlhead()

    getvalues()

    htmlfooter()

main()
