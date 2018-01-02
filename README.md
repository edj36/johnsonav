# Johnson Audio Visual Services Website

Website for students and faculty at Cornell's Johnson School of Management to utilize services provided by the Audio-Visual team. 

By Eric Johnson

# Installation

I didn't do any virtualenv for the project to minimize complexity for a new developer on the project. I used anaconda python 3.6 available [here](https://www.anaconda.com/download/).

Once you have anaconda python or whatever python you want (as long as it's version 3+), clone this repo, `cd` into it, and then install the `pip` packages from `requirements.txt` via
```
pip install -r requirements.txt
```

# Deployment

Push to git as usual:
```
git push -u origin master
```

Push to heroku:

First make sure to run 
```
heroku git:remote -a johnsonav
```
and then 
```
git push heroku master
```

# TODO 

- virtualenv for dependency management
- database of events
- module to display events
- module to write to calendar
- module to send email to users 
