#!/usr/bin/python3
print("Content-Type: text/html\n\n")
print()

print("""
<!DOCTYPE html>
<html>



<!-- nav bar and logo-->
  <head>
    <link rel="stylesheet" href="nav.css">
  </head>
  <body>
    <div class="nav">
      <a class="nav-left" href="grpprj.py">The Career Club</a>
      <div class="navr">
        <a href="internships.html">Internships</a>
        <a href="jobs.html">Jobs</a>
        <a href="employers.html">Employers</a>
        <a href="events.py">Events</a>
        <a href="login3.py" class="active">Login</a>
      </div>
    </div>
  </body>
  </html>
 
 <!DOCTYPE html>
<html lang="en">

<head>
    <style>
                body {
            margin: 0;
            padding: 0;
            margin-top: 0;
        }
        
        /* Styling section, giving background
            image and dimensions */
        section {
            width: 100%;
            margin-top: -50;
            margin-bottom: 100px;
            background-size: cover; }



        .footer {
            margin-top: 1040px;
            padding: 50px;
    bottom: 0;
    left: 0;
    right: 0;
    background: #111;
    height: 300px;
    width: 100vw;
    padding-top: 40px;
    color: #000000;
        }
        
        /* Styling the left floating section */
        section .leftBox {
            width: 50%;
            height: 1000px;
            float: left;
            padding: 50px;
            position: relative;
            box-sizing: border-box;
            margin-top: -100px;
            align-items: center;

        }
        
        /* Styling the background of
            left floating section */
        section .leftBox .content {
            color: #fff;
            background: rgba(0, 0, 0, 0.5);
            padding: 40px;
            transition: .5s;
        }
        
        /* Styling the hover effect
            of left floating section */
        section .leftBox .content:hover {background: #e91e63;
            
        }
        
        /* Styling the header of left
            floating section */
        section .leftBox .content h1 {
            margin: 0;
            padding: 0;
            font-size: 50px;
            text-transform: uppercase;
        }
        
        /* Styling the paragraph of
            left floating section */
        section .leftBox .content p {
            margin: 10px 0 0;
            padding: 0;
        }
        
        /* Styling the three events section */
        section .events {
            position: relative;
            width: 50%;
            height: 1000px;
            background: rgba(0, 0, 0, 0.5);
            float: right;
            padding: 0 ;
            align-items: center;
            margin-top: -100px;

            
        }
        
        /* Styling the links of
        the events section */
        section .events ul {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            padding: 30px;
            box-sizing: border-box;
            margin-top: 15px;
        }
        
        /* Styling the lists of the event section */
        section .events ul li {
            list-style: none;
            background: #fff;
            box-sizing: border-box;
            height: 270px;
            margin-top: 15px;
        }
        
        /* Styling the time class of events section */
        section .events ul li .time {
            position: relative;
            padding: 20px;
            background: #262626;
            box-sizing: border-box;
            width: 30%;
            height: 100%;
            float: left;
            text-align: center;
            transition: .5s;
        }
        
        /* Styling the hover effect
            of events section */
        section .events ul li:hover .time {
            background: #e91e63;
        }
        
        /* Styling the header of time
            class of events section */
        section .events ul li .time h2 {
            position: absolute;
            margin: 0;
            padding: 0;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #fff;
            font-size: 60px;
            line-height: 30px;
        }
        
        /* Styling the texts of time
        class of events section */
        section .events ul li .time h2 span {
            font-size: 30px;
        }
        
        /* Styling the details
        class of events section */
        section .events ul li .details {
            padding: 20px;
            background: #fff;
            box-sizing: border-box;
            width: 70%;
            height: 100%;
            float: left;
        }
        
        /* Styling the header of the
        details class of events section */
        section .events ul li .details h3 {
            position: relative;
            margin: 0;
            padding: 0;
            font-size: 22px;
        }
        
        /* Styling the lists of details
        class of events section */
        section .events ul li .details p {
            position: relative;
            margin: 10px 0 0;
            padding: 0;
            font-size: 16px;
        }
        
        /* Styling the links of details
        class of events section */
        section .events ul li .details a {
            display: inline-block;
            text-decoration: none;
            padding: 10px 15px;
            border: 1.5px solid #262626;
            margin-top: 8px;
            font-size: 18px;
            transition: .5s;
        }
        
        /* Styling the details class's hover effect */
        section .events ul li .details a:hover {
            background: #e91e63;
            color: #fff;
            border-color: #e91e63;
        }
    </style>
</head>


    <section>
        <div class="leftBox">
            <div class="content">
                <h1>
                    Events and Shows
                </h1>
                <img class="imageabout" src="img/about-3.jpg" width="500" height="250">
            </div>
        </div>

        <div class="events">
            <ul>
                <li>
                    <div class="time">
                        <h2>
                            15 <br><span>March</span>
                        </h2>
                    </div>
                    <div class="details">
                        <h3>
                            Barclays Info and Networking Session
                        </h3>
                        
<p>
                            Barclays would like to meet with sophomores to discuss 2024 summer internship opportunities in Sales & Trading and Research Internships for 2024.

                            
                        </p>


                        <a href="#">View Details</a>
                    </div>
                    <div style="clear: both;"></div>
                </li>

                <li>
                    <div class="time">
                        <h2>
                            27 <br><span>May</span>
                        </h2>
                    </div>
                    <div class="details">
                        <h3>
                            BoFA Wealth Management - Virtual
                        </h3>
                        
<p>
                            Join Bank of America representatives on Wednesday, April 12th for an inside the industry look at our Private Bank - Legacy US Trust. Bank of America is the largest provider of personal trust services in the country. 
                        </p>

                        <a href="bofadetail.html">View Details</a>
                    </div>
                    <div style="clear:both;"></div>
                </li>

                <li>
                    <div class="time">
                        <h2>
                            12 <br><span>August</span>
                        </h2>
                    </div>
                    <div class="details">
                        <h3>
                            Girls Who Invest Information Session
                        </h3>
                        
<p>
                            Please join us for an information session covering Girls Who Invest programs and our application process. Come with your questions - we're happy to answer them!
                            
                        </p>


                        <a href="#">View Details</a>
                    </div>
                    <div style="clear:both;"></div>
                </li>
            </ul>
        </div>
    </section>
</body>

</html>
 
<!-- Footer -->
    <!-- Additional CSS Files -->
    <link rel="stylesheet" href="nav.css">
    <div class ="footer">
    <link rel="stylesheet" href="assets/css/fontawesome.css">
    <link rel="stylesheet" href="assets/css/templatemo-eduwell-style.css">
    <link rel="stylesheet" href="assets/css/owl.css">
    <link rel="stylesheet" href="assets/css/lightbox.css">
    <section class="contact-us" id="contact-section">
          <div class="col-lg-12">
             <ul class="social-icons" position= 'fixed'>
             <br>
              <li><a href="#"><i class="fa fa-facebook"></i></a></li>
              <li><a href="#"><i class="fa fa-twitter"></i></a></li>
              <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
              <li><a href="#"><i class="fa fa-rss"></i></a></li>
              <li><a href="#"><i class="fa fa-dribbble"></i></a></li>
             </ul>
            </form>  
            <link rel="stylesheet" href="nav.css">
    <h3 align= "center" > <br>The Career Club</h3>
    <p align= "center" >The Career Club aims to make the job search process easier and more efficient for both job seekers and employers.</p>      
    <br></div>
</section>
</section>
</html>
""")

