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


def delete_entry(zone, current_id):
    client = ovh.Client()

    client.delete('/domain/zone/{}/record/{}'.format(zone, current_id))

def build_dns_entry_dictionary(zone):
    result = {}
    result['by_subdomain'] = {}
    result['by_id'] = {}
    for id in load_dns_entries(zone, None, None):
        entry =  get_dns_entry_content(zone, id)
        subdomain = entry['subdomain']
        if subdomain not in result['by_subdomain'].keys():
            result['by_subdomain'][subdomain] = []
        result['by_subdomain'][subdomain].append(entry)
        result['by_id'][id] = entry
    return result
