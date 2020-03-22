import ovh

from unittest import mock

from terraform_ovh_dns_reconciliator import load_dns_entries, get_dns_entry_content


def test_search_dns_records_with_one_entry():
    with mock.patch.object(ovh, 'Client') as mocked_client:
        mocked_client.return_value.get.return_value = [1234567890]
        dns_entries = load_dns_entries('hashicorp4noobs.fr', 'entry-1')

        assert dns_entries == [1234567890]


def test_search_dns_records_with_two_entry():
    with mock.patch.object(ovh, 'Client') as mocked_client:
        mocked_client.return_value.get.return_value = [1234567890, 9876543210]
        dns_entries = load_dns_entries('hashicorp4noobs.fr', 'entry-0')

        assert dns_entries == [1234567890, 9876543210]

def test_get_entry_content():
    entry = get_dns_entry_content('hashicorp4noobs.fr', 1234567890)

    assert entry == {
        'subdomain': 'entry-0',
        'fieldtype': 'A',
        'ttl': 3600,
        'id': 5110317860,
        'target': '127.0.0.1',
        'zone': 'hashicorp4noobs.fr',
    }
