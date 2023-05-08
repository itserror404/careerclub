#!/usr/bin/python3
import cgi

def store(line):
    # Open a file to append
    filer = open("data.txt", "a")

    # Write to file
    filer.write(line)

    filer.close()
print("Content-type: text/html \n\n")

form_data = cgi.FieldStorage()

# Store form data in a file
with open("contact_form_data.txt", "a") as f:
    for key in form_data.keys():
        f.write(key + ": " + form_data[key].value + "\n")
    f.write("\n")
    store("\n")
print("""<!DOCTYPE html>
<!DOCTYPE html>
<html>
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
        <a href="inbox.html" class="active">Login</a>
      </div>
    </div>
  </body>
</html>
""")

name_data = form_data.getvalue("name", "")
email_data = form_data.getvalue("email", "")
message_data = form_data.getvalue("message", "")

print("""<!DOCTYPE html>
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Additional CSS Files -->
    <link rel="stylesheet" href="assets/css/fontawesome.css">
    <link rel="stylesheet" href="assets/css/templatemo-eduwell-style.css">
    <link rel="stylesheet" href="assets/css/owl.css">
    <link rel="stylesheet" href="assets/css/lightbox.css">
  <section class="contact-us" id="contact-section">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div id="map">
            <!-- You just need to go to Google Maps for your own map point, and copy the embed code from Share -> Embed a map section -->
            <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d14519.559259858976!2d54.4345558!3d24.5238948!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5e5d876232c3eb%3A0x14e8727ec5ee2be1!2sNew%20York%20University%20Abu%20Dhabi!5e0!3m2!1sen!2s!4v1682098710764!5m2!1sen!2s" width="100%" height="420px" frameborder="0" style="border:0; border-radius: 15px; position: relative; z-index: 2;" allowfullscreen=""></iframe>
            <div class="row">
              <div class="col-lg-4 offset-lg-1">
                <div class="contact-info">
                  <div class="icon">
                    <i class="fa fa-phone"></i>
                  </div>
                  <h4>Phone</h4>
                  <span>010-020-0340</span>
                </div>
              </div>
                <div class="col-lg-4">
                  <div class= "contact-info">
                    <div class="icon"><i class="fa fa-phone"></i>
                    </div>
                      <h4>Mobile</h4>
                      <span>090-080-0760</span>
                  </div>
                </div>
              </div>
             </div>
             </div>
              <div class="col-lg-4">
                <div>
                  <div class="row">
                    <div class="col-lg-12">
                      <div class="section-heading">
                        <h6>Contact us</h6>
                        <h4>Say Hello</h4>
                        <p>IF you need a working contact form by PHP script, please visit TemplateMo's contact page for more info.</p>
                      </div>
                    </div>
                    """ + (name_data and "<div class='col-lg-12'><p>Full Name: " + name_data + "</p></div>") + """
                    """ + (email_data and "<div class='col-lg-12'><p>Email: " + email_data + "</p></div>") + """
                    """ + (message_data and "<div class='col-lg-12'><p>Message: " + message_data + "</p></div>") + """
                </div>
              </div>
            </div>
           <div class="col-lg-12">
             <ul class="social-icons">
              <li><a href="#"><i class="fa fa-facebook"></i></a></li>
              <li><a href="#"><i class="fa fa-twitter"></i></a></li>
              <li><a href="#"><i class="fa fa-linkedin"></i></a></li>
              <li><a href="#"><i class="fa fa-rss"></i></a></li>
              <li><a href="#"><i class="fa fa-dribbble"></i></a></li>
             </ul>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
<!-- About End -->
<div class="footer-content">
  <h3>The Career Club</h3>
    <p>The Career Club aims to make the job search process easier and more efficient for both job seekers and employers.</p>
  </div>
</html>
""")

def store(line):
    # Open a file to append
    filer = open("database10.txt", "a")

    # Write to file
    filer.write(line)

    filer.close()

