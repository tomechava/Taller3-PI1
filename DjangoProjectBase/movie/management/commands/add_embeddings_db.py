import os
import sys

# Add the path to the parent directory of your Django project to the Python path
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
project_directory = os.path.dirname(parent_directory)
sys.path.append(project_directory)

# Now you should be able to import the Movie model
from movie.models import Movie

from django.core.management.base import BaseCommand
from django.db import models
import json
import os
import numpy as np

class Command(BaseCommand):
    help = 'Modify path of images'

    def handle(self, *args, **kwargs):
        ##Código para leer los embeddings del archivo movie_descriptions_embeddings.json
        json_file_path = '../movie_descriptions_embeddings.json'
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            movies = json.load(file)       
  
        for movie in movies:
            emb = movie['embedding']
            emb_binary = np.array(emb).tobytes()
            item = Movie.objects.filter(title = movie['title']).first()
            item.emb = emb_binary
            item.save()
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated item embeddings'))        
        