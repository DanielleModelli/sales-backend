# teste-backend-amicci

Django rest API for Briefings.

## Overview

The django API and the postgres database are inside a docker compose, which contains one dockerfile that builds django project, and, psql container that is given by postgres already.

## Features

- CRUD operations for Vendor, Category, Retailer and Briefings.

## Requirements

All the required dependencies are listed inside requirements.txt and docker will install all when creating the container, so there is no need to install de dependecies on your machine.

Need to create an .env file with your database and secret configuration. Docker will use this file to create the container and to connect to the database.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DanielleModelli/teste-backend-amicci.git
   cd your-repository
   docker-compose up --build

2. Install Docker if not already installed on your system.

3. Pull the Docker container image using the following command:

   ```bash
   docker pull ghcr.io/username/repository/image:tag

4. For running the container run
    ``` bash
    docker-compose up

5. The migration will run when you build the container, but if you need to run again, you can run
    ``` bash
    docker-compose run app python manage.py makemigrations
    docker-compose run app python manage.py migrate

