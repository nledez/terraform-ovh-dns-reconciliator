import ovh

from terraform_ovh_dns_reconciliator import load_dns_entries
from terraform_ovh_dns_reconciliator import delete_entry


def search_orphan(tfstate_content):
    '''
    Get OVH DNS entries doesn't link to tfstate
    '''
    orphans = {}

    # Iterate over each tfstate entry
    for entry in tfstate_content:
        # Extract needed information
        subdomain = entry['subdomain']
        fieldtype = entry['fieldtype']
        current_id = entry['id']
        zone = entry['zone']

        # Get current DNS entries ID
        dns_entries = load_dns_entries(zone, fieldtype, subdomain)
        # print(dns_entries)
        # Remove current terraform ID
        # print(current_id)
        try:
            dns_entries.remove(int(current_id))
        except ValueError:
            pass
            # print('{} is not in dns_entries'.format(current_id))
        # Append current orphans
        for dns_entry in dns_entries:
            if zone not in orphans.keys():
                orphans[zone] = []
            orphans[zone].append(dns_entry)

    return orphans


def search_orphan_with_dict(tfstate_content, dns_entries):
    '''
    Get OVH DNS entries doesn't link to tfstate
    '''
    orphans = {}

    # Iterate over each tfstate entry
    for entry in tfstate_content:
        # Extract needed information
        subdomain = entry['subdomain']
        fieldtype = entry['fieldtype']
        current_id = entry['id']
        zone = entry['zone']

        if zone not in orphans.keys():
            orphans[zone] = []

        if current_id not in dns_entries[zone]['by_id'].keys():
            orphans[zone].append(current_id)

    return orphans


def clean_orphans(id_to_delete):
    for zone in id_to_delete.keys():
        for current_id in id_to_delete[zone]:
            delete_entry(zone, current_id)


def build_tfstate_by_id_dictionary(tfstate_content):
    result = {}
    for e in tfstate_content:
        result[e['id']] = e
    return result
