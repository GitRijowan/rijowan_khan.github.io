from flask import Flask, render_template, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

# Complete data structure matching your CV
PERSONAL_DATA = {
    "name": "MD RIJOWAN KHAN",
    "title": "DevOps Engineer",
    "tagline": "Building Scalable Systems with AI & Cloud",
    "email": "rijowan@qq.com",
    "phone": "+86 13141473271",
    "location": "Beijing, China",
    "github": "https://github.com/GitRijowan",
    "linkedin": "https://www.linkedin.com/in/rijowan-khan-57720a231/",
    "website": "https://rijowankhan.com",
    "current_year": datetime.now().year,

    "education": {
        "degree": "BSC - Computer Science and Technology",
        "university": "China University of Petroleum Beijing",
        "duration": "Sept 2022 – Jul 2026",
        "gpa": "84%",
            },

    "experience": [
        {
            "title": "Junior DevOps Engineer",
            "company": "SonetCraft (LLC), USA",
            "type": "Remote",
            "duration": "2025.09 - present",
            "icon": "server",
            "responsibilities": [
                "Assisting senior engineers with deployments, cloud resource management, and operational tasks",
                "Managing containerized environments (Docker) and ensuring stable development setups",
                "Researching model pricing, performance, and API options for client decisions",
                "Handling project management tasks"
            ]
        },
        {
            "title": "DevOps Intern",
            "company": "SonetCraft (LLC), USA",
            "type": "Remote",
            "duration": "2022.06 - 2022.09",
            "icon": "code",
            "responsibilities": [
                "Learned basic DevOps operations under senior engineer guidance",
                "Assisted with environment setup and cloud-related activities",
                "Researched model pricing and API options"
            ]
        },
        {
            "title": "Computer Lab Assistant",
            "company": "America Bangladesh University, Bangladesh",
            "type": "On-site",
            "duration": "2020.07 - 2022.07",
            "icon": "laptop-code",
            "responsibilities": [
                "Assisted faculty and students in laboratory sessions",
                "Arranged required software and maintained lab systems",
                "Supported academic workshops and technical sessions"
            ]
        }
    ],

    "publications": [
        {
            "title": "Architectural Trade-offs in Transformer Models: A Controlled Grid Search and Complexity Analysis",
            "authors": "M. N. Hossain, M. R. Khan, M. Rahman, and I. A. H. Prianka",
            "conference": "IEEE 7th International Conference on Computing, Communication and Automation",
            "year": "2025",
            "status": "Accepted",
            "link": "#"
        },
        {
            "title": "AI-Driven Dynamic Power-Aware Adaptive Scheduling for Cloud Computing",
            "authors": "M. R. Khan",
            "conference": "In Processing",
            "year": "2025",
            "status": "pending",
            "link": "#"
        }
    ],

    "projects": [
        {
            "title": "Credit Card Fraud Detection with Explainable AI",
            "description": "Interactive Streamlit app for real-time fraud detection using Random Forest classifier with SHAP-based explanations, secure CSV uploads, and automated reporting.",
            "tools": ["Python", "Streamlit", "SHAP", "Scikit-learn", "Pandas"],
            "github": "https://github.com/GitRijowan",
            "demo": "#",
            "category": "AI/ML",
            "image": "project1.jpg"
        },
        {
            "title": "Decentralized Voice Authentication System with Blockchain",
            "description": "Blockchain-based voice authentication system combining voice biometrics with Polygon smart contracts. Real-time transaction monitoring and responsive web interface.",
            "tools": ["Solidity", "JavaScript", "MetaMask", "Web3.js", "React"],
            "github": "https://github.com/GitRijowan",
            "demo": "#",
            "category": "Blockchain",
            "image": "project2.jpg"
        },
        {
            "title": "Domain Availability Checker",
            "description": "Fast domain availability checker supporting hundreds of TLDs with RDAP, Redis caching, async lookups, and dynamic IANA updates.",
            "tools": ["Python", "Flask", "Bootstrap", "Redis", "AsyncIO"],
            "github": "https://github.com/GitRijowan",
            "demo": "#",
            "category": "Web Dev",
            "image": "project3.jpg"
        }
    ],

    "skills": {
        "Programming": [
            {"name": "Python", "level":85, "icon": "python"},
            {"name": "SQL", "level": 75, "icon": "database"},
            {"name": "Solidity", "level": 45, "icon": "ethereum"},
        ],
        "DevOps & Cloud": [
            {"name": "Docker", "level": 80, "icon": "docker"},
            {"name": "Cloud Management", "level": 50, "icon": "cloud"},
            {"name": "Git", "level": 55, "icon": "git-alt"}
        ],
        "AI & Data Science": [
            {"name": "Explainable AI", "level": 75, "icon": "eye"}
        ],
        "Professional Skills": [
            {"name": "Research & Writing", "level": 85, "icon": "file-alt"},
            {"name": "Team Coordination", "level": 90, "icon": "users"},
            {"name": "Event Management", "level": 95, "icon": "calendar-alt"}
        ]
    },

    "languages": [
        {"name": "English", "level": "C1", "percentage": 90, "icon": "globe-americas"},
        {"name": "Bangla", "level": "Native", "percentage": 100, "icon": "flag"},
        {"name": "Chinese", "level": "B2", "percentage": 70, "icon": "language"},
        {"name": "Hindi & Urdu", "level": "B2", "percentage": 70, "icon": "comments"}
    ],

    "achievements": [
        {"title": "University Scholarship Type-B",
         "description": "China University of Petroleum (Beijing) 2022 – Present", "icon": "award"},
        {"title": "Champion, BCSS Essay Writing Competition", "description": "2019", "icon": "trophy"},
        {"title": "Champion, Inter-School Chess Tournament", "description": "2018", "icon": "chess"},
        {"title": "Top 3 Team, Cultural Festival Dance", "description": "China University of Petroleum (Beijing) 2023",
         "icon": "music"}
    ],

    "certifications": [
        {"name": "DevOps for Beginners: Docker, K8s, Cloud, CI/CD", "issuer": "UDEMY", "date": "Ongoing",
         "icon": "certificate"},
        {"name": "Basic Safety of University Laboratories", "issuer": "China University of Petroleum, Beijing",
         "date": "30 Oct 2024", "icon": "flask"},
        {"name": "International Cooperative Education", "issuer": "Harbin Engineering University", "date": "Jan 2023",
         "icon": "university"},
        {"name": "Chinese Language and Literature", "issuer": "Hunan University", "date": "Dec 2022", "icon": "book"}
    ],

    "extracurricular": [
        {"role": "Co-Founder", "organization": "Chalkaladathkha Youth Community", "duration": "Mar 2017",
         "icon": "users"},
        {"role": "Vice Captain", "organization": "Bengal Bangers Football Club, Beijing",
         "duration": "Nov 2024 – Present", "icon": "futbol"}
    ],

    "interests": ["Football", "Hiking", "History", "Language Learning", "Chess"]
}


@app.route('/')
def index():
    return render_template('index.html', data=PERSONAL_DATA)


@app.route('/api/visit-count')
def visit_count():
    # In production, use database
    return jsonify({"count": random.randint(1000, 5000)})


@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.json
        # Here you would save to database or send email
        print(f"Message from {data.get('name')}: {data.get('message')}")
        return jsonify({
            "success": True,
            "message": "Message received successfully! I'll get back to you soon."
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error: {str(e)}"
        }), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)