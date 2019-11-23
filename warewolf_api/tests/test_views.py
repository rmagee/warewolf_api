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
