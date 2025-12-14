import random

def generate_blueprint(prompt):
    """
    Simple mock planner for hackathon MVP
    (Replace with actual Oumi API on Day 2)
    """

    return {
        "project_name": "devmind_app_" + str(random.randint(1000, 9999)),
        "description": prompt,
        "frontend": ["home", "dashboard", "settings"],
        "backend": ["GET /api/data", "POST /api/create"],
        "database": ["users", "records"],
        "stack": "Next.js + Flask"
    }
