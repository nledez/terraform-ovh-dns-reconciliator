import ovh

from unittest import mock

from terraform_ovh_dns_reconciliator import search_orphan
def diff_orphan_list(a1, a2):
    if a1.keys() != a2.keys():
        return False
    for k in a1.keys():
        if a1[k].sort() != a2[k].sort():
            return False
    return True

def test_detect_orphan_entries():
    with mock.patch.object(ovh, 'Client') as mocked_client:
        mocked_client.return_value.get.return_value = [5110317618, 9876543210]
        tfstate_content = [
            {
                "fieldtype": "A",
                "id": "5110317618",
                "subdomain": "entry-0",
                "target": "127.0.0.1",
                "ttl": 3600,
                "zone": "hashicorp4noobs.fr"
            },
        ]

        orphan_list = search_orphan(tfstate_content)

        assert diff_orphan_list(orphan_list, {
            'hashicorp4noobs.fr': [9876543210],
        })

def test_detect_another_orphan_entries():
    with mock.patch.object(ovh, 'Client') as mocked_client:
        mocked_client.return_value.get.side_effect = [
            [1234567890, 6789012345],
            [3456789012, 2345678901],
        ]
        tfstate_content = [
            {
                "fieldtype": "A",
                "id": "1234567890",
                "subdomain": "entry-1",
                "target": "127.0.0.1",
                "ttl": 3600,
                "zone": "hashicorp4noobs.fr"
            },
            {
                "fieldtype": "A",
                "id": "2345678901",
                "subdomain": "entry-2",
                "target": "127.0.0.1",
                "ttl": 3600,
                "zone": "hashicorp4noobs.fr"
            },
        ]

        orphan_list = search_orphan(tfstate_content)

        assert diff_orphan_list(orphan_list, {
            'hashicorp4noobs.fr': [ 3456789012, 6789012345],
        })

def test_detect_another_simple_orphan_entries():
    with mock.patch.object(ovh, 'Client') as mocked_client:
        mocked_client.return_value.get.side_effect = [
            [7890123456, 8901234567],
            [4567890123],
        ]
        tfstate_content = [
            {
                "fieldtype": "A",
                "id": "7890123456",
                "subdomain": "entry-1",
                "target": "127.0.0.1",
                "ttl": 3600,
                "zone": "hashicorp4noobs.fr"
            },
            {
                "fieldtype": "A",
                "id": "4567890123",
                "subdomain": "entry-2",
                "target": "127.0.0.1",
                "ttl": 3600,
                "zone": "hashicorp4noobs.fr"
            },
        ]

        orphan_list = search_orphan(tfstate_content)

        assert orphan_list == {
            'hashicorp4noobs.fr': [8901234567],
        }
