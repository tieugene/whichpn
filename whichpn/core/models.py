from django.db import models
from django.utils.translation import gettext as _


class OpSoS(models.Model):
    """Subj."""
    tin = models.BigIntegerField(primary_key=True, verbose_name=_('TIN'))
    name = models.CharField(max_length=239, verbose_name=_('Name'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'opsos'
        ordering = ('tin',)
        verbose_name = _('OpSoS')
        verbose_name_plural = _('OpSoSes')


class SNRange(models.Model):
    """Phone number ranges.
    MSISDN = CC+NDC+SN (subscriber nuber)
    """
    ndc = models.PositiveSmallIntegerField(db_index=True, verbose_name=_('NDC'))  # 3 (up to 32k)
    beg = models.PositiveIntegerField(db_index=True, verbose_name=_('SN from'))  # 7 (up 2 2G=9)
    end = models.PositiveIntegerField(db_index=True, verbose_name=_('SN to'))
    opsos = models.ForeignKey(OpSoS, on_delete=models.CASCADE, verbose_name=_('OpSoS'))
    region = models.CharField(max_length=526, verbose_name=_('Region'))  # 526

    def __str__(self):
        return f"{self.ndc:03d}{self.beg:07d}: {self.opsos} @ {self.region}"

    class Meta:
        # TODO: indexes [together]
        db_table = 'snrange'
        unique_together = (('ndc', 'beg'),)
        ordering = ('ndc', 'beg')
        verbose_name = _('SN Range')
        verbose_name_plural = _('SN Ranges')
