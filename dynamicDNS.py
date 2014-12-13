from boto.route53.connection import Route53Connection
import urllib2
import json

content = urllib2.urlopen("http://ifconfig.me/all/json").read()
decoded = json.loads(content)
external_ip = decoded['ip_addr']


# your amazon keys
key = "XXXXXXXXXXXXXXX"
access = "XXXXXXXXXXXXXX"

route53 = Route53Connection(key, access)

zone = route53.get_zone("your-domain.com")

current_dns_ip = zone.get_a("sub-domain.your-domain.com.").resource_records[0]

if current_dns_ip != external_ip:
        zone.update_a("sub-domain.your-domain.com.", external_ip)