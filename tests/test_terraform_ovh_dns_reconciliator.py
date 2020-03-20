import pytest
import os

from terraform_ovh_dns_reconciliator import load_tfstate

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def test_load_tfstate_with_one_dns_record():
    ex1_filepath = os.path.join(DIR_PATH, 'terraform_ex1.tfstate')
    tfstate_content = load_tfstate(ex1_filepath)

    tfstate_assert = [
        {
            "fieldtype": "A",
            "id": "5110317618",
            "subdomain": "entry-0",
            "target": "127.0.0.1",
            "ttl": 3600,
            "zone": "hashicorp4noobs.fr"
        },
    ]

    assert tfstate_content == tfstate_assert


def test_load_tfstate_with_three_dns_records():
    ex2_filepath = os.path.join(DIR_PATH, 'terraform_ex2.tfstate')
    tfstate_content = load_tfstate(ex2_filepath)


    tfstate_assert = [
        {
            "fieldtype": "A",
            "id": "5110317618",
            "subdomain": "entry-0",
            "target": "127.0.0.1",
            "ttl": 3600,
            "zone": "hashicorp4noobs.fr"
        },
        {
            "fieldtype": "A",
            "id": "5110317621",
            "subdomain": "entry-1",
            "target": "127.0.0.1",
            "ttl": 3600,
            "zone": "hashicorp4noobs.fr"
        },
        {
            "fieldtype": "A",
            "id": "5110317622",
            "subdomain": "entry-2",
            "target": "127.0.0.1",
            "ttl": 3600,
            "zone": "hashicorp4noobs.fr"
        },
    ]

    assert tfstate_content == tfstate_assert
