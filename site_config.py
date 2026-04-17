# site_config.py - Central site configuration
#
# Edit this file to customize your deployment. All site generation
# scripts read from here so you only need to change values once.
#
# ------------------------------------------------------------------
# Custom domain examples
# ------------------------------------------------------------------
# For ciscoinabox.com:
#   SITE_URL    = "https://ciscoinabox.com"
#   SITE_BASEURL = ""
#
# For cisoinabox.cisocurious.com:
#   SITE_URL    = "https://cisoinabox.cisocurious.com"
#   SITE_BASEURL = ""
#
# For GitHub Pages (default):
#   SITE_URL    = "https://ciso-in-a-box.github.io"
#   SITE_BASEURL = "/ciso-in-a-box-site"
# ------------------------------------------------------------------

SITE_TITLE = "CISO-in-a-Box"
SITE_AUTHOR = "CISOinaBox Contributors"
SITE_EMAIL = "contributors@ciso-in-a-box.org"
SITE_DESCRIPTION = (
    "A comprehensive guide to cybersecurity and risk management "
    "for organizations, aspiring CISOs, and security professionals."
)

SITE_URL = "https://ciso-in-a-box.github.io"
SITE_BASEURL = "/ciso-in-a-box-site"

GITHUB_REPO_URL = "https://github.com/CroodSolutions/CISOinaBox"
GITHUB_ORG = "CroodSolutions"
GITHUB_REPO_NAME = "CISOinaBox"
GITHUB_BRANCH = "main"

# ---- Homepage layout --------------------------------------------------
# Section numbers reference SECTION_METADATA in generate_site.py.
# Slugs are resolved automatically, so renaming a section directory
# will not break links.

PATHWAY_CARDS = [
    {
        "title": "The New CISO",
        "description": (
            "Just landed the role? Start here to navigate your first "
            "90 days, build relationships, and set the strategy."
        ),
        "icon": "fas fa-flag",
        "topics": [
            "Getting Started (First 90 Days)",
            "Security Leadership Strategy",
            "Enterprise Risk Management",
        ],
        "link_section": 1,
        "color": "#289dff",
    },
    {
        "title": "The Program Builder",
        "description": (
            "Focus on architecture, engineering, and operations. "
            "Build the systems that defend the business."
        ),
        "icon": "fas fa-tools",
        "topics": [
            "Security Architecture",
            "SecOps & Incident Response",
            "Vulnerability Management",
        ],
        "link_section": 6,
        "color": "#7952b3",
    },
    {
        "title": "The Strategist",
        "description": (
            "Align security with business goals. "
            "Master GRC, compliance, insurance, and resilience."
        ),
        "icon": "fas fa-chess",
        "topics": [
            "Governance, Risk & Compliance",
            "Business Continuity (BCP)",
            "Cyber Insurance",
        ],
        "link_section": 12,
        "color": "#ffc107",
    },
]

HOMEPAGE_MODULES = [
    {"section": 5, "icon": "fas fa-shield-alt", "short_title": "CIS18 Controls", "subtitle": "Critical Framework"},
    {"section": 4, "icon": "fas fa-map-marked-alt", "short_title": "Attack Surface", "subtitle": "Know your perimeter"},
    {"section": 9, "icon": "fas fa-id-card", "short_title": "IAM Overview", "subtitle": "Identity is the perimeter"},
    {"section": 7, "icon": "fas fa-code", "short_title": "AppSec", "subtitle": "Secure Development"},
    {"section": 13, "icon": "fas fa-users", "short_title": "Security Awareness", "subtitle": "Human Firewall"},
    {"section": 19, "icon": "fas fa-book", "short_title": "Standards", "subtitle": "ISO, NIST, SOC2"},
    {"section": 3, "icon": "fas fa-user-secret", "short_title": "Threat Intel", "subtitle": "Know your adversary"},
    {"section": 22, "icon": "fas fa-box-open", "short_title": "Resources", "subtitle": "Tools & Templates"},
]

# ---- Navbar -----------------------------------------------------------
# Each item links to a section number (resolved to slug automatically),
# a special page name, or an external URL.

NAVBAR_CONFIG = [
    {
        "label": "Browse the Guide",
        "items": [
            {"label": "Start Here", "section": 1},
            {"label": "Browse All Sections", "page": "sections"},
            {"label": "Resources", "section": 22},
        ],
    },
    {
        "label": "Learning Paths",
        "items": [
            {"label": "The New CISO", "section": 1},
            {"label": "The Program Builder", "section": 6},
            {"label": "The Strategist", "section": 12},
        ],
    },
    {
        "label": "Project and Source",
        "items": [
            {"label": "Contributing", "page": "contributing"},
            {"label": "GitHub Repo", "url": "github"},
        ],
    },
]