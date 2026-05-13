from django.shortcuts import render
from projects.models import Project


def home(request):
    """Home page view with featured projects."""
    featured_projects = Project.objects.filter(is_featured=True)[:3]

    context = {
        "featured_projects": featured_projects,
    }
    return render(request, "core/index.html", context)


def about(request):
    """About page."""
    return render(request, "core/about.html", {})


def skills(request):
    """Skills page with categorized technical and leadership competencies."""
    skill_categories = [
        {
            "name": "AI & Machine Learning",
            "tagline": "Production AI workflows, LLM applications, and intelligent automation.",
            "accent": "violet",
            "skills": [
                "LangChain", "LangGraph", "OpenAI API", "Anthropic Claude",
                "Hugging Face", "RAG Pipelines", "Vector Databases",
                "scikit-learn", "PyTorch", "TensorFlow", "Prompt Engineering",
                "AI Agents",
            ],
        },
        {
            "name": "Cybersecurity",
            "tagline": "Application security, threat modeling, and secure-by-design systems.",
            "accent": "rose",
            "skills": [
                "OWASP Top 10", "Threat Modeling", "OAuth 2.0", "JWT",
                "SAST / DAST", "Penetration Testing", "Zero Trust",
                "Secrets Management", "SIEM", "Incident Response",
            ],
        },
        {
            "name": "Cloud & DevOps",
            "tagline": "Reliable, observable infrastructure and automated delivery.",
            "accent": "indigo",
            "skills": [
                "AWS", "Azure", "Docker", "Kubernetes", "Terraform",
                "GitHub Actions", "CI/CD", "Linux", "Nginx",
                "Observability", "Infrastructure as Code",
            ],
        },
        {
            "name": "Programming",
            "tagline": "Idiomatic, maintainable code across the stack.",
            "accent": "sky",
            "skills": [
                "Python", "Django", "FastAPI", "JavaScript", "TypeScript",
                "React", "Node.js", "REST APIs", "GraphQL", "SQL",
                "Tailwind CSS", "Git",
            ],
        },
        {
            "name": "Analytics",
            "tagline": "Turning raw data into decisions, dashboards, and forecasts.",
            "accent": "purple",
            "skills": [
                "PostgreSQL", "Pandas", "NumPy", "Power BI", "Tableau",
                "Looker", "ETL Pipelines", "Statistical Modeling",
                "A/B Testing", "BigQuery",
            ],
        },
        {
            "name": "Automation",
            "tagline": "Workflow orchestration that removes toil and accelerates teams.",
            "accent": "fuchsia",
            "skills": [
                "n8n", "Zapier", "Make", "Airflow", "Cron / Task Scheduling",
                "Python Scripting", "Webhooks", "Process Automation",
            ],
        },
        {
            "name": "Leadership",
            "tagline": "Cross-functional leadership, mentoring, and operational excellence.",
            "accent": "emerald",
            "skills": [
                "Team Leadership", "Mentoring", "Agile / Scrum",
                "Project Management", "Stakeholder Communication",
                "Hiring & Onboarding", "Strategic Planning",
                "Operational Excellence",
            ],
        },
    ]

    context = {"skill_categories": skill_categories}
    return render(request, "core/skills.html", context)


def resume(request):
    """Resume page with experience, certifications, and education."""
    experience = [
        {
            "role": "Senior AI Engineer",
            "company": "Confidential",
            "period": "2023 — Present",
            "location": "Remote",
            "highlights": [
                "Designed and shipped LLM-powered workflows that automate "
                "knowledge-worker tasks across operations and support.",
                "Built retrieval-augmented generation pipelines on top of "
                "vector databases, with evaluation harnesses and guardrails.",
                "Led cross-functional design reviews for AI features, "
                "balancing latency, cost, and safety constraints.",
            ],
        },
        {
            "role": "Full-Stack Engineer",
            "company": "Confidential",
            "period": "2020 — 2023",
            "location": "Hybrid",
            "highlights": [
                "Delivered production Django + React applications backed by "
                "PostgreSQL and deployed on AWS via Terraform.",
                "Hardened authentication and authorization paths using "
                "OAuth 2.0, JWT, and OWASP-aligned secure defaults.",
                "Mentored junior engineers and ran the team's code review "
                "and on-call rotation.",
            ],
        },
        {
            "role": "Software Engineer",
            "company": "Confidential",
            "period": "2017 — 2020",
            "location": "On-site",
            "highlights": [
                "Built internal automation tooling that eliminated repeated "
                "manual workflows, saving hundreds of hours per quarter.",
                "Owned data pipelines feeding analytics dashboards used by "
                "leadership for weekly business reviews.",
            ],
        },
    ]

    certifications = [
        {"name": "AWS Certified Solutions Architect", "issuer": "Amazon Web Services"},
        {"name": "Certified Kubernetes Administrator (CKA)", "issuer": "CNCF"},
        {"name": "CompTIA Security+", "issuer": "CompTIA"},
        {"name": "Certified Ethical Hacker (CEH)", "issuer": "EC-Council"},
        {"name": "Google Professional Data Engineer", "issuer": "Google Cloud"},
    ]

    education = [
        {
            "degree": "B.Sc. Computer Science",
            "school": "University",
            "period": "Graduated",
            "details": "Coursework in algorithms, distributed systems, "
                       "machine learning, and information security.",
        },
    ]

    context = {
        "experience": experience,
        "certifications": certifications,
        "education": education,
    }
    return render(request, "core/resume.html", context)
