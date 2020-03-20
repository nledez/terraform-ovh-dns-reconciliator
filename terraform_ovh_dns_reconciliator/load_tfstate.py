import json


def load_tfstate(filename):
    dns_entries = []

    with open(filename) as json_data:
        data = json.load(json_data)
        resources = data.get('resources', [])

        # Extract each resources
        for resource in resources:
            resource_type = resource.get('type', None)

            # Manage only ovh_domain_zone_record terraform type
            if resource_type == 'ovh_domain_zone_record':
                for instance in resource.get('instances', []):
                    # Extract and append attributes to dns_entries
                    dns_entries.append(instance.get('attributes', {}))

    return dns_entries
