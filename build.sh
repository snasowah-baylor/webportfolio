#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Seed fixtures only on a fresh DB.
# Once admin data exists, fixtures are NOT replayed — admin is the source of truth.
python manage.py shell -c "
from projects.models import Project
from core.models import SkillCategory, Experience
from blog.models import BlogPost
from django.core.management import call_command

if Project.objects.count() == 0:
    call_command('loaddata', 'projects/fixtures/projects.json')
else:
    print('projects table not empty — skipping projects fixture')

if SkillCategory.objects.count() == 0:
    call_command('loaddata', 'core/fixtures/skills.json')
else:
    print('skill_category table not empty — skipping skills fixture')

if Experience.objects.count() == 0:
    call_command('loaddata', 'core/fixtures/resume.json')
else:
    print('experience table not empty — skipping resume fixture')

if BlogPost.objects.count() == 0:
    call_command('loaddata', 'blog/fixtures/blog.json')
    call_command('loaddata', 'blog/fixtures/sector_articles.json')
else:
    print('blog_post table not empty — skipping blog fixtures')
"
