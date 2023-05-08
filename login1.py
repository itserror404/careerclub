#!/usr/bin/python3
import cgi

print("Content-type: text/html\n\n")
css_styles = """
<style>
    body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        background-color: #f0f0f0;
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
"""
formv = cgi.FieldStorage()

email = formv["email"].value
password = formv["password"].value

myfile = open("database10.txt", "r")
match = 0
for line in myfile:
    line = line.rstrip("\n")
    items = line.split(":")
    if (items[3] == email) and (items[0] == password):
        match = 1
        print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Access Granted</title>
    {css_styles}
</head>
<body>
    <!-- Navigation -->
    <div class="nav">
        <a class="nav-left" href="grpprj.py">The Career Club</a>
        <a href="internships.html">Internships</a>
        <a href="jobs.html">Jobs</a>
        <a href="employers.html">Employers</a>
        <a href="events.py">Events</a>
        <a href="inbox.html">Login</a>
    </div>
    <div class="container">
        <h2 style="text-align: center;">Access Granted!</h2>
        <p style="text-align: center;">Congrats {items[2]}, you have access to the website</p>
    </div>
</body>
</html>
""")
        break

if match == 0:
    print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
    {css_styles}
</head>
<body>
    <!-- Navigation -->
    <div class="nav">
        <a class="nav-left" href="grpprj.py">The Career Club</a>
        <a href="http://i5.abudhabi.nyu.edu/~ym2306/Project/internships.html">Internships</a>
        <a href="http://i5.abudhabi.nyu.edu/~ym2306/Project/jobs.html">Jobs</a>
        <a href="http://i5.abudhabi.nyu.edu/~ym2306/Project/employers.html">Employers</a>
        <a href="http://i5.abudhabi.nyu.edu/~ym2306/Project/events.html">Events</a>
        <a href="http://i5.abudhabi.nyu.edu/~ym2306/Project/inbox.html">Login</a>
    </div>
    <div class="container">
        <h2 style="text-align: center;">Access Denied!</h2>
        <p style="text-align: center;"><a href='login3.py' style='color: #37352f; text-decoration: underline;'>Wrong password: go back to enter password again</a></p>
    </div>
</body>
</html>
""")

