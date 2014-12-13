Homemade Dynamic DNS
===============

This is a simple python script that implements a dynamic dns solution using Amazon's Route 53. This is useful if you have dynamic ip in your home/office but you still want to access to a server in it remotely.

You will only need to buy a domain, and sign up on AWS (amazon web services) for Route's 53 service.

Once you deploy your script on your server, you need to set up a cron for it to run every minute or every 3 mins. The script will detect when your ip changes and it will update the ip associated to that domain. So the domain is always pointing to your home/office ip, no matter if it changes.



