from terraform_ovh_dns_reconciliator import load_dns_entries

def search_orphan(tfstate_content):
    orphans = []

    # Iterate over each tfstate entry
    for entry in tfstate_content:
        # Extract needed information
        subdomain = entry['subdomain']
        zone = entry['zone']
        current_id = entry['id']

        # Get current DNS entries ID
        dns_entries = load_dns_entries(zone, subdomain)
        # Remove current terraform ID
        dns_entries.remove(int(current_id))
        # Append current orphans
        orphans.extend(dns_entries)

    return orphans
