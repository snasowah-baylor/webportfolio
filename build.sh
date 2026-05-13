#!/usr/bin/env bash
set -o errexit
set -o pipefail

echo "===> DJANGO_SETTINGS_MODULE = ${DJANGO_SETTINGS_MODULE:-(unset, defaults to portfolio.settings)}"
echo "===> DATABASE_URL is ${DATABASE_URL:+SET}${DATABASE_URL:-NOT SET}"

echo "===> pip install"
pip install -r requirements.txt

echo "===> collectstatic"
python manage.py collectstatic --no-input

echo "===> migrate"
python manage.py migrate --no-input

echo "===> conditional seed (python heredoc; exceptions propagate)"
python << 'PYEOF'
import os, sys, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings_prod")
django.setup()

print(f"  (using DJANGO_SETTINGS_MODULE={os.environ['DJANGO_SETTINGS_MODULE']})")

from django.core.management import call_command
from projects.models import Project
from core.models import SkillCategory, Experience
from blog.models import BlogPost

def seed_if_empty(label, model, fixtures):
    n = model.objects.count()
    if n == 0:
        print(f"  [{label}] table empty — loading {fixtures}")
        for f in fixtures:
            call_command('loaddata', f, verbosity=2)
        print(f"  [{label}] now has {model.objects.count()} rows")
    else:
        print(f"  [{label}] has {n} rows — skipping fixture")

seed_if_empty("projects",       Project,         ["projects/fixtures/projects.json"])
seed_if_empty("skills",         SkillCategory,   ["core/fixtures/skills.json"])
seed_if_empty("resume",         Experience,      ["core/fixtures/resume.json"])
seed_if_empty("blog",           BlogPost,        ["blog/fixtures/blog.json", "blog/fixtures/sector_articles.json"])

print("===> final counts")
print(f"  projects: {Project.objects.count()}")
print(f"  skill_categories: {SkillCategory.objects.count()}")
print(f"  experiences: {Experience.objects.count()}")
print(f"  blog_posts: {BlogPost.objects.count()}")
sys.exit(0)
PYEOF

echo "===> build complete"
