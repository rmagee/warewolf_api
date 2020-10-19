#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_warewolf_api
------------

Tests for `warewolf_api` models module.
"""
import os
from rest_framework.test import APITestCase as TestCase
from django.contrib.auth import get_user_model
from quartet_epcis.parsing.business_parser import BusinessEPCISParser
from quartet_masterdata.models import TradeItem, Company
from django.urls import reverse
from quartet_epcis.models.entries import Entry

from warewolf_api import models


class TestWarewolf_api(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='unittest',
            email='testuser@seriallab.local'
        )
        user.save()
        self.client.force_authenticate(user=user)
        self.user = user

    def _create_trade_item(self):
        company = Company.objects.create(name='test company')
        TradeItem.objects.create(
            GTIN14='00777220112102',
            NDC='7722-0112-10',
            company=company
        )

    def test_get_item_detail(self):
        self._parse_test_data()
        url = reverse('item-detail',
                      kwargs={"barcode": '0100777220112102212PWT46W493'})
        self._create_trade_item()
        response = self.client.get(
            '{0}?0100777220112102212PWT46W493'.format(url))
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_try_bad_cp(self):
        self._parse_test_data()
        url = reverse('item-detail',
                      kwargs={"barcode": '0100377220112102212PWT46W493'})
        self._create_trade_item()
        response = self.client.get(
            '{0}?0100777220112102212PWT46W493'.format(url))
        self.assertEqual(response.status_code, 400)
        self.assertIn('Trade Item', response.data['message'])
        print(response.data)

    def test_try_bad_sn(self):
        self._parse_test_data()
        url = reverse('item-detail',
                      kwargs={"barcode": '0100777220112102212PWT46W49f'})
        self._create_trade_item()
        response = self.client.get(
            '{0}?0100777220112102212PWT46W49A'.format(url))
        self.assertEqual(response.status_code, 400)
        self.assertIn('Could not find', response.data['message'])
        print(response.data)

    def test_decommission_children(self):
        self._parse_test_data()
        url = reverse('decommission-parent',
                      kwargs={'child_urn': 'urn:epc:id:sgtin:077722.0011210.11X8KN3H4W'}
                      )
        parent = 'urn:epc:id:sgtin:077722.0011210.12CW68RW6G'
        children = Entry.objects.filter(parent_id__identifier='urn:epc:id:sgtin:077722.0011210.12CW68RW6G')
        self.assertEqual(children.count(), 18)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        children = Entry.objects.filter(
        parent_id__identifier='urn:epc:id:sgtin:077722.0011210.12CW68RW6G')
        self.assertEqual(children.count(), 0)


    def tearDown(self):
        pass

    def _parse_test_data(self, test_file='data/epcis.xml',
                         recursive_decommission=False):
        curpath = os.path.dirname(__file__)
        parser = BusinessEPCISParser(
            os.path.join(curpath, test_file),
            recursive_decommission=recursive_decommission
        )
        message_id = parser.parse()
        print(parser.event_cache)
        return message_id, parser
