#!/usr/bin/python3
import cgi

# Get the form data
formval = cgi.FieldStorage()
fname = formval.getvalue("fname")
email = formval.getvalue("email")

# Print the HTML response
print("Content-Type: text/html\n\n")
print()

print("""
    <!DOCTYPE html>

<link rel="stylesheet" href="form.css">
<div class="sidebar">
      <div class="sidebar-1">
        <div class="s1-initial">J</div>
          <a class="s2-link" onclick="w3_close()" class="s1-name" href="inbox.html">Login</a>
        <div class="s1-icon"><i class="fa fa-angle-down"></i></div>
      </div>
      <div class="sidebar-2">
        <div class="s2-item">
          <div class="s2-icon">
            <i class="far fa-star"></i>
          </div>
           <a class="s2-link" href="index.html">Home</a>
          
        </div>
        <div class="s2-item">
          <div class="s2-icon">
            <i class="fas fa-tasks"></i>
          </div>

            <div> <a href="internships.html" class="s2-link">Internships</a></div>
          
        </div>
        <div class="s2-item">
          <div class="s2-icon">
            <i class="fa fa-cog"></i>
          </div>
          
          <a href="jobs.html" class="s2-link">Jobs</a>
          
        </div>
        <div class="s2-item">
          <div class="s2-icon">
            <i class="fas fa-table"></i>
          </div>
            <a href="employers.html" class="s2-link">Employers</a>
        </div>

       <div class="s2-item">
          <div class="s2-icon">
            <i class="fas fa-table"></i>
          </div>
          
              <a href="events.html" class="s2-link">Events</a>
          </div>
        </div>
      </div>
    </div>

</html>
    <html>
    <link rel="stylesheet" href="form.css">
        <body>
        <div class= "main">
            <h1>Thank you for submitting the application</h1>
            <h2>Form Submission Details:</h2>
                <p><b>Thank you </b>%s</p>
                <p><b>For submitting your application to Bank of America<b></p>
                <p><b>We will be in touch with you shortly on the email:</b> %s</p>
        </div>
        </body>
    </html> 
""" % (fname, email) )
