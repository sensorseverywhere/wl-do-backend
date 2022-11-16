from django.conf import settings
from django.db import models


class Content(models.Model):

    TYPES = (
        ('PAGE', 'Page'),
        ('ARTICLE', 'Article'),
        ('STORY', 'Story'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='content')
    type =  models.CharField(choices=TYPES, default='Page', max_length=10)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def natural_key(self):
        return (self.title)
    
    def get_all_by_author_name(self):
        return self.author


class ContentImage(models.Model):
    cb = models.ForeignKey(Content, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.image


class NewsItem(models.Model):
    url = models.CharField(max_length=256)
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image_url = models.CharField(max_length=256)
    active = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class Story(models.Model):
    DRAFT = 0
    PUBLISHED = 1
    STATUSES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    THRILLER = 0
    ROMANCE = 1
    COMEDY = 2
    GENRES = (
        (THRILLER, 'Thriller'),
        (ROMANCE, 'Romance'),
        (COMEDY, 'Comedy'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='story')
    status = models.IntegerField(choices=STATUSES, default=DRAFT)
    genre = models.IntegerField(choices=GENRES, default=COMEDY)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True, blank=True)
    live = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse('story:story_detail', args={'pk': self.pk})

    def __str__(self):
        return self.title


class UserStoryVotes(models.Model):
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.votes)


class Word(models.Model):

    TYPES = (
        ('NONE', 'None'),
        ('VERB', 'Verb'),
        ('ADVERB', 'Adverb'),
        ('ARTICLE', 'Article'),
        ('NOUN', 'Noun'),
        ('PRONOUN', 'Pronoun'),
        ('ADJECTIVE', 'Adjective'),
        ('PREPOSITION', 'Preposition'),
        ('CONJUNCTION', 'Conjunction'),
        ('CONCTRACTION', 'Contraction')
    )

    word = models.CharField(max_length=50)
    word_type = models.CharField(choices=TYPES, default='None', max_length=20)
    clause = models.ForeignKey('Clause', related_name='clauses', on_delete=models.CASCADE)


"""
    A clause can be made of many words, but words must be restricted by type. 
    Eg an INDEPENDENT clause has a SUBJECT ( Noun, Pronoun ) and a VERB

    Article  noun    verb    preposition    adverb   noun
    The      person  is      in             the      house
"""

class Clause(models.Model):
    TYPES = (
        ('NONE', 'None'),
        ('INDEPENDENT', 'Independent'),
        ('DEPENDENT', 'Dependent'),
        ('COORDINATING_CONJUNCTION', 'Coordinating-Conjunction'),
        ('SUBORDINATING_CONJUNCTION', 'Subordinating-Conjunction')
    )
    clause = models.CharField(choices=TYPES, max_length=40, default='None')
    sentence = models.ForeignKey('Sentence', related_name='sentences', on_delete=models.CASCADE)


"""
    A sentence is made of CLAUSES.
    There are 4 types
    SIMPLE = INDEPENDENT clause
    COMPOUND = 2 INDEPENDENT clauses joined by a COORDINATING CONJUNCTION
    COMPLEX = 1 INDEPENDENT clause and 1 DEPENDENT clause joined by a SUBORDINATING CONJUNCTION
    COMPOUND COMPLEX = 2 INDEPENDENT clauses and 1 or more DEPENDENT clauses
"""

class Sentence(models.Model):
    TYPES = (
        ('NONE', 'None'),
        ('SIMPLE', 'Simple'),
        ('COMPOUND', 'Compound'),
        ('COMPLEX', 'Complex'),
        ('COMPOUND_COMPLEX', 'Compound-Complex')
    )

    sentence = models.CharField(max_length=500)
    word_type = models.CharField(choices=TYPES, default='None', max_length=20)

