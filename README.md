# spamhaus

A basic parser for Spamhaus listings so you don't need to leave the command line.

*Usage:*
```bash
$ ./spamhaus_parser.py -d spamhaus.org -f tab
SBL2        127.0.0.2/32          spamhaus.org   2016-04-02 18:34:00     Spamhaus Block List (SBL)  test record
SBL9        127.0.0.9/32          spamhaus.org   2016-04-02 17:57:00     Spamhaus DROP (Don't Route Or Peer) and EDROP test record
SBL230      192.203.178.107/32    spamhaus.org   2001-08-01 08:51:00     SBL TEST ADDRESS - sbl.crynwr.com
$ ./spamhaus_parser.py -d spamhaus.org -f json
{
    "description": "Spamhaus Block List (SBL)  test record",
    "domain_name": "spamhaus.org",
    "incident_id": "SBL2",
    "ip_address": "127.0.0.2/32",
    "timestamp": "2016-04-02T18:34:00"
},
{
    "description": "Spamhaus DROP (Don't Route Or Peer) and EDROP test record",
    "domain_name": "spamhaus.org",
    "incident_id": "SBL9",
    "ip_address": "127.0.0.9/32",
    "timestamp": "2016-04-02T17:57:00"
},
{
    "description": "SBL TEST ADDRESS - sbl.crynwr.com",
    "domain_name": "spamhaus.org",
    "incident_id": "SBL230",
    "ip_address": "192.203.178.107/32",
    "timestamp": "2001-08-01T08:51:00"
}
```

### Dependancies

 * [requests][1]
 * [BeautifulSoup4][2]

[1]: http://docs.python-requests.org/en/master/
[2]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
