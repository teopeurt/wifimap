from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import simplejson

from spots.models import AccessPoint

class JsonPointTest(TestCase):
    
    def setUp(self):
        self.access_point = AccessPoint.objects.create(name='point 1', description='Point 1 description', address='Rio de Janeiro, Brazil', lat=-22.9963233069, lng=-43.3637237549)
        self.url = reverse('spot_json_detail', args=[self.access_point.id])
        self.response = self.client.get(self.url)
        
    def tearDown(self):
        AccessPoint.objects.all().delete()
        
    def test_view_exists(self):
        assert 200 == self.response.status_code
        
    def test_view_returns_json(self):
        assert self.response.items()[0][1] == 'application/json'
        
    def test_name_in_json(self):
        assert 'point 1' in simplejson.loads(self.response.content)['name']

    def test_id_in_json(self):
        assert self.access_point.id == simplejson.loads(self.response.content)['id']
        
    def test_address_in_json(self):
        assert 'Rio de Janeiro, Brazil' == simplejson.loads(self.response.content)['address']