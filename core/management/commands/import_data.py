import json
from django.core.management.base import BaseCommand
from core.models import Boek, Film, FodmapItem


class Command(BaseCommand):
    help = 'Import data from JSON files into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--boeken',
            type=str,
            help='Path to boekenlijst.json'
        )
        parser.add_argument(
            '--films',
            type=str,
            help='Path to filmlijst.json'
        )
        parser.add_argument(
            '--fodmap',
            type=str,
            help='Path to fodmaplijst.json'
        )

    def handle(self, *args, **options):
        if options['boeken']:
            self.import_boeken(options['boeken'])

        if options['films']:
            self.import_films(options['films'])

        if options['fodmap']:
            self.import_fodmap(options['fodmap'])

    def import_boeken(self, filepath):
        self.stdout.write(f'Importing books from {filepath}...')

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count = 0
        for item in data:
            Boek.objects.get_or_create(
                voornaam=item.get('voornaam', ''),
                achternaam=item.get('achternaam', ''),
                titel=item.get('titel', ''),
                defaults={
                    'beschrijving': item.get('beschrijving', ''),
                    'taal': item.get('Taal', item.get('taal', '')),
                    'opmerking': item.get('Opmerking', item.get('opmerking', '')),
                }
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} books'))

    def import_films(self, filepath):
        self.stdout.write(f'Importing films from {filepath}...')

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count = 0
        for item in data:
            Film.objects.get_or_create(
                titel=item.get('titel', ''),
                defaults={
                    'regisseur': item.get('regiseur', item.get('regisseur', '')),
                    'schrijver': item.get('schrijver', ''),
                    'acteurs': item.get('acteurs', ''),
                    'jaar': item.get('jaar', ''),
                    'beschrijving': item.get('beschrijving', ''),
                    'taal': item.get('Taal', item.get('taal', '')),
                }
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} films'))

    def import_fodmap(self, filepath):
        self.stdout.write(f'Importing FODMAP items from {filepath}...')

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count = 0
        for item in data:
            # Find the category key (it's not 'groep')
            categorie = None
            naam = None
            for key, value in item.items():
                if key != 'groep':
                    categorie = key
                    naam = value
                    break

            if categorie and naam:
                FodmapItem.objects.get_or_create(
                    categorie=categorie,
                    naam=naam,
                    defaults={
                        'groep': item.get('groep', ''),
                    }
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} FODMAP items'))
