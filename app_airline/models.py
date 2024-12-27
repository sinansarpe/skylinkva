from django.db import models


from app_database.models import (
                                    ATCBadges, PilotBadges,

                                )
# Create your models here.

# =============================================================
# AIRLINE MAIN


class Airline (models.Model):

    isOnline                = models.BooleanField           ('Website is Online', default=True)

    airline_longName        = models.CharField              ('Airline Name', max_length=100, unique=True)
    airline_shortName       = models.CharField              ('Airline Short Name', max_length=20, unique=True, null=True, blank=True)
    airline_sloganFirstLine = models.CharField              ('Slogan First Line', max_length=100, null=True, blank=True,)
    airline_slogan          = models.CharField              ('Slogan',max_length=255, null=True, blank=True,)
    airline_about           = models.TextField              ('About', null=True, blank=True)
    airline_established     = models.DateField              ('Established on', null=True, blank=True)
    
   
    airline_icao            = models.CharField              ('ICAO Designator', max_length=3, unique=True)
    airline_iata            = models.CharField              ('IATA Designator', max_length=2, unique=True)

    airline_url             = models.URLField               ('URL')
    airline_email           = models.EmailField             ('E-mail', null=True, blank=True)
    airline_staff_email     = models.EmailField             ('E-mail (STAFF)', null=True, blank=True)   
    airline_noreply_email   = models.EmailField             ('E-Mail (No Reply)', null=True, blank=True)

    airline_logo            = models.ImageField             ('Logo', upload_to='uploads/airline/images/main/logos', null=True, blank=True,
                                                                    help_text='Airline main logo for DARK backgrounds')

    airline_web_copyright   = models.CharField              ('Copyright', max_length=250, null=True, blank=True)
    airline_web_warning     = models.CharField              ('Web Warning', max_length=250, null=True, blank=True,
                                                                    help_text='Warning for not real airline' )
    
    
    class Meta:
        verbose_name ="Airline Setting"
        verbose_name_plural ="Airline Settings"

    def __str__ (self):
        return self.airline_shortName
    

class AirlineLandingImage (models.Model):
    
    airline_shortName       = models.ForeignKey         (Airline, on_delete=models.CASCADE, verbose_name='Airline', null=True, blank=True)

    airline_landing_image   = models.ImageField         ('Landing Page Image', upload_to='uploads/airline/images/main/landing', null=True, blank=True,
                                                                help_text='3840x1500px')
    is_Published            = models.BooleanField       ('is Published?', default=False)    

    class Meta:
        verbose_name ="Airline Landing_Image"
        verbose_name_plural ="Airline Landing Images"
    

    def __str__ (self):
        return f"airline_landing_image"

# =============================================================
# AIRLINE PARTNERS

class Partnerships (models.Model):

    airline_shortName       = models.ForeignKey             (Airline, on_delete=models.CASCADE, verbose_name='Airline', null=True, blank=True)
    
    partner_order           = models.SmallIntegerField      ('Order', default=1)    
    partner_longName        = models.CharField              ('Partner', max_length=100, unique=True)
    partner_shortName       = models.CharField              ('Partner Abbr.', max_length=10, unique=True)

    partner_logo            = models.ImageField             ('Partner Logo',upload_to='uploads/airline/images/main/partners', null=True, blank=True,
                                                                help_text='Canvas size: 450x150px')
    partner_URL             = models.URLField               ('Partner URL')
    partner_email           = models.EmailField             ('Partner E-mail', null=True, blank=True)

    partner_since           = models.DateField              ('Partner Since', null=True, blank=True)
    partner_active          = models.BooleanField           ('Partnership is approved', default=False)    

    class Meta:
        verbose_name ="Partner"
        verbose_name_plural ="Partners"

    def __str__ (self):
        return self.partner_shortName


# =============================================================
# AIRLINE OFFERS

class Offers (models.Model):

    airline_shortName       = models.ForeignKey             (Airline, on_delete=models.CASCADE, verbose_name='Airline')

    offer_order             = models.SmallIntegerField      ('Order', default=1)
    offer_icon              = models.CharField              ('Icon', max_length=50, null=True, blank=True,
                                                                help_text='Favicon or others can be used')
    offer_title             = models.CharField              ('Title', max_length=100, unique=True)
    offer_content           = models.TextField              ('Content', help_text='What we offer description')
    offer_published         = models.BooleanField           ('is Published', default=False)

    class Meta:
        verbose_name ="Offer"
        verbose_name_plural ="Offers"

    def __str__ (self):
        return self.offer_title 


# =============================================================
# STAFF POSITIONS

class StaffPositions (models.Model):

    airline_shortName       = models.ForeignKey         (Airline, on_delete=models.CASCADE, verbose_name='Airline', null=True, blank=True)

    staff_order             = models.SmallIntegerField  ('Order #', default=1)
    staff_title             = models.CharField          ('Title', max_length=100, unique=True)
    staff_title_abbr        = models.CharField          ('Abbr.', max_length=5, unique=True)
    staff_position_brief    = models.CharField          ('Brief Description of Position', max_length=255, null=True, blank=True)
    staff_job_description   = models.TextField          ('Job Description', null=True, blank=True)
    staff_job_specification = models.TextField          ('Job Specification', null=True, blank=True)
    staff_pos_hiring        = models.BooleanField       ('Hiring', default=False)
    staff_pos_email         = models.EmailField         ('Staff E-mail', null=True, blank=True)


    class Meta:
        verbose_name ="Staff Position"
        verbose_name_plural ="Staff Positions"

    def __str__ (self):
        return self.staff_title

class StaffPositionRevisions (models.Model):

    staff_title             = models.ForeignKey         (StaffPositions, on_delete=models.CASCADE, verbose_name='Staff Position')
    spr_title               = models.CharField          ('Revision Title', max_length=50)
    spr_content             = models.TextField          ('Content')

    spr_date                = models.DateField          ('Date')
    spr_isPublished         = models.BooleanField       ('is Published', default=False)    

    class Meta:
        verbose_name ="Staff Position"
        verbose_name_plural ="Staff Positions"

    def __str__ (self):
        return self.staff_title

# =============================================================
# AIRLINE BADGES

class AirlineBadges (models.Model):

    airline_shortName       = models.ForeignKey             (Airline, on_delete=models.CASCADE, verbose_name='Airline', null=True, blank=True) 
    
    badge_order             = models.SmallIntegerField      ('Order #', default=1)           
    #pilot_title             = models.ForeignKey            (CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    pilot_title             = models.CharField              ('Title', max_length=100,unique=True)
    pilot_title_abbr        = models.CharField              ('Title Abbr', max_length=5, unique=True)
    pilot_badge             = models.ImageField             ('Badge', upload_to='uploads/airline/badges/airline/pilot', null=True, blank=True)
    req_hours               = models.SmallIntegerField      ('Hours', default=0)
    req_pireps              = models.SmallIntegerField      ('PIREPS', default=0)
    req_points              = models.SmallIntegerField      ('Points', default=0)
    req_bonus_points        = models.SmallIntegerField    ('Bonus Points', default=0)
    req_atc_badge           = models.ForeignKey             (ATCBadges, on_delete=models.CASCADE, verbose_name='Required ATC Badge', null=True, blank=True)
    req_pilot_badge         = models.ForeignKey             (PilotBadges, on_delete=models.CASCADE, verbose_name='Required Pilot Badge', null=True, blank=True)
    description             = models.TextField              ('Description', null=True, blank=True)
    
    class Meta:
        verbose_name ="Airline Pilot Badge"
        verbose_name_plural ="Airline Pilot Badges"

    def __str__ (self):
        return self.pilot_title    

# =============================================================
# FREQUENTLY ASKED QUESTIONS

class FaqCategories( models.Model):
    cat_order               = models.SmallIntegerField      ('Order', default=1)
    cat_name                = models.CharField              ('Category Name', max_length=100)
    cat_icon                = models.CharField              ('Category Icon', max_length=100, help_text="fontawesome icon or others")

    class Meta:
        verbose_name ="FAQ Category"
        verbose_name_plural ="FAQ Categories"

    def __str__ (self):
        return self.cat_name   

class Faq( models.Model):

    cat_name                = models.ForeignKey              (FaqCategories, on_delete=models.CASCADE, verbose_name='Category', null=True, blank=True)

    faq_order               = models.SmallIntegerField       ('Order', default=1)    
    faq_question            = models.CharField               ('Question', max_length=250, null=True, blank=True)
    faq_answer              = models.TextField               ('Answer')
   
    class Meta:
        verbose_name ="FAQ - Frequently Asked Question"
        verbose_name_plural ="FAQ - Frequently Asked Questions"

    def __str__ (self):
        return self.faq_question
    
# =============================================================
# LATEST NEWS

class News (models.Model):

    news                    = models.TextField              ('News')
    news_img                = models.ImageField             ('News Image', upload_to='uploads/airline/news/images', null=True, blank=True, help_text='Use 16:9 resolution images.')
    news_date               = models.DateField              ('Date', auto_now_add=True)
    is_published            = models.BooleanField           ('is Published', default=False)

    class Meta:
        verbose_name ="Skylink News"
        verbose_name_plural ="Skylink News"

    def __str__ (self):
        return self.news
    
# =============================================================
# BASE & HUBS

class BaseHubs (models.Model):

    order                   = models.SmallIntegerField      ('Fleet Order', default=1)    
    airport                 = models.CharField              ('Airport', max_length=100, help_text='Esenboga International Airport')        
    city                    = models.CharField              ('Airport City', max_length=50, help_text='Ankara')
    icao                    = models.CharField              ('Airport ICAO', max_length=4, help_text='LTAC')
    iata                    = models.CharField              ('Airport IATA', max_length=3, help_text='ESB')
    image                   = models.ImageField             ('Airport Image', upload_to='uploads/airline/base-hubs/images', null=True, blank=True)
    link                    = models.URLField               ('Link', null=True, blank=True,help_text='https://en.wikipedia.org/wiki/Istanbul_Airport')
    is_base                 = models.BooleanField           ('Base Airport', default=False)
    is_hub                  = models.BooleanField           ('Hub Airport', default=False)

    is_scheduled            = models.BooleanField           ('Scheduled', default=False)
    is_charter              = models.BooleanField           ('Charter', default=True)
    is_cargo                = models.BooleanField           ('Cargo', default=False)

    class Meta:
        verbose_name ="Airport"
        verbose_name_plural ="Airports"

    def __str__ (self):
        return self.airport 

class Scenery (models.Model):

    airport                 = models.ForeignKey             (BaseHubs, on_delete=models.CASCADE, verbose_name='Airport')
    image                   = models.ImageField             ('Scenery Image', upload_to='uploads/airline/basehubs/scenery/images', null=True, blank=True)
    publisher               = models.CharField              ('Publisher', max_length=100)
    publisher_url           = models.URLField               ('Publisher URL')

    is_free                 = models.BooleanField           ('Free', default=False)
    is_payware              = models.BooleanField           ('Payware', default=False)

    supports                = models.CharField              ('Supports', max_length=100, help_text='MSFS20 & MSFS24')


    class Meta:
        verbose_name ="Scenery"
        verbose_name_plural ="Sceneries"

    def __str__ (self):
        return self.publisher 
    
# =============================================================
# FLEET

class Fleet (models.Model):
    
    order                   = models.SmallIntegerField      ('Fleet Order', default=1)
    name                    = models.CharField              ('Fleet Name', max_length=100, help_text='Boeing 737-600')
    designator              = models.CharField              ('Designator', max_length=5, help_text='B736')
    publisher               = models.CharField              ('Publisher', max_length=100)
    publisher_url           = models.URLField               ('Publisher URL')
    publisher_logo          = models.ImageField             ('Publisher Logo', upload_to='uploads/airline/fleet/images', null=True, blank=True)

    class Meta:
        verbose_name ="Fleet"
        verbose_name_plural ="Fleets"

    def __str__ (self):
        return self.designator    
    

class Aircraft (models.Model):
    
    Type_of_flight_choices  = (

                                ("Scheduled", "Scheduled"),
                                ("Charter","Charter"),
                                ("Cargo", "Cargo"),
                                ("General Aviation", "General Aviation"),                    
                            )
    
    
    
    
    is_active               = models.BooleanField           ('Active', default=False)
    
    designator              = models.ForeignKey             (Fleet, on_delete=models.CASCADE, null=True, blank=True)
    registration            = models.CharField              ('Registration', max_length=10, unique=True, help_text='TC-SLA')
    type_of_flight          = models.CharField              ('Type of Flight', max_length=30, choices=Type_of_flight_choices, default="Charter", null=True, blank=True)
    max_passengers          = models.SmallIntegerField      ('Maximum Passengers', default=1)
    engine_type             = models.CharField              ('Engine Type', max_length=30, null=True, blank=True)
    airport                 = models.ForeignKey             (BaseHubs, on_delete=models.CASCADE, verbose_name='Aircraft Base')
    image                   = models.ImageField             ('Image', upload_to='uploads/airline/fleet/airframe/images', null=True, blank=True, help_text='16:9 Resolution')
    description             = models.TextField              ('About Fleet', null=True, blank=True, help_text='Some information about fleet')


    
    is_commercial           = models.BooleanField           ('Commercial', default=False)
    is_charter              = models.BooleanField           ('Charter', default=False)
    is_cargo                = models.BooleanField           ('Freighter', default=False)
    is_training             = models.BooleanField           ('Training', default=False)

    livery_URL              = models.URLField               ('Livery Download Link')


    class Meta:
        verbose_name ="Aircraft"
        verbose_name_plural ="Aircraft"

    def __str__ (self):
        return self.registration

# =============================================================
# RULES AND REGULATIONS:

class RulesRegulations (models.Model):
    rules_order      = models.SmallIntegerField  ('Order', default=1)
    title            = models.CharField          ('Title', max_length=100,)
    content          = models.TextField          ('Content')

    class Meta:
        verbose_name ="Rule"
        verbose_name_plural ="Rules"

    def __str__ (self):
        return self.title  

class RulesRegulationsUpdate (models.Model):

    title           = models.ForeignKey         (RulesRegulations, on_delete=models.CASCADE, verbose_name='Title')
    content         = models.TextField          ('Update')
    date            = models.DateField          ('Date Applied', auto_now_add=True)

    class Meta:
        verbose_name ="Rule Update"
        verbose_name_plural ="Rule Updates"


# =============================================================
# FLIGHT OPERATIONS:

class FlightOperations (models.Model):

    title            = models.CharField          ('Title', max_length=100,)
    content          = models.TextField          ('Content')

    class Meta:
        verbose_name ="Flight Operation"
        verbose_name_plural ="Flight Operations"

    def __str__ (self):
        return self.title

class FlightOperationsUpdate (models.Model):

    title           = models.ForeignKey         (FlightOperations, on_delete=models.CASCADE, verbose_name='Title')
    content         = models.TextField          ('Update')
    date            = models.DateField          ('Date Applied', auto_now_add=True)

    class Meta:
        verbose_name ="Flight Operations Update"
        verbose_name_plural ="Flight Operations Updates"

# =============================================================
# RANKING SYSTEM:

class RankingSystem (models.Model):
    ranking_order    = models.SmallIntegerField  ('Ranking Order', default=1)
    title            = models.CharField          ('Title', max_length=100,)
    content          = models.TextField          ('Content')

    class Meta:
        verbose_name ="Ranking"
        verbose_name_plural ="Rankings"

    def __str__ (self):
        return self.title 

class RankingSystemUpdate (models.Model):

    title           = models.ForeignKey         (RankingSystem, on_delete=models.CASCADE, verbose_name='Title')
    content         = models.TextField          ('Update')
    date            = models.DateField          ('Date Applied', auto_now_add=True)

    class Meta:
        verbose_name ="Ranking System Update"
        verbose_name_plural ="Ranking System Updates"

class Downloads (models.Model):

    title            = models.CharField          ('Title', max_length=100,)
    content          = models.TextField          ('Content')
    link             = models.URLField           ('Link')

    class Meta:
        verbose_name ="Download"
        verbose_name_plural ="Downloads"

    def __str__ (self):
        return self.title 
    
# =============================================================
# SCHEDULED FLIGHTS:

class ScheduledFlights (models.Model):

    flight_number     = models.SmallIntegerField    ('Flight Number', help_text='Number only: 102')
    callsign          = models.CharField            ('Callsign', max_length=3, help_text='3 Chars only : 3EG')
    departure         = models.CharField            ('Departure Airport', max_length=50, help_text='City and IATA: Bodrum/BJV')
    arrival           = models.CharField            ('Arrival Airport', max_length=50, help_text='City and IATA: Ankara/ESB')
    aircraft          = models.ForeignKey           (Aircraft, on_delete=models.CASCADE, verbose_name='Assigned Aircraft', null=True, blank=True) 
    is_active         = models.BooleanField         ('is Active', default=False)

    class Meta:
        verbose_name ="Scheduled Flight (Everyday)"
        verbose_name_plural ="Scheduled Flights (Everyday)"

    def __str__ (self):
        return self.callsign
    


# =============================================================
# PRIVACY POLICY


class PrivacyPolicy (models.Model):

    order           = models.SmallIntegerField          ('Order')
    title           = models.CharField                  ('Title', max_length=100)
    content         = models.TextField                  ('Content')

    class Meta:
        verbose_name ="Privacy Policy Title"
        verbose_name_plural ="Privacy Policy Titles"

    def __str__ (self):
        return self.title 