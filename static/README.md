# Static assets

Drop your actual resume PDF here as `resume.pdf` so the **Download Resume** button on `/resume/` serves it. The button is wired to `{% static 'resume.pdf' %}`. If the file is missing the link will 404 until you add it.

After dropping the file in, run `python manage.py collectstatic --no-input` (or just rely on `build.sh` to run it on deploy).
