from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "simple-demo-key"

# Small sample recommendation list
items = [
    {"title": "Python Basics", "category": "Practical", "level": "Beginner",
     "tags": ["python", "programming", "coding"], "description": "Learn Python with simple exercises."},
    {"title": "Introduction to Artificial Intelligence", "category": "Theoretical", "level": "Beginner",
     "tags": ["ai", "artificial intelligence", "technology"], "description": "Understand basic AI concepts."},
    {"title": "Machine Learning with Python", "category": "Practical", "level": "Intermediate",
     "tags": ["ai", "machine learning", "python"], "description": "Build basic machine learning models."},
    {"title": "Java Programming", "category": "Practical", "level": "Beginner",
     "tags": ["java", "programming", "coding"], "description": "Learn Java programming fundamentals."},
    {"title": "Data Structures and Algorithms", "category": "Both", "level": "Intermediate",
     "tags": ["programming", "coding", "problem solving"], "description": "Improve logical and coding skills."},
    {"title": "Deep Learning", "category": "Theoretical", "level": "Advanced",
     "tags": ["ai", "deep learning", "machine learning"], "description": "Study neural networks and deep learning."},
    {"title": "Web Development", "category": "Practical", "level": "Beginner",
     "tags": ["html", "css", "javascript", "web"], "description": "Create simple websites."},
    {"title": "Advanced Python Projects", "category": "Practical", "level": "Advanced",
     "tags": ["python", "projects", "programming"], "description": "Practice Python through larger projects."}
]

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []
    message = ""

    if request.method == "POST":
        background = request.form.get("background", "")
        interests = request.form.get("interests", "")
        skill = request.form.get("skill", "Beginner")
        category = request.form.get("category", "Both")
        goal = request.form.get("goal", "")
        preferences = request.form.get("preferences", "")
        count = 5

        # Combine interests and goals to identify the user's learning direction.
        words = (interests + " " + goal + " " + preferences).lower()
        interest_words = [word.strip() for word in words.replace(",", " ").split()]

        ranked = []
        for item in items:
            score = 0

            for tag in item["tags"]:
                if tag in interest_words or tag in words:
                    score += 3

            if item["level"] == skill:
                score += 2
            elif skill == "Intermediate" and item["level"] == "Beginner":
                score += 1

            if category == "Both" or item["category"] == category or item["category"] == "Both":
                score += 2

            reason = "Matches your interests and learning preferences."
            if item["level"] == skill:
                reason += " It matches your selected skill level."
            if category == "Both" or item["category"] == category:
                reason += " It matches your preferred category."

            ranked.append((score, item, reason))

        ranked.sort(key=lambda x: x[0], reverse=True)
        recommendations = [
            {"title": item["title"], "description": item["description"], "reason": reason}
            for score, item, reason in ranked[:count]
        ]

        if not recommendations:
            message = "No recommendations found."

        session["last_interests"] = interests

    return render_template("index.html", recommendations=recommendations, message=message)


@app.route("/feedback", methods=["POST"])
def feedback():
    old_interests = session.get("last_interests", "")
    feedback_text = request.form.get("feedback", "")
    session["last_interests"] = old_interests + " " + feedback_text
    return render_template(
        "index.html",
        recommendations=[],
        message="Feedback added to your interests. Submit the form again to refresh recommendations."
    )


if __name__ == "__main__":
    app.run(debug=True)
