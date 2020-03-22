import ovh

def load_dns_entries(zone, subdomain):
    client = ovh.Client()

    dns_entries = client.get('/domain/zone/{}/record'.format(zone),
                         subDomain=subdomain)

    return dns_entries
