import ovh


def load_dns_entries(zone, fieldtype, subdomain):
    client = ovh.Client()

    dns_entries = client.get('/domain/zone/{}/record'.format(zone),
                             fieldType=fieldtype,
                             subDomain=subdomain)

    return dns_entries


def get_dns_entry_content(zone, id):
    client = ovh.Client()
    clean_entry = {}

    entry = client.get('/domain/zone/{}/record/{}'.format(zone, id))

    clean_entry = {
        'subdomain': entry['subDomain'],
        'fieldtype': entry['fieldType'],
        'target': entry['target'],
        'zone': entry['zone'],
        'ttl': entry['ttl'],
        'id': entry['id'],
    }

    return clean_entry
