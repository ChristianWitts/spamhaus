# spamhaus

A basic parser for Spamhaus listings so you don't need to leave the command line.

*Usage:*
```bash
$ ./spamhause_parser.py -d mywebsite.com
SBL000001   0.0.0.0/32            mywebsite.com     2016-04-25 06:22:00      Malware distribution @0.0.0.0
```

### Dependancies

 * [requests][1]
 * [BeautifulSoup4][2]

[1]: http://docs.python-requests.org/en/master/
[2]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
