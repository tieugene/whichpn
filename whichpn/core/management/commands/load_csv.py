"""Manage command to reload data from CSV.

:todo: Speedup
"""

from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _
from settings import SPECIAL
from core.models import OpSoS, SNRange
from util import csv_handle


class Command(BaseCommand):
    """Load CSV data."""
    help = _("Load and replace data from CSV file")

    def add_arguments(self, parser):
        parser.add_argument('ndc', type=int)
        parser.add_argument('csv_source', type=str)

    def handle(self, *args, **options):
        """Handle command line."""
        ndc = options['ndc']  # chk in 1..9
        src_path = options['csv_source']
        if not (csv_rows := csv_handle(ndc, src_path, SPECIAL)):
            print("Something went wrong.")
        else:
            SNRange.objects.filter(ndc__gte=ndc*100, ndc__lte=(ndc*100)+99).delete()  # 1. del old
            for row in csv_rows:
                OpSoS.objects.get_or_create(tin=row[6], defaults={'name': row[4]})  # 2. Find or Add OpSoS
                SNRange.objects.create(  # 3. add the record
                    ndc=row[0],
                    beg=row[1],
                    end=row[2],
                    opsos_id=row[6],
                    region=row[5]
                )
            print("OK")

    def __handle_sample(self):
        for u in SNRange.objects.all():
            try:
                s = OpSoS.objects.get(user=u)
            except OpSoS.DoesNotExist:
                s = OpSoS(user=u, settings=SPECIAL)
                s.save()
