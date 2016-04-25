# spamhaus

A basic parser for Spamhaus listings so you don't need to leave the command line.

*Usage:*
```bash
$ ./spamhaus_parser.py -d spamhaus.org
SBL2        127.0.0.2/32          spamhaus.org   2016-04-02 18:34:00      Spamhaus Block List (SBL)  test record
SBL9        127.0.0.9/32          spamhaus.org   2016-04-02 17:57:00      Spamhaus DROP (Don't Route Or Peer) and EDROP test record
SBL230      192.203.178.107/32    spamhaus.org   2001-08-01 08:51:00      SBL TEST ADDRESS - sbl.crynwr.com
```

### Dependancies

 * [requests][1]
 * [BeautifulSoup4][2]

[1]: http://docs.python-requests.org/en/master/
[2]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
