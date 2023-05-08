#!/usr/bin/python3
import cgi

print("Content-type: text/html \n\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
            padding-top: 60px;
            background-color: #f0f0f0 !important;
        }

        .title {
            text-align: center;
            font-size: 52px;
            font-weight: 700;
            color: #333;
            margin-bottom: 20px;
            font-family: Arial, sans-serif;
            margin-top: 250px; 
        }

        .footer{
            width: 100%;
            background-color: #f0f0f0 !important;
        }


        label {
            font-size: 14px;
            color: black;
            font-family: "Segoe UI", Frutiger, "Frutiger Linotype", "Dejavu Sans", "Helvetica Neue", Arial, sans-serif;
        }

        input {
            width: 95%;
            padding: 10px;
            margin: 5px 0;
            font-size: 18px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button.primary {
            background-color: #04AA6D !important;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 95%;
        }
        button.primary:hover {
        opacity: 0.8;
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

        .input-container {
            display: flex;
            flex-direction: column;
            width: 400px;
            padding: 20px;
        }

        @media (max-width: 768px) {
            .title {
                font-size: 40px;
            }

            .nav a {
                font-size: 16px;
            }

            .input-container {
                width: 90%;
            }
        }
                @media (max-width: 480px) {
            .title {
                font-size: 32px;
            }

            .nav a.nav-left {
                margin-right: 0;
                max-width: 100%;
            }

            .nav {
                flex-wrap: wrap;
                justify-content: space-between;
            }

            .nav a {
                font-size: 14px;
                padding: 10px;
            }
        

        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <div class="nav">
        <a class="nav-left" href="">The Career Club</a>
        <a href="internships.html">Internships</a>
        <a href="jobs.html">Jobs</a>
        <a href="employers.html">Employers</a>
        <a href="events.py">Events</a>
        <a href="login3.py">Login</a>
    </div>

    <div class="title">
        Sign Up
    </div>
    <form action="contact1.py" method="POST">
        <div class="input-container">
            <label for="username">Username:</label>
            <input type="text" name="username" required>
            <label for="email">Email:</label>
            <input type="email" name="email" required>
            <label for="password">Password:</label>
            <input type="password" name="password" required>
            <label for="industry">Industry Preferences:</label>
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
            <button class="primary" type="submit">Sign Up</button>
        </div>
    </form>

    <!-- Footer -->
    
        <div class="footer">
        <!-- Additional CSS Files -->
        <link rel="stylesheet" href="assets/css/fontawesome.css">
        <link rel="stylesheet" href="assets/css/templatemo-eduwell-style.css">
        <link rel="stylesheet" href="assets/css/owl.css">
        <link rel="stylesheet" href="assets/css/lightbox.css">
        <section class="contact-us" id="contact-section">
            <div class="col-lg-12">
                <ul class="social-icons">
                    <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                    <li><a href="#"><i class="fa fa-twitter"></i></a></li>
                    <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
                    <li><a href="#"><i class="fa fa-rss"></i></a></li>
                    <li><a href="#"><i class="fa fa-dribbble"></i></a></li>
                </ul>
                
                <h3 align="center"><br>The Career Club</h3>
                <p align="center">The Career Club aims to make the job search process easier and more efficient for both job seekers and employers.</p>      
                <br>
            </div>
        </section>
        </div>
    </div>
</body>
</html>
""")
