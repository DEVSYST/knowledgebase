# FILE CREATED DURING CODE REVIEW 17.01.2017


class AtelierManager(model.Manager):
    def get_stuff(self, owner):
        self.get_queryset().filter(owner__name='henk').order_by('date')


class Atelier(model.Model):
    objects = AtelierManager()

    owner = models.ForeignKey('Owner')
    workers = models.ManyToManyField('Workers', through='WorkersGet')
    name = model.Charf()

    def get_ateliers(worker_name):
        a = Workers.objects.get(name=worker_name)
        return self.filter(worker_id=a.id)
        return 
    
    class Meta:
        ordering = ('date',)
        
Atelier.objects.get_stuff()

Atelier.objects.filter(workers__name='henk')


from django.core.exceptions import ObjectDoesNotExist
from vadain.webservice.rpi.models.device import DeviceTypesSet, DeviceTypeEvents
from vadain.webservice.rpi.models.prod import ProdEvents


class DeviceType(model.Model):
    
    @property
    def event_name(self):
        return self.prod_event.name


def get_device_details(device_name):
    try:
        device_type = DeviceTypesSet.objects.get(device__name=device_name)
        device_type_event = DeviceTypeEvents.objects.get(device_id=device_type.device.device_id)
        prod_event = ProdEvents.objects.get(event_id=device_type_event.event_id)
    except ObjectDoesNotExist:
        return None
    device_item = DeviceDetailItem
    device_item.id = device_type.device.device_id
    device_item.name = device_type.device.name
    device_item.description = device_type.device.description
    device_item.ip_address = device_type.ip_address
    device_item.event_name = prod_event.description
    return device_item


w = Worker.objects.filter(name='henk').exists()
print w.query

Worker.objects.get_or_create(name='henk')

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.debug("hi i log here")
logger.info("this can be seen")


class Henk(object):
    def __init__(self, employee_id, device_id, status_change_id, order_nr, close_date, language, error_msg, event_id):
        self.employee_id = employee_id
        self.device_id = device_id
        self.status_change_id = status_change_id
        self.order_nr = order_nr
        self.close_date = close_date
        self.language = language
        self.error_msg = ''
        self.event_id = event_id
        self.rowcount = False

    def initialize():
        # Close_Record run procedure
        self.close_order_update_order_traffic()
        self.update_order_options()
        self.update_order_status()
self.return_result_msg()

a = Henk()
a.initialize()

class henkTest(TestCase):
    def test_henk_init(self):
        a = Henk()
        a.initialize()
        # assertins go here
    
    def test_henk_close_order_update_order_traffic(self):
        a = henk()
        a.close_order_update_order_traffic()
        # assetions

class RPIVadainOrderOptions(models.Model):
    # field
    def close(self, #args):
        # put stuff here
    
