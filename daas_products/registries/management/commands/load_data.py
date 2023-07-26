# load_data.py
from django.core.management.base import BaseCommand
from registries.models import (Salutation, Gender, MaritalStatus, EducationLevel, Position,
                             Region, Zone, Woreda, Kebele, Specialisation)
import pandas as pd

class Command(BaseCommand):
    help = 'Load data into models'

    def handle(self, *args, **options):

        # Salutation
        salutations = ['Ato', 'W/ro', 'W/t', 'Dr.']
        for salutation in salutations:
            Salutation.objects.get_or_create(name=salutation)

        # Gender
        genders = ['Male', 'Female']
        for gender in genders:
            Gender.objects.get_or_create(name=gender)

        # Marital Status
        marital_statuses = ['Single', 'Married', 'Separated', 'Divorced', 'Widowed']
        for status in marital_statuses:
            MaritalStatus.objects.get_or_create(name=status)

        # Education Level
        education_levels = ['Phd', '2nd Degree', '1st Degree', 'Diploma', 'Level IV', 'Level III', 'Level II', 'Level I']
        for level in education_levels:
            EducationLevel.objects.get_or_create(name=level)

        # Specialisation
        specialisation = ['Animal Production', 'Animal Health', 'Animal Feed Production', 'Small Scale Irrigation', 
                        'Natural Resource Management', 'Cooperative Management', 'Land Administration', 
                        'Apiculture Technician', 'Artificial Insemination (AI)', 'Agricultural Mechanization', 
                        'Rural Development And Extension', 'General Agriculture', 'Horticulture', 'Animal Science', 
                        'Plant Science', 'Poultry Production', 'Soil &Water Conservation', 'Agroforestry', 'Fishery', 
                        'Dairy Production', 'Bee Keeping Technicians', 'Agricultural Economics', 
                        'Agricultural Resources Economics And Management', 'Natural Resources Economics And Management', 
                        'Post-Harvest Technologies', 'Agribusiness Value Chain Analysis', 'Agronomy', 
                        'Climate-Smart Agriculture', 'Forest Economics', 'Agricultural Production', 'Environmental Economics', 'Other']
        for specialisation in specialisation:
            Specialisation.objects.get_or_create(name=specialisation)

        # Position
        positions = ['Development Agent', 'Head Of Kebele Agricultural Office']
        for position in positions:
            Position.objects.get_or_create(name=position)

        # Load the CSV data into a pandas DataFrame
        df = pd.read_csv('daas_products/daas_products/data/rzwk.csv') 
        # Iterate over the rows in the DataFrame
        for index, row in df.iterrows():
            # Retrieve or create Region
            region, created = Region.objects.get_or_create(name=row['Region'])
            
            # Retrieve or create Zone
            zone, created = Zone.objects.get_or_create(name=row['Zone'], region=region)
            
            # Retrieve or create Woreda
            woreda, created = Woreda.objects.get_or_create(name=row['Woreda'], zone=zone)
            
            # Retrieve or create Kebele
            if not Kebele.objects.filter(name=row['Kebele'], woreda=woreda).exists():
            # If not, create Kebele
                kebele, created = Kebele.objects.get_or_create(name=row['Kebele'], woreda=woreda)
        
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
