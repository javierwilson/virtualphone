# virtualphone
Manage a Twilio phone.
Read your SMS messages using Django admin interface.

## Requirements
* Django 3. (Tested with Django 3.2.8)
* A Twilio account
* An email address

## Installation
* git clone https://github.com/javierwilson/virtualphone
* cd virtualphone
* mkvirtualenv virtualphone # or whatever you do to keep organize your projects' envs.
* pip install -r requirements.txt

## Configuration
* cp virtualphone/env.sample virtualphone/.env
* vim virtualphone/.env
  * Set the project's Django `SECRET_KEY`
  * Enter you Twilio caller ID as variable `TWILIO_DEFAULT_CALLERID` (optional)
  * Set the email where you want to receive a copy of your messages with `EMAIL_TO`
  * Configure the FROM line of those emails with `EMAIL_FROM`
  * Set DEBUG to true if you are not in production and/or wish to troubleshoot

## Reading your messages
* Keep the project running and set it as Twilio's SMS webhook for your phone number
* Go to http://example.com/admin and browse the model "Message"
