from terraform_ovh_dns_reconciliator import load_dns_entries

def search_orphan(tfstate_content):
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
        # Remove current terraform ID
        dns_entries.remove(int(current_id))
        # Append current orphans
        for dns_entry in dns_entries:
            if zone not in orphans.keys():
                orphans[zone] = []
            orphans[zone].append(dns_entry)

    return orphans
