#!/usr/bin/env python3

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, unquote, urlparse

from site_config import (
    GITHUB_BRANCH,
    GITHUB_ORG,
    GITHUB_REPO_NAME,
    GITHUB_REPO_URL,
    HOMEPAGE_MODULES,
    NAVBAR_CONFIG,
    PATHWAY_CARDS,
    SITE_AUTHOR,
    SITE_BASEURL,
    SITE_DESCRIPTION,
    SITE_EMAIL,
    SITE_TITLE,
    SITE_URL,
)

ROOT = Path(__file__).resolve().parent
SITE_ROOT = ROOT / "ciso-in-a-box-site"
DOCS_ROOT = SITE_ROOT / "docs"
ASSETS_ROOT = SITE_ROOT / "assets" / "content"
SECTION_DIR_RE = re.compile(r"^(\d+)\s*-\s*(.+)$")
README_NAMES = {"readme.md"}
REPO_PREFIXES = (
    f"{GITHUB_REPO_URL}/blob/{GITHUB_BRANCH}/",
    f"{GITHUB_REPO_URL}/tree/{GITHUB_BRANCH}/",
)


@dataclass(frozen=True)
class SectionMeta:
    number: int
    source_title: str
    page_title: str
    slug: str
    nav_category: str
    browse_summary: str


@dataclass
class Page:
    source_path: Path
    title: str
    permalink: str
    output_path: Path
    description: str
    section_meta: SectionMeta | None = None
    is_section_home: bool = False
    related_pages: list["Page"] = field(default_factory=list)
    previous_page: "Page | None" = None
    next_page: "Page | None" = None


SECTION_METADATA = {
    1: SectionMeta(
        1,
        "Getting Started",
        "Getting Started",
        "getting-started",
        "Guide",
        "Practical first steps for improving security and building momentum.",
    ),
    2: SectionMeta(
        2,
        "Understanding Business Risk",
        "Understanding Enterprise Risk Management (ERM) for CISOs",
        "understanding-enterprise-risk-management-erm-for-cisos",
        "Risk & Threat Management",
        "How to translate cyber issues into business risk, impact, and decision-making.",
    ),
    3: SectionMeta(
        3,
        "Understanding the Adversary",
        "Cyber Attacks and Defense: Threat Intelligence, Adversaries, and Collective Defense",
        "cyber-attacks-and-defense-threat-intelligence-adversaries-and-collective-defense",
        "Risk & Threat Management",
        "Who attacks organizations, how they operate, and how defenders can respond.",
    ),
    4: SectionMeta(
        4,
        "Mapping Attack Surface",
        "Mapping Your Attack Surface",
        "mapping-your-attack-surface",
        "Risk & Threat Management",
        "How to identify exposed systems, services, identities, and external dependencies.",
    ),
    5: SectionMeta(
        5,
        "CIS18 and Basic Security Controls",
        "Overview of CIS18 Critical Security Controls",
        "overview-of-cis18-critical-security-controls",
        "Security Controls",
        "A structured walkthrough of CIS18 and the controls that reduce common risk.",
    ),
    6: SectionMeta(
        6,
        "Security Architecture and Engineering",
        "Security Architecture and Engineering",
        "security-architecture-and-engineering",
        "Security Controls",
        "Design principles and engineering patterns for resilient, defensible systems.",
    ),
    7: SectionMeta(
        7,
        "Product and Software Security",
        "Product and Software Security",
        "product-and-software-security",
        "Security Controls",
        "How to evaluate, build, and secure software and technology products safely.",
    ),
    8: SectionMeta(
        8,
        "Secure Business Process Design",
        "Secure Business Process Optimization",
        "secure-business-process-optimization",
        "Security Controls",
        "Ways to improve business processes without introducing avoidable security gaps.",
    ),
    9: SectionMeta(
        9,
        "Identity and Access Management",
        "Identity and Access Management (IAM) Overview",
        "identity-and-access-management-iam-overview",
        "Security Program",
        "Foundations of IAM, access control, lifecycle management, and privileged access.",
    ),
    10: SectionMeta(
        10,
        "Security Management",
        "CISO Security Management Strategy Guide",
        "ciso-security-management-strategy-guide",
        "Security Program",
        "Operating the security function through roles, planning, governance, and execution.",
    ),
    11: SectionMeta(
        11,
        "Security Leadership",
        "Security Leadership Strategy Guide for CISOs",
        "security-leadership-strategy-guide-for-cisos",
        "Security Program",
        "Leadership approaches for setting direction, influencing stakeholders, and scaling impact.",
    ),
    12: SectionMeta(
        12,
        "Governance Risk and Compliance",
        "Governance, Risk & Compliance (GRC) Strategy Guide for Cybersecurity Programs",
        "governance-risk-compliance-grc-strategy-guide-for-cybersecurity-programs",
        "Compliance & Resilience",
        "Core governance, risk, and compliance practices for building accountable programs.",
    ),
    13: SectionMeta(
        13,
        "Security Awareness",
        "Security Awareness: Building a Human Firewall",
        "security-awareness-building-a-human-firewall",
        "Security Program",
        "How to build user awareness programs that reduce phishing, fraud, and human error.",
    ),
    14: SectionMeta(
        14,
        "Security Operations - SOC",
        "Cybersecurity Operations (SecOps) Program Maturity Guide",
        "cybersecurity-operations-secops-program-maturity-guide",
        "Security Program",
        "Monitoring, detection, triage, and operational practices for effective SecOps teams.",
    ),
    15: SectionMeta(
        15,
        "Response - IR",
        "Cyber Incident Response Strategy Guide for CISOs",
        "cyber-incident-response-strategy-guide-for-cisos",
        "Security Program",
        "How to prepare for, manage, and learn from cybersecurity incidents effectively.",
    ),
    16: SectionMeta(
        16,
        "Business Continuity Planning - BCP",
        "Business Continuity Planning - BCP",
        "business-continuity-planning---bcp",
        "Compliance & Resilience",
        "Planning to keep critical business services operating during disruptive events.",
    ),
    17: SectionMeta(
        17,
        "Disaster Recovery - DR",
        "Disaster Recovery - DR",
        "disaster-recovery---dr",
        "Compliance & Resilience",
        "Recovery strategies for restoring technology, data, and operations after major outages.",
    ),
    18: SectionMeta(
        18,
        "Vulnerability Management and Risk",
        "Vulnerability Management and Risk",
        "vulnerability-management-and-risk",
        "Compliance & Resilience",
        "Methods for identifying, prioritizing, and reducing vulnerability-driven risk.",
    ),
    19: SectionMeta(
        19,
        "Frameworks and Standards",
        "Frameworks and Standards",
        "frameworks-and-standards",
        "Compliance & Resilience",
        "A practical guide to common security frameworks, standards, and control mappings.",
    ),
    20: SectionMeta(
        20,
        "Careers - The Road to CISO",
        "Cybersecurity and IT Career Pathways",
        "cybersecurity-and-it-career-pathways",
        "Security Program",
        "Career paths, skill development, and progression toward security leadership roles.",
    ),
    21: SectionMeta(
        21,
        "Cyber Insurance",
        "Cyber Insurance",
        "cyber-insurance",
        "Compliance & Resilience",
        "How cyber insurance works and how to evaluate coverage, readiness, and tradeoffs.",
    ),
    22: SectionMeta(
        22,
        "Resources",
        "Resources",
        "resources",
        "Guide",
        "Reference links, tools, templates, and supporting material across the guide.",
    ),
}


def slugify(value: str) -> str:
    value = unquote(value).strip().lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "page"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def strip_markdown(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_>#]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return strip_markdown(stripped.lstrip("#").strip())
    return None


def remove_first_h1(text: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.strip().startswith("# "):
            del lines[index]
            if index < len(lines) and not lines[index].strip():
                del lines[index]
            break
    return "\n".join(lines).strip() + "\n"


def repair_table_rows(text: str) -> str:
    lines = text.split("\n")
    table_active = False
    pipe_count = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("|"):
            table_active = False
            continue
        if re.match(r"^\|[\s\-:|]+\|?$", stripped):
            continue
        parts = [p.strip() for p in stripped.split("|") if p.strip() != ""]
        if not table_active:
            table_active = True
            pipe_count = stripped.count("|") - (1 if stripped.endswith("|") else 0)
        if pipe_count > 0 and not stripped.endswith("|"):
            lines[i] = line + " |"
    result = "\n".join(lines)
    result = re.sub(r"(?<!\n)(#{1,6}\s[^\n]+)\n(\|)", r"\1\n\n\2", result)
    result = re.sub(r"\n(#{1,6}\s[^\n]+)\n(\|)", r"\n\1\n\n\2", result)
    return result


def strip_excluded_sections(text: str) -> str:
    patterns = [
        r"\n## Updating the Wiki\n.*$",
    ]
    for pattern in patterns:
        text = re.sub(pattern, "\n", text, flags=re.DOTALL)
    return text.strip() + "\n"


def summary_from_text(text: str) -> str:
    cleaned = strip_excluded_sections(remove_first_h1(text))
    paragraphs = [
        part.strip() for part in re.split(r"\n\s*\n", cleaned) if part.strip()
    ]
    for paragraph in paragraphs:
        first = paragraph.splitlines()[0].strip()
        if first.startswith(("#", "-", "*", "|", "```")):
            continue
        summary = strip_markdown(paragraph)
        if summary:
            return summary[:220].rstrip()
    return "Guidance and reference material from the CISO-in-a-Box repository."


def section_directories() -> list[tuple[SectionMeta, Path]]:
    results: list[tuple[SectionMeta, Path]] = []
    for path in ROOT.iterdir():
        if not path.is_dir() or path.name == SITE_ROOT.name:
            continue
        match = SECTION_DIR_RE.match(path.name)
        if not match:
            continue
        number = int(match.group(1))
        meta = SECTION_METADATA.get(number)
        if meta:
            results.append((meta, path))
    return sorted(results, key=lambda item: item[0].number)


def find_section_readme(section_dir: Path) -> Path:
    for child in section_dir.iterdir():
        if child.is_file() and child.name.lower() in README_NAMES:
            return child
    raise FileNotFoundError(f"No section README found in {section_dir}")


def find_markdown_files(section_dir: Path) -> list[Path]:
    return sorted(
        [path for path in section_dir.rglob("*.md") if path.is_file()],
        key=lambda path: (
            len(path.relative_to(section_dir).parts),
            path.as_posix().lower(),
        ),
    )


def relative_asset_url(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return jekyll_relative_url("/assets/content/" + "/".join(quote(part) for part in rel.parts))


def jekyll_relative_url(path: str) -> str:
    if not path.startswith("/"):
        path = "/" + path
    return "{{ '" + path + "' | relative_url }}"


def jekyll_permalink(path: str, fragment: str | None = None) -> str:
    url = jekyll_relative_url(path)
    if fragment:
        return f"{url}#{fragment}"
    return url


def title_from_file(path: Path, fallback: str) -> str:
    heading = first_heading(read_text(path))
    return heading or fallback


def build_pages() -> tuple[list[Page], list[Page]]:
    pages: list[Page] = []
    section_pages: list[Page] = []

    for meta, section_dir in section_directories():
        readme = find_section_readme(section_dir)
        section_page = Page(
            source_path=readme,
            title=meta.page_title,
            permalink=f"/{meta.slug}/",
            output_path=DOCS_ROOT / f"{meta.slug}.markdown",
            description=meta.browse_summary,
            section_meta=meta,
            is_section_home=True,
        )
        pages.append(section_page)
        section_pages.append(section_page)

        related: list[Page] = []
        for source_path in find_markdown_files(section_dir):
            if source_path == readme:
                continue
            rel = source_path.relative_to(section_dir)
            relative_parts = rel.with_suffix("").parts
            if rel.name.lower() in README_NAMES and len(relative_parts) > 1:
                slug_parts = [slugify(part) for part in relative_parts[:-1]]
            else:
                slug_parts = [slugify(part) for part in relative_parts]
            fallback = rel.stem.replace("-", " ").replace("_", " ").strip().title()
            page = Page(
                source_path=source_path,
                title=title_from_file(source_path, fallback),
                permalink="/" + "/".join([meta.slug, *slug_parts]) + "/",
                output_path=DOCS_ROOT.joinpath(*([meta.slug, *slug_parts[:-1]]))
                / f"{slug_parts[-1]}.markdown",
                description=summary_from_text(read_text(source_path)),
                section_meta=meta,
            )
            pages.append(page)
            related.append(page)

        section_page.related_pages = sorted(
            related, key=lambda page: page.title.lower()
        )

    for index, page in enumerate(section_pages):
        if index > 0:
            page.previous_page = section_pages[index - 1]
        if index < len(section_pages) - 1:
            page.next_page = section_pages[index + 1]

    contributing = ROOT / "CONTRIBUTING.md"
    if contributing.exists():
        pages.append(
            Page(
                source_path=contributing,
                title="Contributing",
                permalink="/contributing/",
                output_path=SITE_ROOT / "contributing.markdown",
                description=summary_from_text(read_text(contributing)),
            )
        )

    return pages, section_pages


def build_lookup(pages: list[Page]) -> dict[Path, str]:
    return {page.source_path.resolve(): page.permalink for page in pages}


def resolve_local_target(
    raw_url: str, base_file: Path
) -> tuple[Path | None, str | None]:
    if raw_url.startswith(("mailto:", "tel:")):
        return None, None

    split = raw_url.split("#", 1)
    url_without_fragment = split[0]
    fragment = split[1] if len(split) == 2 else None
    decoded = unquote(url_without_fragment)

    for prefix in REPO_PREFIXES:
        if decoded.startswith(prefix):
            rel = decoded.removeprefix(prefix)
            target = ROOT / rel
            return target.resolve() if target.exists() else None, fragment

    parsed = urlparse(decoded)
    if parsed.scheme or parsed.netloc:
        return None, None

    if not decoded:
        return None, fragment

    if decoded.startswith("/"):
        target = ROOT / decoded.lstrip("/")
    else:
        target = (base_file.parent / decoded).resolve()

    if target.exists():
        return target, fragment

    return None, fragment


def rewrite_links(
    text: str, source_path: Path, permalink_lookup: dict[Path, str]
) -> str:
    pattern = re.compile(r"(!?\[[^\]]*\]\()([^()]+)(\))")

    def replace(match: re.Match[str]) -> str:
        prefix, raw_url, suffix = match.groups()
        if raw_url.startswith("#"):
            return match.group(0)

        target, fragment = resolve_local_target(raw_url, source_path)
        if target is None:
            return match.group(0)

        target = target.resolve()
        if target.is_dir():
            for child in target.iterdir():
                if child.is_file() and child.name.lower() in README_NAMES:
                    target = child.resolve()
                    break

        if target in permalink_lookup:
            url = jekyll_permalink(permalink_lookup[target])
        elif target.is_file() and target.suffix.lower() != ".md":
            url = relative_asset_url(target)
        else:
            return match.group(0)

        if fragment:
            url = f"{url}#{fragment}"
        return f"{prefix}{url}{suffix}"

    return pattern.sub(replace, text)


def autolink_plain_urls(text: str) -> str:
    url_pattern = re.compile(r'(?<!\]\()(?<!")(?P<url>https?://[^\s<]+)')

    def replace(match: re.Match[str]) -> str:
        url = match.group("url")
        trimmed = url.rstrip(".,;:!?)]")
        suffix = url[len(trimmed) :]
        return f"<{trimmed}>{suffix}"

    return url_pattern.sub(replace, text)


def yaml_quote(value: str) -> str:
    return "'" + value.replace("\\", "").replace("'", "''") + "'"


def front_matter(page: Page) -> str:
    lines = [
        "---",
        "layout: page",
        f"title: {yaml_quote(page.title)}",
        f"permalink: {page.permalink}",
        f"share-description: {yaml_quote(page.description)}",
    ]
    if page.section_meta:
        lines.append(f"nav_category: {yaml_quote(page.section_meta.nav_category)}")
        lines.append(f"section_number: {page.section_meta.number}")
    lines.append("---\n")
    return "\n".join(lines)


def build_related_links(page: Page) -> str:
    if not page.related_pages:
        return ""
    lines = ["## Additional Pages in This Section", ""]
    for related in page.related_pages:
        lines.append(f"- [{related.title}]({jekyll_permalink(related.permalink)})")
    return "\n".join(lines) + "\n"


def build_section_pager(page: Page) -> str:
    lines: list[str] = []
    if page.previous_page:
        prev = page.previous_page
        lines.extend(
            [
                "",
                f"Previous: [{prev.section_meta.source_title}]({jekyll_permalink(prev.permalink)})",
            ]
        )
    if page.next_page:
        nxt = page.next_page
        lines.extend(
            [
                "",
                f"Next: [{nxt.section_meta.source_title}]({jekyll_permalink(nxt.permalink)})",
            ]
        )
    return "\n".join(lines) + ("\n" if lines else "")


def build_child_intro(page: Page) -> str:
    assert page.section_meta is not None
    return f"[Back to {page.section_meta.source_title}]({jekyll_permalink(page.section_meta.slug)})\n\n"


def copy_assets() -> None:
    if ASSETS_ROOT.exists():
        shutil.rmtree(ASSETS_ROOT)
    ASSETS_ROOT.mkdir(parents=True, exist_ok=True)

    for _, section_dir in section_directories():
        for path in section_dir.rglob("*"):
            if not path.is_file() or path.suffix.lower() == ".md":
                continue
            destination = ASSETS_ROOT / path.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination)


def sections_cards(section_pages: list[Page]) -> str:
    category_order = [
        "Guide",
        "Risk & Threat Management",
        "Security Controls",
        "Security Program",
        "Compliance & Resilience",
    ]
    grouped: dict[str, list[Page]] = {category: [] for category in category_order}
    for page in section_pages:
        grouped.setdefault(page.section_meta.nav_category, []).append(page)

    blocks: list[str] = []
    for category in category_order:
        pages = grouped.get(category, [])
        if not pages:
            continue
        blocks.extend([f"## {category}", "", '<div class="section-browser-grid">'])
        for page in pages:
            count = len(page.related_pages)
            count_text = (
                f"{count} additional page{'s' if count != 1 else ''}"
                if count
                else "Section overview"
            )
            blocks.extend(
                [
                    '<a class="section-browser-card" href="%s">'
                    % jekyll_permalink(page.permalink),
                    '  <div class="section-browser-number">%s</div>'
                    % page.section_meta.number,
                    '  <div class="section-browser-body">',
                    "    <h3>%s</h3>" % page.section_meta.source_title,
                    "    <p>%s</p>" % page.section_meta.browse_summary,
                    "    <span>%s</span>" % count_text,
                    "  </div>",
                    "</a>",
                ]
            )
        blocks.extend(["</div>", ""])
    return "\n".join(blocks).strip() + "\n"


def sections_page_content(section_pages: list[Page]) -> str:
    return "\n".join(
        [
            sections_cards(section_pages).strip(),
            "",
        ]
    )


def write_sections_page(section_pages: list[Page]) -> None:
    content = "\n".join(
        [
            "---",
            "layout: page",
            "title: 'Browse All Sections'",
            "permalink: /sections/",
            "share-description: 'Browse all sections of the CISO-in-a-Box content library, organized by category.'",
            "---",
            "",
            sections_page_content(section_pages).strip(),
            "",
        ]
    )
    write_text(SITE_ROOT / "sections.markdown", content)


def write_contributing_page(page: Page, lookup: dict[Path, str]) -> None:
    body = repair_table_rows(
        autolink_plain_urls(
            rewrite_links(
                strip_excluded_sections(remove_first_h1(read_text(page.source_path))),
                page.source_path,
                lookup,
            )
        )
    )
    write_text(page.output_path, front_matter(page) + body)


def _build_navbar_yaml() -> str:
    lines: list[str] = []
    for group in NAVBAR_CONFIG:
        lines.append(f'  "{group["label"]}":')
        for item in group["items"]:
            label = item["label"]
            if "url" in item and item["url"] == "github":
                lines.append(f'    - "{label}": "{GITHUB_REPO_URL}"')
            elif "page" in item:
                lines.append(f'    - "{label}": "/{item["page"]}/"')
            elif "section" in item:
                meta = SECTION_METADATA.get(item["section"])
                slug = meta.slug if meta else item.get("fallback_slug", "")
                lines.append(f'    - "{label}": "/{slug}/"')
    return "\n".join(lines)


def write_config() -> None:
    navbar = _build_navbar_yaml()
    lines = [
        "###########################################################",
        "### CISOinaBox Jekyll Configuration",
        "",
        f"title: {SITE_TITLE}",
        f"author: {SITE_AUTHOR}",
        f"email: {SITE_EMAIL}",
        "description: >-",
        f"  {SITE_DESCRIPTION}",
        f'baseurl: "{SITE_BASEURL}"',
        f'url: "{SITE_URL}"',
        "",
        "navbar-links:",
        navbar,
        "",
        "remote_theme: daattali/beautiful-jekyll@6.0.1",
        "plugins:",
        "  - jekyll-remote-theme",
        "  - jekyll-include-cache",
        "  - jekyll-feed",
        "  - jekyll-sitemap",
        "  - jekyll-seo-tag",
        "",
        "site-css:",
        '  - "/assets/css/custom.css"',
        "",
        'timezone: "America/Phoenix"',
        "highlighter: rouge",
        "markdown: kramdown",
        "",
        'navbar-col: "#0e0e0e"',
        'navbar-text-col: "#FFFFFF"',
        'navbar-border-col: "#0e0e0e"',
        'page-col: "#FFFFFF"',
        'text-col: "#0e0e0e"',
        'link-col: "#289dff"',
        'hover-col: "#289dff"',
        'footer-col: "#0e0e0e"',
        'footer-text-col: "#FFFFFF"',
        'footer-link-col: "#289dff"',
        'footer-hover-col: "#289dff"',
        "",
        "social-network-links:",
        f"  github: {GITHUB_ORG}",
        "",
        'site-logo: "/assets/img/avatar-icon.png"',
    ]
    write_text(SITE_ROOT / "_config.yml", "\n".join(lines) + "\n")


def write_index_page() -> None:
    def perm(slug: str) -> str:
        return "{{ '" + f"/{slug}/" + "' | relative_url }}"

    def section_perm(number: int) -> str:
        meta = SECTION_METADATA.get(number)
        return perm(meta.slug) if meta else "/"

    start_url = section_perm(1)
    sections_url = perm("sections")

    pathways_html: list[str] = []
    for card in PATHWAY_CARDS:
        link_url = section_perm(card["link_section"])
        topics_html = "\n".join(f"      <li>{t}</li>" for t in card["topics"])
        color = card["color"]
        border_style = f' style="border-top-color: {color};"' if color != "#289dff" else ""
        icon_color_style = f' style="color: {color};"' if color != "#289dff" else ""
        btn_style = f' style="color: {color}; border-color: {color};"' if color != "#289dff" else ""
        pathways_html.extend(
            [
                f'  <div class="pathway-card"{border_style}>',
                f'    <div class="pathway-icon"{icon_color_style}>',
                f'      <i class="{card["icon"]}"></i>',
                "    </div>",
                f'    <div class="pathway-title">{card["title"]}</div>',
                f'    <div class="pathway-desc">',
                f'      {card["description"]}',
                "    </div>",
                '    <ul class="topic-list">',
                topics_html,
                "    </ul>",
                f'    <a href="{link_url}" class="pathway-btn"{btn_style}>',
                f'      {card["title"].split()[0]} &rarr;</a>',
                "  </div>",
            ]
        )

    modules_html: list[str] = []
    for mod in HOMEPAGE_MODULES:
        mod_url = section_perm(mod["section"])
        modules_html.extend(
            [
                f'  <a href="{mod_url}" class="module-card">',
                f'    <div class="module-icon"><i class="{mod["icon"]}"></i></div>',
                "    <div class=\"module-info\">",
                f'      <h4>{mod["short_title"]}</h4>',
                f'      <span>{mod["subtitle"]}</span>',
                "    </div>",
                "  </a>",
            ]
        )

    content = "\n".join(
        [
            "---",
            "layout: home",
            'title: "CISO-in-a-Box"',
            'subtitle: "Your Complete Cybersecurity Guide"',
            "permalink: /",
            "head-extra: ",
            "  - custom.html",
            "---",
            "",
            '<div class="hero-section">',
            '  <h1 class="hero-title">The Open Source CISO Guide \U0001f6e1\ufe0f</h1>',
            '  <p class="hero-subtitle">',
            '    From "Day 1" to program maturity. A community-driven framework for building, managing, and scaling modern cybersecurity programs.',
            "  </p>",
            '  <div style="margin-top: 30px;">',
            f'    <a href="{start_url}" class="btn btn-primary btn-lg" style="border-radius: 50px; padding: 12px 30px;">Start the Journey</a>',
            f'    <a href="{sections_url}" class="btn btn-outline-primary btn-lg" style="border-radius: 50px; padding: 12px 30px; margin-left: 10px;">',
            "      Browse Sections",
            "    </a>",
            f'    <a href="{GITHUB_REPO_URL}" class="btn btn-outline-dark btn-lg" style="border-radius: 50px; padding: 12px 30px; margin-left: 10px;">',
            '      <i class="fab fa-github"></i> View Source',
            "    </a>",
            "  </div>",
            "</div>",
            "",
            '<div class="section-header">',
            '  <h2 class="section-title">Choose Your Path</h2>',
            '  <p class="section-desc">Tailored guides depending on where you are in your journey.</p>',
            "</div>",
            "",
            '<div class="pathways-grid">',
            "\n".join(pathways_html),
            "</div>",
            "",
            '<div class="section-header">',
            '  <h2 class="section-title">Core Knowledge Modules</h2>',
            '  <p class="section-desc">Comprehensive guides covering every domain of information security.</p>',
            "</div>",
            "",
            '<div class="modules-grid">',
            "\n".join(modules_html),
            "</div>",
            "",
            '<div class="community-section">',
            "  <h3>Built by the Community, For the Community \U0001f91d</h3>",
            "  <p>",
            "    This project is open source. We believe in sharing knowledge to make the digital world safer.",
            "    <br>Whether you're an expert or just starting, your contribution matters.",
            "  </p>",
            f'  <a href="{GITHUB_REPO_URL}/blob/{GITHUB_BRANCH}/CONTRIBUTING.md" class="community-btn">',
            '    <i class="fas fa-code-branch"></i> Contribute Now',
            "  </a>",
            "</div>",
        ]
    )
    write_text(SITE_ROOT / "index.markdown", content + "\n")


def generate() -> None:
    pages, section_pages = build_pages()
    lookup = build_lookup(pages)

    if DOCS_ROOT.exists():
        shutil.rmtree(DOCS_ROOT)
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)

    copy_assets()
    write_config()
    write_sections_page(section_pages)
    write_index_page()

    for page in pages:
        if page.permalink == "/contributing/":
            write_contributing_page(page, lookup)
            continue

        raw_text = read_text(page.source_path)
        body = (
            repair_table_rows(
                autolink_plain_urls(
                    rewrite_links(
                        strip_excluded_sections(remove_first_h1(raw_text)),
                        page.source_path,
                        lookup,
                    )
                )
            ).strip()
            + "\n"
        )
        if page.is_section_home:
            body += "\n" + build_related_links(page) + build_section_pager(page)
        elif page.section_meta:
            body = build_child_intro(page) + body
        write_text(page.output_path, front_matter(page) + body)


if __name__ == "__main__":
    generate()
