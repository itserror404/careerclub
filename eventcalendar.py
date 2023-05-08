#!/usr/bin/python3
print("Content-Type: text/html\n\n")
print()

print("""<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
  <style>
    ::selection {
      background-color: rgba(46, 204, 113, 1);
      color: white;
    }
  </style>
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
        <a href="events.html">Events</a>
        <a href="login3.py" class="active">Login</a>
      </div>
    </div>
  </body>
</html>
""")

print("""<!DOCTYPE html>
  <head>
  <link rel="stylesheet" href="calendar.css">
   <div class="route" id="index"></div>
<div class="route" id="oct-week-3"></div>
<div class="route" id="oct-week-4"></div>
<div class="route" id="nov-week-1"></div>
<div class="route" id="schedule"></div>
<main class="cal-device">
  <header class="cal-header">
    <div class="cal-subheader"></div>
    <div class="cal-bar">
      <div class="cal-button -left">
        <i class="fa fa-bars -calendar"></i>
        <a href="#index" class="fa fa-chevron-left -schedule"></a>
      </div>
      <div class="cal-title">
        <div class="cal-heading -calendar">Calendar</div>
        <div class="cal-heading -schedule">Wednesday, November 10</div>
      </div>
      <div class="cal-button -right">
        <i class="fa fa-search"></i>
      </div>
    </div>
  </header>
  <section class="cal-app">
    <header class="cal-week">
      <div class="cal-weekday">SUN</div>
      <div class="cal-weekday">MON</div>
      <div class="cal-weekday">TUE</div>
      <div class="cal-weekday">WED</div>
      <div class="cal-weekday">THU</div>
      <div class="cal-weekday">FRI</div>
      <div class="cal-weekday">SAT</div>
    </header>
    <div class="cal-scene -calendar">
      <div class="cal-month -october">
        <header class="cal-header">
          <a class="cal-link" href="#oct-week-1"><span>October</span></a>
          <a class="cal-arrow" href="#nov-week-1"><i class="fa fa-chevron-up"></i></a>
          <a class="cal-arrow" href="#oct-week-4"><i class="fa fa-chevron-up"></i></a>
        </header>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a href="#schedule"  class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
      </div>
      <div class="cal-month -november">
        <header class="cal-header">
          <a class="cal-link" href="#nov-week-1"><span>November</span></a>
          <a class="cal-arrow"><i class="fa fa-chevron-up"></i></a>
        </header>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a href="#schedule" class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a href="#schedule" class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a href="#schedule" class="cal-day"></a>
        <a href="#schedule" class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
      </div>
      <div class="cal-month -december">
        <header class="cal-header">
          <a class="cal-link"><span>December</span></a>
          <a class="cal-arrow" href="#nov-week-1"><i class="fa fa-chevron-down"></i></a>
          <a class="cal-arrow" href="#oct-week-3"><i class="fa fa-chevron-down"></i></a>
        </header>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a href="#schedule" class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a href="#schedule" class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
      </div>
      <div class="cal-month -january">
        <header class="cal-header">
          <div class="cal-link"><span>January</span></div>
          <a class="cal-arrow" href="#oct-week-4"><i class="fa fa-chevron-down"></i></a>
        </header>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
        <a class="cal-day"></a>
      </div>
    </div>
    <div class="cal-scene -schedule">
      <div class="cal-item">
        <div class="cal-time"><span>08:00</span></div>
        <div class="cal-task">
          <p>wake up</p>
        </div>
      </div>
      <div class="cal-item -long">
        <div class="cal-time"><span>12:15</span></div>
        <div class="cal-task">
          <p>meeting with the team, discussing the project requirements</p>
        </div>
      </div>
      <div class="cal-item">
        <div class="cal-time"><span>13:00</span></div>
        <div class="cal-task">
          <p>lunch with Peter</p>
          <a><i class="fa fa-map-marker"></i>cafe <q>Petit brasserie</q></a>
        </div>
      </div>
      <div class="cal-item">
        <div class="cal-time"><span>14:30</span></div>
        <div class="cal-task">
          <p>call with Johnathan and Stevie</p>
        </div>
      </div>
      <div class="cal-item -long">
        <div class="cal-time"><span>16:45</span></div>
        <div class="cal-task">
          <p>project presentation</p>
          <a><i class="fa fa-map-marker"></i>Head Office</a>
        </div>
      </div>
      <div class="cal-item">
        <div class="cal-time"><span>18:00</span></div>
        <div class="cal-task">
          <p>call with Johnathan and Stevie</p>
        </div>
      </div>
      <div class="cal-item -long">
        <div class="cal-time"><span>19:00</span></div>
        <div class="cal-task">
          <p>David's birthday party</p>
          <a><i class="fa fa-map-marker"></i>bar <q>Tailor's John</q></a>
        </div>
      </div>
      <div class="cal-item">
        <div class="cal-time"></div>
        <div class="cal-task"></div>
      </div>
    </div>
  </section>

</div>

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
            </form>  
            <link rel="stylesheet" href="nav.css">
    <h3 align= "center" > <br>The Career Club</h3>
    <p align= "center" >The Career Club aims to make the job search process easier and more efficient for both job seekers and employers.</p>      
    <br></div> """)

