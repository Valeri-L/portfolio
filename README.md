# Legacy Portfolio — Vue.js + Django

This repository contains my previous portfolio website, built before my current Next.js portfolio.

The project was developed as a full-stack web application using **Vue.js**, **Django**, **Redis**, and **Docker**, and was previously hosted on AWS under:

```txt
https://portfolio.valerilevinson.com
```

This project is now considered a **legacy / archived portfolio**, but it still represents an important stage in my development journey. It includes frontend UI work, backend API development, caching, Docker-based deployment, contact form handling, and third-party API integration.

---

## Project Overview

The portfolio was created to showcase my development skills, personal projects, achievements, technical background, and contact options.

Unlike a simple static portfolio, this project included a backend service built with Django. The backend was mainly responsible for handling contact form submissions and sending the submitted details directly to my email.

The project also included dynamic sections such as LeetCode statistics, GitHub activity summaries, projects, skills, and a contact form.

---

## Tech Stack

### Frontend

* Vue.js
* Vue Composition API
* Tailwind CSS
* Custom animated UI components
* Responsive layout
* Multilingual support: English / Hebrew

### Backend

* Django
* Django REST Framework
* Redis caching
* Email sending service
* Google reCAPTCHA integration
* CORS configuration

### Infrastructure

* Docker
* Docker Compose
* AWS hosting
* Linux server environment

---

## Main Features

### Portfolio Sections

The frontend included several main sections:

* About Me
* What I Do
* Projects
* Skills
* Achievements
* Contact Me

Each section was built as a separate Vue component to keep the project structured and reusable.

---

## About Me Section

The About Me section included:

* Animated typing effect
* English / Hebrew language support
* Highlighted text segments
* Custom visual effects
* Tilted card animation
* Shiny text animation

This section was designed to make the portfolio feel more interactive and personal.

---

## Achievements Section

The achievements section included:

* LeetCode completed questions
* Difficulty totals: Easy, Medium, Hard
* Total solved questions
* GitHub yearly activity summary
* Animated counters using `countup.js`

LeetCode data was fetched from the backend and cached to reduce unnecessary API calls.

Caching was handled using browser local storage with expiration logic, and Redis was also used on the backend side.

---

## Projects Section

The projects section showcased personal and technical projects, including private and public projects.

The goal of this section was to document not only what I built, but also why I built it and what problem each project solved.

---

## Skills Section

The skills section displayed my technical stack and development knowledge, including frontend, backend, infrastructure, and networking-related skills.

---

## Contact Section

The contact section included:

* Contact form
* Name field
* Email field
* Phone field
* Message field
* Google reCAPTCHA validation
* Backend API call to Django
* Email sending to myself
* Alert messages for success or error states

The backend endpoint received the form data and sent it to my email, making the contact form functional instead of only visual.

---

## Backend Functionality

The Django backend was mainly responsible for:

* Handling contact form submissions
* Sending emails
* Integrating reCAPTCHA validation
* Serving API endpoints
* Managing CORS
* Supporting LeetCode-related API functionality
* Redis-based caching

The most important backend feature was the contact form flow:

```txt
User fills contact form
        ↓
Vue frontend sends request to Django API
        ↓
Django validates the request
        ↓
reCAPTCHA is checked
        ↓
Django sends the message details to my email
```

---

## Docker Setup

The project was designed to run with Docker Compose.

### docker-compose.yml

```yaml
version: "3.9"

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    image: levinsonvaleri/portfolio_frontend:latest
    platform: "linux/amd64"
    ports:
      - "3000:3000"
    depends_on:
      - backend

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    image: levinsonvaleri/portfolio_backend:latest
    platform: "linux/amd64"
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
```

---

## Environment Variables

Create a `.env` file inside the `backend/` directory.

Example:

```env
SECRET_KEY="your django secret key"
DEBUG="False"
LEETCODE_API_URL="https://leetcode.com/graphql"
REDIS_LOCATION="your redis url"
REDIS_PASSWORD="your redis password"
CORS_ALLOWED_ORIGINS="your domain / localhost"
EMAIL_HOST_USER="email that sends contact messages"
EMAIL_HOST_PASSWORD="email password"
ALLOWED_HOSTS="localhost"
ALLOWED_HOSTS_99="additional host if needed"
RECAPTCHA_SECRET_KEY="your recaptcha secret key"
```

Do not commit real secrets, passwords, email credentials, or API keys to GitHub.

---

## Running the Project

Clone the repository:

```bash
git clone <repository-url>
```

Create the backend `.env` file:

```bash
cd backend
touch .env
```

Add the required environment variables.

Then run the project with Docker Compose:

```bash
docker-compose up --build
```

To run it in detached mode:

```bash
docker-compose up --build -d
```

To stop the containers:

```bash
docker-compose down
```

---

## Project Status

This is my old portfolio project built with Vue.js and Django.

It is no longer my main portfolio, but it is still a valuable project because it demonstrates:

* Full-stack development
* Vue.js frontend architecture
* Django backend API development
* Contact form backend logic
* Email sending functionality
* Docker-based deployment
* Redis caching
* reCAPTCHA integration
* AWS deployment experience
* Multilingual portfolio structure

My newer portfolio is built with Next.js, but this project shows an earlier stage of my development path and the progress I made while learning and building real applications.

---

## Notes

This repository can be used as a reference for building a full-stack portfolio with Vue.js and Django.

It is not just a static portfolio. It includes real backend functionality, API communication, caching logic, and a working contact form flow.
