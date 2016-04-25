#!/usr/bin/env python

import argparse
from datetime import datetime
import requests
from bs4 import BeautifulSoup

SPAMHAUS_ROOT = "https://www.spamhaus.org/sbl/listings/{0}"


class Listing(object):
    def __init__(self, incident_id, ip_address, domain_name, timestamp, description):
        self.incident_id = incident_id
        self.ip_address = ip_address
        self.domain_name = domain_name
        self.timestamp = datetime.strptime(timestamp, "%d-%b-%Y %H:%M %Z")
        self.description = description

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def __repr__(self):
        return "{incident_id:<12}{ip_address:<22}{domain_name} \t {timestamp}\t {description}".format(**self.__dict__)


def parse_spamhaus(domain):
    uri = SPAMHAUS_ROOT.format(domain)

    request = requests.get(uri)
    soup = BeautifulSoup(request.text, "html.parser")
    listings = []
    for incident in soup.find_all("table", border="0", cellpadding="4", cellspacing="0", width="100%"):
        spans = incident.findAll("span")
        listing = Listing(incident_id=spans[0].b.text,
                          ip_address=spans[1].b.text,
                          domain_name=spans[2].b.text,
                          timestamp=spans[3].text,
                          description=' '.join(s.strip() for s in spans[4].text.splitlines()))
        listings.append(listing)

    for listing in sorted(listings, reverse=True):
        print listing


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse the Spamhaus DB for your domain")
    parser.add_argument("-d", "--domain", help="The domain you want to query")
    args = parser.parse_args()

    if args.domain:
        parse_spamhaus(args.domain)
    else:
        parser.print_help()

