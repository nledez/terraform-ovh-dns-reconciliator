import ovh

def load_dns_entries(zone, subdomain):
    client = ovh.Client()

    dns_entries = client.get('/domain/zone/{}/record'.format(zone),
                         subDomain=subdomain)

    return dns_entries

def get_dns_entry_content(zone, id):
    return {
        'subdomain': 'entry-0',
        'fieldtype': 'A',
        'ttl': 3600,
        'id': 5110317860,
        'target': '127.0.0.1',
        'zone': 'hashicorp4noobs.fr',
    }
    # "subDomain": "entry-0",
    # "fieldType": "A",
    # "ttl": 3600,
    # "id": 5110317860,
    # "target": "127.0.0.1",
    # "zone": "hashicorp4noobs.fr",
