#!/usr/bin/python3
import cgi

print("Content-type: text/html \n\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            grid-template-rows: auto 1fr auto;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0 !important;
        }

        main {
            justify-content: center;
            align-items: center;
            padding-top: 100px;
        }

        .flex-container {
          display: flex;
          align-items: center;
          justify-content: center;
          background-color: #f0f0f0 !important;
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
            font-weight: normal;
            font-size: 14px;
            color: black;
            font-family: "Segoe UI", Frutiger, "Frutiger Linotype", "Dejavu Sans", "Helvetica Neue", Arial, sans-serif;
        }

        input {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            font-size: 18px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .container {
            max-width: 600px;
        }

        button {
            background-color: #04AA6D !important;
            color: white;
            padding: 14px 20px;
            border: none;
            border-radius: none;
            margin: 8px 0;
            border: none;
            cursor: pointer;
            width: 100%;
        }

        button:hover {
            opacity: 0.8;
        }

        .cancelbtn, .signupbtn {
            width: 49%;
            padding: 10px 18px;
            background-color: #04AA6D;
        }

        .cancelbtn {
            float: right;
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
            width: 100%;
        }

        @media (max-width: 768px) {
        .container {
            max-width: 100%;
            padding: 0 20px;
        }

        .nav a {
            font-size: 16px;
            padding: 10px 12px;
        }

        .nav a.nav-left {
            font-size: 24px;
        }

        .cancelbtn, .signupbtn {
            width: 100%;
        }
    }

    
    @media (max-height: 600px) and (aspect-ratio: 3/4) {
        .title {
            font-size: 40px;
            margin-bottom: 10px;
        }

        input {
            font-size: 16px;
        }

        button {
            padding: 8px 12px;
            font-size: 16px;
        }

        .nav a {
            font-size: 14px;
            padding: 8px 10px;
        }

        .nav a.nav-left {
            font-size: 20px;
        }
    }

    @media (max-height: 600px) {
    main {
        padding-top: 50px;
    }

    .title {
        font-size: 40px;
        margin-bottom: 10px;
    }
}

    /* Social icons hover */
    .social-icons a {
        display: inline-block;
        position: relative;
        border-radius: 50%;
        transition: background-color 0.3s;
    }

    .social-icons a:hover {
        background-color: rgba(0, 0, 0, 0.1);
    }

    .social-icons i {
        display: block;
        padding: 10px;
    }
}
    </style>
</head>
<body>
    <main>
        <!-- Navigation -->
        <div class="nav">
            <a class="nav-left" href="grpprj.py">The Career Club</a>
            <a href="internhsips.html">Internships</a>
            <a href="jobs.html">Jobs</a>
            <a href="employers.html">Employers</a>
            <a href="events.py">Events</a>
            <a href="login3.py">Login</a>
        </div>

        <div class="flex-container">
        <div class="container">
            <div class="title">
                Login
            </div>
            <form action="login1.py" method="post">
                <div class="input-container">
                    <label for="email">Email:</label>
                    <input type="email" placeholder="Enter Username" name="email" required>
                </div>
                <div class="input-container">
                    <label for="psw">Password:</label>
                    <input type="password" placeholder="Enter Password" name="password" required>
                </div>

                <button class="button" type="submit">Login</button>
            </form>
            <div>
                <button type="button" onclick="window.location.href='signup1.py'" class="signupbtn">Sign Up</button>
                <button type="button" onclick="window.location.href='grprg.py'" class="cancelbtn">Cancel</button>
            </div>
            <button type="button" onclick="window.location.href='fgt.html'" class="button">Forgot Password</button>
        </div>
        </div>

<!-- Footer -->
        <!-- Additional CSS Files -->

        <div class="flex-container">
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
</body>
</html>
""")
