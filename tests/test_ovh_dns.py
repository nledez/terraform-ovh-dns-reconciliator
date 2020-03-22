import pytest
import ovh

from unittest import mock

from terraform_ovh_dns_reconciliator import load_dns_entries

def test_search_dns_records_with_one_entry():
    with mock.patch.object(ovh, 'Client') as mocked_client:
        mocked_client.return_value.get.return_value = [5110321661]
        dns_entries = load_dns_entries('hashicorp4noobs.fr', 'entry-1')

        assert dns_entries == [5110321661]
