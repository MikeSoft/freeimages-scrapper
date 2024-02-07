## Questions:

**How can we automate the login of the page?**  
Using the requests library and sessions to store the cookies and the csrf token, we can automate the login of the page.

**How can we scale the extractor to get thousands of pages per hour?**  
We can use a distributed system to scrape the images, using a queue system like celery, and a distributed system like
kubernetes to scale the system.

## Tech Stack

```
Python 3.8.5  (https://www.python.org/)
Django 4.2.7 (https://www.djangoproject.com/)
Docker 20.10.8 (https://www.docker.com/)
Docker-compose 1.29.2 (https://docs.docker.com/compose/)
Mysql 8.0.26 (https://www.mysql.com/)
```

## How to run the project

- Deploy with Docker

I've created a make file to manage the differents aspects of the application, with only one command, you can create the
virtual environment, install the dependencies, run the migrations, run the server in docker.
With only one comand you can run the project

```shell
make buildandrun
```

### Create user for admin dashboard

```shell
make createadmin
```

the console will ask you a password
with the password you can go to the admin dashboard with [this link](http://localhost/admin)

user=```admin```  
password=```the password that you set in the console```

# How to Scrape the images

go to http://localhost/admin/images/search/  
![screenshot](./documentation/images/admin_search.png)
and click on "Add search" button, and fill the form with the search that you want to scrape.   
The system automatically will scrape the images and save it in the database.  
It uses a celery task to scrape the images.
now go to http://localhost/admin/images/image/ to see the images that you have scraped.
![screenshot](./documentation/images/admin_images.png)  
if you click on the image title, you can see the image detail. i also added the tags that the image has.

```bash


---
# How registered a user:

when i was going to test how to log in a user, i found that the login form is not working, so i decided to create a user
debbuging the form and the request that the form is sending to the server.

```bash
user=donaldtrump123
pass=sejawat716
```

![screenshot](./documentation/images/free_images_login_fail.png)  
![screenshot](./documentation/images/free_images_login_fail_message.png)
**i used postman to solved it**
![screenshot](./documentation/images/fix_errr_request.png)

```bash
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2OTkzNjU5LCJpYXQiOjE3MDY5MDcyNTksImp0aSI6IjdkMTkzMDIyZjVmMzRjZTdhMzM5YzY2ZGZjMmJjMjU4IiwidXNlcl9pZCI6MTEwOTM3NTl9.oS51s0CuoQo1IHU9iXC0aQgchFbDf8Q6euHjqZM3mNU",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNzUxMjA1OSwiaWF0IjoxNzA2OTA3MjU5LCJqdGkiOiJkYTRmNTRkNGFhMzg0YmY0YWIzNTQ3MTNkMGI1Zjg1ZSIsInVzZXJfaWQiOjExMDkzNzU5fQ.NXBZr-80G31b_yGv0OKAO_l4pEyqP4xXQ_YAq8ldhk4"
}
```

![screenshot](./documentation/images/loggued.png)

```bash
curl --location 'https://www.freeimages.com/ajax/user/signup' \
--header 'authority: www.freeimages.com' \
--header 'accept: */*' \
--header 'accept-language: en-US,en;q=0.9,es-CO;q=0.8,es;q=0.7' \
--header 'cookie: country=CO; _gid=GA1.2.935622841.1706904265; _hjSessionUser_2757305=eyJpZCI6IjYwNzBkMzVhLTI1NGEtNWI4ZC1hYjBlLWFmZWY4MDNkMmQ4YiIsImNyZWF0ZWQiOjE3MDY5MDQyNjU0OTEsImV4aXN0aW5nIjp0cnVlfQ==; csrftoken=sosFUZFvMSK1wZ2DoXJg4F34sk8KtGAD1PDkKZ4vknrRya1ysQCvCGauuFJKzUJB; OptanonAlertBoxClosed=2024-02-02T20:04:36.181Z; pig=true; _gat_UA-231639-4=1; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+02+2024+15%3A52%3A53+GMT-0500+(Colombia+Standard+Time)&version=6.34.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=CO%3BMET; _ga=GA1.1.64882344.1706904265; _hjSession_2757305=eyJpZCI6IjM3MTIxN2Q2LWE1NjQtNDY5Yy1hZGY1LWE1NzJhM2E1NDkyZiIsImMiOjE3MDY5MDcxNzMzODgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowfQ==; _ga_QLP2HMBP1Y=GS1.1.1706907115.2.1.1706907199.40.0.0' \
--header 'dnt: 1' \
--header 'origin: https://www.freeimages.com' \
--header 'referer: https://www.freeimages.com/signup' \
--header 'sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "macOS"' \
--header 'sec-fetch-dest: empty' \
--header 'sec-fetch-mode: cors' \
--header 'sec-fetch-site: same-origin' \
--header 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36' \
--form 'csrfmiddlewaretoken="ro61EjYorF0tIFRB5enfPdZwupwYYeGO0PhGujnoZaHjKQQw97gune6WwK7Y4sPM"' \
--form 'first_name="donald"' \
--form 'last_name="trump"' \
--form 'username="donaldtrump123"' \
--form 'email="sejawat716@bitofee.com"' \
--form 'password="sejawat716"' \
--form 'password_confirmation="sejawat716"'
```

## Future Improvements

- Create and setting file for each environment ( unique configuration )
- Add a logger
- Add a cache layer
- Authentication and Authorization layer
- AWS deployment
- Add a CI/CD pipeline
- Add a monitoring tool
- Add a metrics tool
- Add a security tool
- Add a code quality tool
- Add a code coverage tool
-