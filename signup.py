#!/usr/bin/python3
print("Content-Type: text/html\n\n")
print()

print("""<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">

<head>
<div>
<div>
<head>
  <link rel="stylesheet" href="nav.css">
</head>
  <div class="nav">
    <a class="nav-left" href="grpprj.py">The Career Club</a>
    <div class="navr">
      <a href="internships.html">Internships</a>
      <a href="jobs.html">Jobs</a>
      <a href="employers.html">Employers</a>
      <a href="events.html">Events</a>
      <a href="inbox.html" class="active">Login</a>
    </div>
  </div>
  </div>
  </div>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <style>
        
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }

        .title {
            text-align: center;
            font-size: 52px;
            font-weight: 700;
            color: #333;
            margin-bottom: 20px;
            font-family: Arial, sans-serif;
        }

        label {
            font-size: 14px;
            color: #666;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 5px 0; 
            font-size: 18px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button.primary {
            display: block;
            margin: 20px auto 0;
            padding: 15px;
            font-size: 20px;
            background-color: red; 
        }



    </style>
</head>




</html>
    <div>
        <div class="title">
            Sign Up
        </div>
        <form action="contacts.py" method="POST">
            <p><label for="username">Username:</label></p>
            <p><input type="text" name="username" required></p>
            <p><label for="email">Email:</label></p>
            <p><input type="email" name="email" required></p>
            <p><label for="password">Password:</label></p>
            <p><input type="password" name="password" required></p>
            <p><label for="industry">Industry Preferences:</label></p>
        <div style="display: flex; margin: 5px 0;">
            <div style="margin-right: 20px;">
                <input type="checkbox" id="Information Technology" name="industry" value="Information Technology">
                <label for="Information Technology">Information Technology</label>
            </div>
            <div style="margin-right: 20px;">
                <input type="checkbox" id="Healthcare" name="industry" value="Healthcare">
                <label for="Healthcare">Healthcare</label>
            </div>
            <div>
                <input type="checkbox" id="Finance" name="industry" value="Finance">
                <label for="Finance">Finance</label>
            </div>
        </div>


            <p><button class="primary" type="submit">Sign Up</button></p>
        </form>
    </div>
</body>
</html>
""")

