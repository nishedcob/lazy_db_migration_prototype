
import datetime
from django.db.models.signals import post_init
from django.dispatch import receiver

from data.models import Thing, SubThing

@receiver(post_init, sender=Thing)
@receiver(post_init, sender=SubThing)
def thing_update_last_accessed(sender, instance, **kwargs):
    if sender == Thing:
        print("A Thing was just accessed: {}".format(instance), flush=True)
        instance.last_accessed = datetime.datetime.utcnow()
        instance.save(update_fields=['last_accessed'])
        print("A Thing just had its access time updated: {}".format(instance), flush=True)
    elif sender == SubThing:
        print("A SubThing was just accessed: {}".format(instance), flush=True)
