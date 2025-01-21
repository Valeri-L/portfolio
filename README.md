#Portfolio
This is an open-source web application developed using Vue.js, Django, and Redis, hosted on AWS at portfolio.valerilevinson.com.

#Features
Achievements Section: Showcases GitHub-leetcode questions, with updates on each request, caching results for 25 minutes.
Git Commits Summary: Displays a yearly summary of my Git commits.
Projects Section: Provides documentation and blog posts for both private and public projects I’ve built.

#Template Instructions
To use this project as a template for your own, I recommend setting it up with Docker for easier configuration. Follow these steps:

1.Clone the repository.
2.Create a .env file inside the backend/ directory and add the following configuration:
----------code window
makefile
Copy
Edit
SECRET_KEY="your django secret key"
DEBUG="False"
LEETCODE_API_URL="https://leetcode.com/graphql"
REDIS_LOCATION="redis url"
REDIS_PASSWORD="redis password"
CORS_ALLOWED_ORIGINS="your domain / localhost (for development)"
EMAIL_HOST_USER="email that will send the contact me message"
EMAIL_HOST_PASSWORD="email password"
ALLOWED_HOSTS="localhost"
ALLOWED_HOSTS_99="additional host if needed"
RECAPTCHA_SECRET_KEY="integrated recaptcha key"
------------code window

3.Run the following Docker command:
css
Copy
Edit
docker-compose up --build -d
(Remove -d if you want to see the logs of the images.)
Later, I'll add a more detailed tutorial for setting everything up.


managers:
pip=24.2
npm=9.2.0


languages:
python=3.11


node=v18.19.1

frameworks :
Vue js
django-framework

