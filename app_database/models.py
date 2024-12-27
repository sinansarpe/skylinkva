from django.db import models

#from app_users.models import CustomUser
# Create your models here.

# =============================================================
# NETWORKS

class Networks (models.Model):

    network_name            = models.CharField          ('Network Name', max_length=100, unique=True)
    network_abbr            = models.CharField          ('Network Abbr.', max_length=10, 
                                                                help_text='IVAO / VATSIM etc.')
    network_url             = models.URLField           ('Network Link', null=True, blank=True)
    network_logo            = models.ImageField         ('Network Logo', upload_to='uploads/airline/images/partners', null=True, blank=True,
                                                                help_text='Image Size: 450x150 px.')
    class Meta:
        verbose_name ="Network"
        verbose_name_plural ="Networks"

    def __str__ (self):
        return self.network_name

# =============================================================
# BADGES

class PilotBadges (models.Model):

    network_name       = models.ForeignKey            (Networks, on_delete=models.CASCADE, verbose_name='Network')

    badge_order        = models.SmallIntegerField     ('Order', default=1)    
    #pilot_title        = models.ForeignKey            (CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    pilot_title        = models.CharField             ('Title', max_length=100, unique=True, null=True, blank=True)
    pilot_title_abbr   = models.CharField             ('Title Abbr', max_length=5, unique=True)
    pilot_badge        = models.ImageField            ('Badge', upload_to='uploads/airline/images/badges/ivao/pilot',  null=True, blank=True, 
                                                                help_text='IVAO ATC Badges')

    class Meta:
        verbose_name ="Pilot Badge"
        verbose_name_plural ="Pilot Badges"

    def __str__ (self):
        return self.pilot_title  


class ATCBadges (models.Model):

    network_name            = models.ForeignKey     (Networks, on_delete=models.CASCADE, verbose_name='Network')

    badge_order      = models.SmallIntegerField     ('Order', default=1)    
    #atc_title        = models.ForeignKey            (CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    atc_title        = models.CharField             ('Title', max_length=100, unique=True, null=True, blank=True)
    atc_title_abbr   = models.CharField             ('Title Abbr', max_length=5, unique=True)
    atc_badge        = models.ImageField            ('Badge', upload_to='uploads/airline/images/badges/ivao/atc', null=True, blank=True, 
                                                                help_text='IVAO ATC Badges')
    class Meta:
        verbose_name ="ATC Badge"
        verbose_name_plural ="ATC Badges"

    def __str__ (self):
        return self.atc_title  

# =============================================================
# DIVISIONS

class Divisions (models.Model):

    network_name            = models.ForeignKey         (Networks, on_delete=models.CASCADE, verbose_name='Network')
    
    division_name           = models.CharField          ('Division Name', max_length=40, unique=True, null=True, blank=True)
    division_abbr           = models.CharField          ('Division Abbr.', max_length=2, )

    class Meta:
        verbose_name ="IVAO Division"
        verbose_name_plural ="IVAO Divisions"

    def __str__ (self):
        return self.division_abbr

# =============================================================

