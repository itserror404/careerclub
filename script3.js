const form = document.getElementById('job-search-form');
const result = document.getElementById('job-search-results');

async function displayJobs() {
  const read = await fetch('jobs3.csv');
  const data = await read.text();
  const joblist = readfile(data);
  
  const filtered = joblist.filter(job => {
    return true; // no search term applied
  });

  result.innerHTML = '';

  if (filtered.length === 0) {
    result.innerHTML = '<p>No jobs found.</p>';
    return;
  }

  filtered.forEach(job => {
    const jobelement = document.createElement('div');
    jobelement.classList.add('job');
    jobelement.innerHTML = `
      <div class="job-box">
        <div class="job-title"><a href="${job.detailURL}">${job.title}</a></div>
        <div class="job-details">
          <div class="job-company">${job.company}</div>
          <div class="job-location">${job.mode} ∙ ${job.location}</div>
        </div>
        <div class="job-apply">
          <a class="btn btn-danger" href="${job.applyURL}" role="button">Apply</a>
        </div>
      </div>
    `;
    result.appendChild(jobelement);
  });
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const search = document.getElementById('search-field').value;
  const location = document.getElementById('location').value;
  const jobfield = document.getElementById('job-field').value;


  const filtered = jobList.filter(job => {
    const matchsearch = job.title.toLowerCase().includes(search.toLowerCase());
    const matchlocation = location === '' || job.location === location;
    const matchjob = jobfield === '' || job.jobfield === jobfield;
    return matchsearch && matchlocation && matchjob;
  });

  result.innerHTML = '';

  if (filtered.length === 0) {
    result.innerHTML = '<p>No jobs found.</p>';
    return;
  }

  filtered.forEach(job => {
    const jobelement = document.createElement('div');
    jobelement.classList.add('job');
    jobelement.innerHTML = `
      <div class="job-box">
        <div class="job-title"><a href="${job.detailURl}">${job.title}</a></div>
        <div class="job-details">
          <div class="job-company">${job.company}</div>
          <div class="job-location">${job.mode} ∙ ${job.location}</div>
        </div>
        <div class="job-apply">
          <a class="btn btn-danger" href="${job.applyURl}" role="button">Apply</a>
        </div>
      </div>
    `;
    result.appendChild(jobelement);
  });
});

function readfile(csvString) {
  const line = csvString.trim().split('\n');
  const header = line.shift().split(',');
  return line.map((line) => {
    const values = line.split(',');
    const job = {};
    header.forEach((i, j) => {
      if (i === "description") {
        job[i] = `"${values[j]}"`;
      } else {
        job[i] = values[j];
      }
    });
    return job;
  });
}

displayJobs();
