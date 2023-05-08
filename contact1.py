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

        .nav {
            background-color: #fff;
            overflow: hidden;
            position: fixed;
            top: 0;
            right: 0;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            width: 100%;
            line-height: 1.1;
            z-index: 100;
            height: 60px;
            box-sizing: border-box;
        }

        .nav a.nav-left {
            margin-right: auto;
            font-size: 30px;
        }

        .nav a {
            color: #37352f;
            padding: 20px 16px;
            text-decoration: none;
            font-weight: 550;
            font-family: "Segoe UI", Frutiger, "Frutiger Linotype", "Dejavu Sans", "Helvetica Neue", Arial, sans-serif;
            font-size: 20px;
            font-style: normal;
            font-variant: normal;
            font-weight: 700;
            line-height: 1.1;
        }

        .nav a.active {
            background-color: #fff;
            color: #37352f;
            border-radius: 5px;
        }

        .nav a:hover {
            background-color: rgba(55, 53, 47, 0.08);
            color: #37352f;
            border-radius: 5px;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.3);
            width: 300px;
        }

        .title {
            text-align: center;
        }


    </style>

    </head>
    <body>
    <!-- Navigation -->
    <div class="nav">
        <a class="nav-left" href="#">The Career Club</a>
        <div>
            <a href="internships.html">Internships</a>
            <a href="jobs.html">Jobs</a>
            <a href="employers.html">Employers</a>
            <a href="events.py">Events</a>
            <a href="login3.py">Login</a>
        </div>
    </div>

    <div class="container">
        <h1>Thank You for Signing Up</h1>
        <hr>
    ''')

def getvalues():

    print("<p><h3> Thanks for your registration! </h3>")
    print("<p> Here is your information: ")

    line = ""
    
    for key in fdata.keys():
        if key == "password":
            print("<p>" + "Password " + ": " + "*" * len(fdata[key].value))
            line += fdata[key].value + ":"
        elif key == "industry":
            industry_values = fdata.getlist(key)
            print("<p>Industry Preferences: " + ", ".join(industry_values))
            line += ", ".join(industry_values) + ":"
        else:
            print("<p>" + key.capitalize() + ": " + fdata[key].value)
            line += fdata[key].value + ":"
    
    line += "\n"
    store(line)

def store(line):
    #open a file to append 

    filer = open("database10.txt", "a")

    #write to file
    filer.write(line)

    filer.close()

def htmlfooter():
    print('''
    </div></body></html>
    ''')

def main():

    htmlhead()

    getvalues()

    htmlfooter()

main()
