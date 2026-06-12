#!/usr/bin/env python3
"""
HTML Report Generator for Thesis Reader
Generates structured HTML analysis reports for academic papers.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field


# ============================================================================
# Data Classes
# ============================================================================

@dataclass
class PaperBasicInfo:
    """Basic paper information"""
    title: str
    title_cn: str = ""
    authors: str = ""
    conference: str = ""
    doi: str = ""
    doi_url: str = ""
    institution: str = ""


@dataclass
class AuthorResearchInfo:
    """Author research profile"""
    name: str
    affiliation: str = ""
    research_tags: List[str] = field(default_factory=list)


@dataclass
class RelatedPaperItem:
    """Related paper reference"""
    title: str
    meta: str = ""
    description: str = ""
    relation: str = ""
    doi_url: str = ""


@dataclass
class ProblemSolutionPair:
    """Problem-solution contrast pair"""
    problem_title: str
    problem_desc: str
    solution_title: str
    solution_desc: str


@dataclass
class ContributionItem:
    """Contribution item"""
    number: int
    title: str
    description: str


@dataclass
class RoadmapChild:
    """Roadmap child item"""
    number: str
    title: str


@dataclass
class RoadmapItem:
    """Roadmap section item"""
    number: str
    title: str
    description: str = ""
    children: List[RoadmapChild] = field(default_factory=list)


@dataclass
class CompareTableHeader:
    """Comparison table column header"""
    columns: List[str] = field(default_factory=list)


@dataclass
class CompareTableRow:
    """Comparison table row"""
    cells: List[str] = field(default_factory=list)


@dataclass
class MetricCard:
    """Metric display card"""
    icon: str
    value: str
    label: str


@dataclass
class KeyTechCard:
    """Key technology card"""
    icon: str
    title: str
    description: str


@dataclass
class SampleCard:
    """Sample/demo card"""
    icon: str
    title: str
    description: str
    tags: List[str] = field(default_factory=list)


@dataclass
class ProgressCard:
    """Progress indicator card"""
    title: str
    value: str
    percentage: int


@dataclass
class DiscussionCard:
    """Discussion/limitation card"""
    title: str
    description: str


@dataclass
class ChapterOverview:
    """Chapter overview for full paper"""
    number: str
    title: str
    description: str


@dataclass
class ExtendedPaper:
    """Extended reading paper reference"""
    title: str
    meta: str = ""
    description: str = ""
    tags: List[str] = field(default_factory=list)
    doi_url: str = ""


# ============================================================================
# Core HTML Generator
# ============================================================================

class HTMLReportGenerator:
    """HTML report generator with unified styling and navigation"""

    def __init__(self, paper_title: str = "Paper Analysis"):
        self.paper_title = paper_title

    def get_css(self) -> str:
        """Get unified CSS styles"""
        return '''
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            :root {
                --primary: #007AFF; --primary-dark: #0056CC; --primary-light: rgba(0, 122, 255, 0.1);
                --danger: #FF3B30; --danger-light: rgba(255, 59, 48, 0.1);
                --success: #34C759; --success-light: rgba(52, 199, 89, 0.1);
                --warning: #FF9500; --warning-light: rgba(255, 149, 0, 0.1);
                --purple: #AF52DE; --purple-light: rgba(175, 82, 222, 0.1);
                --bg: #FFFFFF; --bg-secondary: #F5F5F7;
                --text: #1D1D1F; --text-secondary: #86868B; --border: #E5E5E7;
                --card-shadow: 0 4px 24px rgba(0,0,0,0.08); --hover-shadow: 0 8px 32px rgba(0,0,0,0.12);
                --gradient-start: #E3F2FD; --gradient-end: #BBDEFB;
            }
            body {
                font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif;
                background: linear-gradient(135deg, var(--gradient-start) 0%, var(--gradient-end) 100%);
                color: var(--text); line-height: 1.6; overflow-x: hidden;
            }
            .app { display: flex; width: 100%; min-height: 100vh; }
            .sidebar {
                width: 280px; background: rgba(255, 255, 255, 0.95);
                border-right: 1px solid var(--border);
                display: flex; flex-direction: column; position: fixed; left: 0; top: 0; bottom: 0;
                z-index: 1000; box-shadow: 0 0 20px rgba(0,0,0,0.05);
            }
            .sidebar-header { padding: 24px; border-bottom: 1px solid var(--border); }
            .sidebar-header h1 { font-size: 18px; font-weight: 700; color: var(--text); margin-bottom: 8px; }
            .sidebar-header p { font-size: 13px; color: var(--text-secondary); }
            .nav-menu { flex: 1; padding: 16px 12px; overflow-y: auto; }
            .nav-item {
                display: flex; align-items: center; padding: 12px 16px; margin: 4px 0;
                border-radius: 10px; cursor: pointer; transition: all 0.2s ease; font-size: 14px; color: var(--text);
            }
            .nav-item:hover { background: var(--bg-secondary); }
            .nav-item.active { background: var(--primary); color: white; font-weight: 500; }
            .content { flex: 1; display: flex; flex-direction: column; background: transparent; margin-left: 280px; }
            .content-body { flex: 1; padding: 32px 48px; padding-bottom: 80px; overflow-y: auto; background: transparent; }
            .title-card { background: var(--bg); border-radius: 16px; padding: 28px; margin-bottom: 24px; box-shadow: var(--card-shadow); text-align: center; }
            .title-card h2 { font-size: 28px; font-weight: 700; color: var(--text); margin-bottom: 8px; }
            .title-card p { font-size: 14px; color: var(--text-secondary); }
            .page { display: none; animation: fadeIn 0.4s ease; }
            .page.active { display: block; }
            @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
            .card { background: var(--bg); border-radius: 16px; padding: 32px; margin-bottom: 24px; box-shadow: var(--card-shadow); transition: all 0.3s ease; }
            .card:hover { box-shadow: var(--hover-shadow); }
            .card-header { display: flex; align-items: center; margin-bottom: 24px; }
            .card-icon { width: 48px; height: 48px; background: linear-gradient(135deg, var(--primary), var(--primary-dark)); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-right: 16px; }
            .card-title { font-size: 20px; font-weight: 600; color: var(--text); }
            .card-subtitle { font-size: 13px; color: var(--text-secondary); margin-top: 4px; }
            .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 24px; }
            .stat-card { background: var(--bg-secondary); border-radius: 12px; padding: 20px; text-align: center; transition: all 0.2s ease; }
            .stat-card:hover { transform: translateY(-2px); }
            .stat-number { font-size: 18px; font-weight: 600; color: var(--primary); margin-bottom: 6px; }
            .stat-label { font-size: 12px; color: var(--text-secondary); }
            .info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 24px; }
            .info-item { background: var(--bg-secondary); padding: 16px; border-radius: 10px; }
            .info-label { font-size: 11px; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px; }
            .info-value { font-size: 14px; font-weight: 600; color: var(--text); }
            .author-item { background: var(--bg-secondary); padding: 16px; border-radius: 12px; margin-bottom: 12px; }
            .author-item:last-child { margin-bottom: 0; }
            .author-name { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 6px; }
            .author-affiliation { font-size: 13px; color: var(--text-secondary); margin-bottom: 8px; }
            .author-research { display: flex; flex-wrap: wrap; gap: 6px; }
            .research-tag { padding: 4px 10px; background: rgba(0,122,255,0.1); color: var(--primary); border-radius: 12px; font-size: 12px; }
            .related-paper { padding: 16px; background: var(--bg-secondary); border-radius: 10px; margin-bottom: 12px; }
            .related-paper:last-child { margin-bottom: 0; }
            .related-paper-title { font-size: 14px; font-weight: 500; color: var(--text); margin-bottom: 6px; }
            .related-paper-meta { font-size: 12px; color: var(--text-secondary); margin-bottom: 8px; }
            .related-paper-desc { font-size: 13px; line-height: 1.6; color: var(--text); margin-bottom: 8px; }
            .related-paper-relation { font-size: 13px; line-height: 1.6; color: var(--text-secondary); padding: 10px; background: rgba(0,122,255,0.08); border-radius: 8px; margin-bottom: 8px; }
            .keyword-tag { display: inline-block; padding: 5px 12px; background: rgba(0,122,255,0.1); color: var(--primary); border-radius: 16px; font-size: 12px; font-weight: 500; margin: 4px 4px 4px 0; }
            .answer-box { background: var(--bg-secondary); border-radius: 12px; padding: 20px; margin-top: 12px; }
            .answer-text, .answer-box p { font-size: 15px; line-height: 1.8; color: var(--text); }
            .contribution-item { display: flex; align-items: flex-start; margin-bottom: 14px; padding: 16px; background: var(--bg-secondary); border-radius: 10px; }
            .contribution-item .contribution-number { display: inline-block; width: 28px; height: 28px; background: var(--primary); color: white; border-radius: 50%; text-align: center; line-height: 28px; font-size: 14px; font-weight: 700; margin-right: 12px; flex-shrink: 0; }
            .contribution-text { font-size: 14px; line-height: 1.7; color: var(--text); }
            .chapter-card { display: flex; align-items: flex-start; padding: 24px; background: var(--bg-secondary); border-radius: 12px; margin-bottom: 16px; transition: all 0.2s ease; }
            .chapter-card:hover { background: #E8F4FF; }
            .chapter-number { background: var(--primary); color: white; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 700; margin-right: 20px; flex-shrink: 0; }
            .chapter-content { flex: 1; }
            .chapter-title { font-weight: 600; font-size: 16px; margin-bottom: 8px; }
            .chapter-desc { font-size: 14px; color: var(--text-secondary); line-height: 1.4; }
            .timeline { position: relative; padding-left: 40px; }
            .timeline::before { content: ""; position: absolute; left: 15px; top: 0; bottom: 0; width: 2px; background: linear-gradient(180deg, var(--primary), var(--bg-secondary)); }
            .timeline-item { position: relative; margin-bottom: 24px; padding: 20px; background: var(--bg); border-radius: 12px; box-shadow: var(--card-shadow); }
            .timeline-item::before { content: ""; position: absolute; left: -31px; top: 24px; width: 12px; height: 12px; background: var(--primary); border-radius: 50%; border: 3px solid var(--bg); box-shadow: 0 0 0 3px var(--primary); }
            .timeline-step { font-size: 14px; font-weight: 700; color: var(--primary); margin-bottom: 6px; }
            .timeline-title { font-size: 16px; font-weight: 600; margin-bottom: 8px; }
            .timeline-desc { font-size: 14px; color: var(--text-secondary); }
            .compare-section { margin-bottom: 0; }
            .compare-title { font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 14px; padding-left: 12px; border-left: 4px solid var(--primary); }
            .compare-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
            .compare-box { padding: 20px; border-radius: 12px; position: relative; }
            .compare-box.problem { background: var(--danger-light); border: 1px solid rgba(255, 59, 48, 0.2); }
            .compare-box.solution { background: var(--success-light); border: 1px solid rgba(52, 199, 89, 0.2); }
            .compare-label { display: inline-block; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600; margin-bottom: 12px; }
            .compare-box.problem .compare-label { background: var(--danger); color: white; }
            .compare-box.solution .compare-label { background: var(--success); color: white; }
            .compare-text { font-size: 14px; line-height: 1.7; color: var(--text); }
            .contributions-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; }
            .contribution-card { padding: 20px; background: var(--bg-secondary); border-radius: 12px; border-left: 4px solid var(--primary); transition: all 0.2s ease; }
            .contribution-card:hover { transform: translateY(-2px); background: #E8F4FF; }
            .roadmap-container { position: relative; padding-left: 40px; }
            .roadmap-container::before { content: ""; position: absolute; left: 15px; top: 0; bottom: 0; width: 2px; background: linear-gradient(180deg, var(--primary), var(--border)); }
            .roadmap-item { position: relative; margin-bottom: 20px; }
            .roadmap-item:last-child { margin-bottom: 0; }
            .roadmap-item::before { content: ""; position: absolute; left: -31px; top: 24px; width: 12px; height: 12px; background: var(--primary); border-radius: 50%; border: 3px solid var(--bg); box-shadow: 0 0 0 2px var(--primary); }
            .roadmap-header { display: flex; align-items: center; cursor: pointer; padding: 16px 20px; background: var(--bg-secondary); border-radius: 12px; transition: all 0.2s ease; }
            .roadmap-header:hover { background: #E8F4FF; }
            .roadmap-header.active { background: var(--primary-light); }
            .roadmap-number { background: var(--primary); color: white; width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 700; margin-right: 16px; flex-shrink: 0; }
            .roadmap-title { font-size: 15px; font-weight: 600; color: var(--text); flex: 1; }
            .roadmap-desc { font-size: 12px; color: var(--text-secondary); margin-top: 2px; }
            .roadmap-toggle { width: 24px; height: 24px; background: var(--bg); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; color: var(--primary); transition: transform 0.3s ease; flex-shrink: 0; }
            .roadmap-header.active .roadmap-toggle { transform: rotate(45deg); }
            .roadmap-children { margin-left: 16px; margin-top: 12px; overflow: hidden; max-height: 0; transition: max-height 0.3s ease; }
            .roadmap-children.expanded { max-height: 1000px; }
            .roadmap-child { padding: 10px 16px; background: var(--bg); border-radius: 8px; margin-bottom: 8px; font-size: 13px; color: var(--text-secondary); border-left: 3px solid var(--primary); }
            .roadmap-child:last-child { margin-bottom: 0; }
            .roadmap-child-number { color: var(--primary); font-weight: 600; margin-right: 8px; }
            .term { color: var(--primary); cursor: help; border-bottom: 1px dashed var(--primary); text-decoration: none; position: relative; }
            .impact-box { background: var(--warning-light); border: 1px solid rgba(255, 149, 0, 0.2); border-radius: 12px; padding: 20px; display: flex; align-items: flex-start; }
            .impact-icon { font-size: 24px; margin-right: 16px; flex-shrink: 0; }
            .impact-content h4 { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
            .impact-content p { font-size: 14px; line-height: 1.7; color: var(--text-secondary); }
            .compare-table-wrapper { overflow-x: auto; border-radius: 12px; }
            .compare-table { width: 100%; border-collapse: collapse; min-width: 600px; }
            .compare-table th, .compare-table td { padding: 14px 16px; text-align: left; border-bottom: 1px solid var(--border); font-size: 13px; }
            .compare-table th { background: var(--bg-secondary); font-weight: 600; color: var(--text); }
            .compare-table tr:hover td { background: #F8FAFF; }
            .compare-table tr:last-child td { border-bottom: none; }
            .table-paper { font-weight: 500; color: var(--text); }
            .positioning-card { background: linear-gradient(135deg, var(--primary-light) 0%, rgba(255,255,255,1) 100%); border: 2px solid var(--primary); }
            .positioning-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 16px; }
            .positioning-item { background: var(--bg); padding: 16px; border-radius: 10px; border-left: 4px solid var(--primary); }
            .category-tag { display: inline-flex; align-items: center; padding: 8px 16px; border-radius: 20px; font-size: 13px; font-weight: 500; margin: 4px; }
            .category-tag.blue { background: var(--primary-light); color: var(--primary); }
            .category-tag.green { background: var(--success-light); color: var(--success); }
            .category-tag.orange { background: var(--warning-light); color: var(--warning); }
            .category-tag.purple { background: var(--purple-light); color: var(--purple); }
            .category-tag.red { background: var(--danger-light); color: var(--danger); }
            .group-header { display: flex; align-items: center; margin-bottom: 20px; padding-bottom: 12px; border-bottom: 2px solid var(--border); }
            .group-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 20px; margin-right: 12px; }
            .group-icon.blue { background: var(--primary-light); }
            .group-icon.green { background: var(--success-light); }
            .group-icon.orange { background: var(--warning-light); }
            .group-icon.purple { background: var(--purple-light); }
            .group-title { font-size: 18px; font-weight: 600; color: var(--text); }
            .key-tech-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
            .key-tech-card { background: var(--bg-secondary); border-radius: 12px; padding: 20px; border-top: 4px solid var(--primary); transition: all 0.2s ease; }
            .key-tech-card:hover { transform: translateY(-4px); box-shadow: var(--hover-shadow); }
            .key-tech-icon { font-size: 32px; margin-bottom: 12px; }
            .key-tech-title { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
            .key-tech-desc { font-size: 13px; line-height: 1.6; color: var(--text-secondary); }
            .concept-card { background: linear-gradient(135deg, var(--primary-light) 0%, rgba(255,255,255,1) 100%); border-radius: 12px; padding: 20px; margin-bottom: 16px; border-left: 4px solid var(--primary); }
            .concept-card:last-child { margin-bottom: 0; }
            .concept-title { font-size: 15px; font-weight: 600; color: var(--primary); margin-bottom: 8px; }
            .concept-desc { font-size: 14px; line-height: 1.7; color: var(--text); }
            .algo-card { background: var(--bg-secondary); border-radius: 12px; padding: 24px; margin-bottom: 16px; border-left: 4px solid var(--primary); }
            .algo-card:last-child { margin-bottom: 0; }
            .algo-title { font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }
            .algo-number { display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px; background: var(--primary); color: white; border-radius: 6px; font-size: 12px; font-weight: 600; }
            .algo-content { font-size: 14px; line-height: 1.8; color: var(--text-secondary); }
            .flow-chart { display: flex; flex-direction: column; gap: 16px; padding: 20px 0; }
            .flow-step { display: flex; align-items: center; gap: 20px; }
            .flow-node { flex: 1; background: var(--bg-secondary); border-radius: 12px; padding: 20px; border-left: 4px solid var(--primary); transition: all 0.2s ease; }
            .flow-node:hover { background: var(--primary-light); transform: translateX(4px); }
            .flow-node-number { display: inline-block; width: 28px; height: 28px; background: var(--primary); color: white; border-radius: 50%; text-align: center; line-height: 28px; font-size: 14px; font-weight: 600; margin-right: 12px; }
            .flow-node-title { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
            .flow-node-desc { font-size: 13px; color: var(--text-secondary); }
            .flow-arrow { width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; color: var(--primary); font-size: 24px; }
            .param-table { width: 100%; border-collapse: collapse; margin-top: 16px; }
            .param-table th, .param-table td { padding: 14px 16px; text-align: left; border-bottom: 1px solid var(--border); font-size: 13px; }
            .param-table th { background: var(--bg-secondary); font-weight: 600; color: var(--text); }
            .param-table tr:hover td { background: #F8FAFF; }
            .param-name { font-weight: 500; color: var(--primary); font-family: monospace; }
            .sample-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
            .sample-card { background: var(--bg-secondary); border-radius: 12px; overflow: hidden; transition: all 0.2s ease; }
            .sample-card:hover { transform: translateY(-4px); box-shadow: var(--hover-shadow); }
            .sample-image { height: 120px; background: linear-gradient(135deg, var(--primary-light), var(--bg)); display: flex; align-items: center; justify-content: center; font-size: 48px; }
            .sample-info { padding: 20px; }
            .sample-title { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
            .sample-desc { font-size: 13px; color: var(--text-secondary); line-height: 1.6; }
            .sample-tag { display: inline-block; padding: 4px 10px; background: var(--primary-light); color: var(--primary); border-radius: 12px; font-size: 11px; font-weight: 500; margin-top: 8px; }
            .metric-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; }
            .metric-card { background: var(--bg-secondary); border-radius: 12px; padding: 24px; text-align: center; transition: all 0.2s ease; }
            .metric-card:hover { background: var(--primary-light); }
            .metric-icon { font-size: 28px; margin-bottom: 8px; }
            .metric-value { font-size: 22px; font-weight: 700; color: var(--primary); margin-bottom: 4px; }
            .metric-label { font-size: 12px; color: var(--text-secondary); }
            .compare-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
            .compare-card { background: var(--bg-secondary); border-radius: 12px; padding: 24px; border-left: 4px solid var(--primary); }
            .compare-card.highlight { border-left-color: var(--success); background: var(--success-light); }
            .progress-card { background: var(--bg-secondary); border-radius: 12px; padding: 20px; margin-bottom: 16px; }
            .progress-card:last-child { margin-bottom: 0; }
            .progress-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
            .progress-title { font-size: 14px; font-weight: 600; color: var(--text); }
            .progress-value { font-size: 14px; font-weight: 600; color: var(--primary); }
            .progress-bar { height: 8px; background: var(--bg); border-radius: 4px; overflow: hidden; }
            .progress-fill { height: 100%; background: linear-gradient(90deg, var(--primary), var(--success)); border-radius: 4px; transition: width 0.3s ease; }
            .discussion-card { background: linear-gradient(135deg, var(--warning-light) 0%, rgba(255,255,255,1) 100%); border-radius: 12px; padding: 24px; margin-bottom: 16px; border-left: 4px solid var(--warning); }
            .discussion-card:last-child { margin-bottom: 0; }
            .discussion-title { font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
            .discussion-content { font-size: 14px; line-height: 1.7; color: var(--text-secondary); }
            a { color: var(--primary); text-decoration: none; }
            a:hover { text-decoration: underline; }
            @media (max-width: 768px) {
                .sidebar { transform: translateX(-100%); transition: transform 0.3s ease; }
                .sidebar.visible { transform: translateX(0); }
                .content { margin-left: 0; }
                .content-body { padding: 16px; }
                .compare-row, .flow-step { flex-direction: column; }
                .flow-arrow { transform: rotate(90deg); }
                .key-tech-grid, .sample-grid, .compare-grid { grid-template-columns: 1fr; }
                .metric-grid { grid-template-columns: repeat(2, 1fr); }
            }
        </style>
        '''

    def get_nav_script(self, page_ids: List[str]) -> str:
        """Get navigation JavaScript"""
        return '''
        <script>
            const pages = %s;
            let currentPage = 0;
            function toggleRoadmap(header) {
                const children = header.nextElementSibling;
                header.classList.toggle('active');
                children.classList.toggle('expanded');
            }
            function goToPage(index) {
                if (index < 0 || index >= pages.length) return;
                document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
                const targetPage = document.getElementById('page-' + pages[index]);
                if (targetPage) { targetPage.classList.add('active'); }
                document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
                const activeNavItem = document.querySelector('.nav-item[data-page="' + pages[index] + '"]');
                if (activeNavItem) { activeNavItem.classList.add('active'); }
                currentPage = index;
                window.scrollTo(0, 0);
            }
            document.querySelectorAll('.nav-item').forEach(item => {
                item.addEventListener('click', () => {
                    const page = item.getAttribute('data-page');
                    goToPage(pages.indexOf(page));
                });
            });
        </script>
        ''' % repr(page_ids)

    def build_html(self, pages: List[Dict], sidebar_title: str = "Paper Analysis") -> str:
        """Build complete HTML page from pages list"""
        page_ids = [p['id'] for p in pages]
        nav_html = ''.join(
            '''<div class="nav-item %s" data-page="%s"><span>%s</span></div>''' % (
                'active' if i == 0 else '', p['id'], p['title']
            ) for i, p in enumerate(pages)
        )
        pages_html = ''.join(
            '''<div class="page %s" id="page-%s"><div class="title-card"><h2>%s</h2><p>%s</p></div>%s</div>''' % (
                'active' if i == 0 else '', p['id'], p['title'],
                p.get('subtitle', ''), p.get('content', '')
            ) for i, p in enumerate(pages)
        )
        return (
            '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">'''
            '''<meta name="viewport" content="width=device-width, initial-scale=1.0">'''
            '''<title>%s</title>%s</head><body>'''
            '''<div class="app"><div class="sidebar"><div class="sidebar-header">'''
            '''<h1>%s</h1><p>Paper Analysis</p></div><div class="nav-menu">%s</div></div>'''
            '''<div class="content"><div class="content-body">%s</div></div></div>%s'''
            '''</body></html>'''
        ) % (self.paper_title, self.get_css(), sidebar_title, nav_html, pages_html, self.get_nav_script(page_ids))


# ============================================================================
# Page Content Builders
# ============================================================================

def _card(icon: str, title: str, subtitle: str = "", content: str = "") -> str:
    """Build a generic card"""
    subtitle_html = f'<div class="card-subtitle">{subtitle}</div>' if subtitle else ""
    return (
        f'<div class="card"><div class="card-header">'
        f'<div class="card-icon">{icon}</div><div>'
        f'<div class="card-title">{title}</div>{subtitle_html}'
        f'</div></div>{content}</div>'
    )


# ============================================================================
# Report 1: Abstract (摘要报告)
# ============================================================================

def create_abstract_report(
    paper_title: str,
    basic_info: PaperBasicInfo,
    author_research: List[AuthorResearchInfo] = None,
    related_papers: List[RelatedPaperItem] = None,
    research_questions: List[str] = None,
    core_methods: List[str] = None,
    contributions: List[ContributionItem] = None,
    validation_results: List[str] = None,
    keywords: List[str] = None,
    abstract_original: str = "",
    abstract_translation: str = "",
    output_path: str = "abstract.html"
) -> str:
    """Create abstract analysis report"""
    generator = HTMLReportGenerator(paper_title)
    author_research = author_research or []
    related_papers = related_papers or []
    research_questions = research_questions or []
    core_methods = core_methods or []
    contributions = contributions or []
    validation_results = validation_results or []
    keywords = keywords or []

    # Page 1: Paper Info
    info_html = ""
    if basic_info.title or basic_info.authors or basic_info.conference or basic_info.doi:
        info_html += '<div class="card">'
        info_html += '<div class="card-header"><div class="card-icon">📄</div><div>'
        info_html += f'<div class="card-title">{basic_info.title}</div>'
        if basic_info.title_cn:
            info_html += f'<div class="card-subtitle">{basic_info.title_cn}</div>'
        info_html += '</div></div></div>'

        info_items = []
        if basic_info.authors:
            info_items.append(f'<div class="info-item"><div class="info-label">Authors</div><div class="info-value">{basic_info.authors}</div></div>')
        if basic_info.conference:
            info_items.append(f'<div class="info-item"><div class="info-label">Published in</div><div class="info-value">{basic_info.conference}</div></div>')
        if basic_info.institution:
            info_items.append(f'<div class="info-item"><div class="info-label">Institution</div><div class="info-value">{basic_info.institution}</div></div>')
        if basic_info.doi:
            doi_link = f'<a href="{basic_info.doi_url}" target="_blank">{basic_info.doi}</a>' if basic_info.doi_url else basic_info.doi
            info_items.append(f'<div class="info-item"><div class="info-label">DOI</div><div class="info-value">{doi_link}</div></div>')
        if info_items:
            info_html += f'<div class="info-grid">{"".join(info_items)}</div>'

    if author_research:
        info_html += '<div class="card">'
        info_html += '<div class="card-header"><div class="card-icon">👥</div><div>'
        info_html += '<div class="card-title">Author Research Areas</div>'
        info_html += '<div class="card-subtitle">Authors\' Research Focus</div>'
        info_html += '</div></div>'
        for author in author_research:
            info_html += f'<div class="author-item"><div class="author-name">{author.name}</div>'
            if author.affiliation:
                info_html += f'<div class="author-affiliation">{author.affiliation}</div>'
            if author.research_tags:
                tags_html = "".join(f'<span class="research-tag">{t}</span>' for t in author.research_tags)
                info_html += f'<div class="author-research">{tags_html}</div>'
            info_html += '</div>'
        info_html += '</div>'

    if related_papers:
        info_html += '<div class="card">'
        info_html += '<div class="card-header"><div class="card-icon">📚</div><div>'
        info_html += '<div class="card-title">Related Papers</div>'
        info_html += '<div class="card-subtitle">Recommended Reading</div>'
        info_html += '</div></div>'
        for paper in related_papers:
            info_html += f'<div class="related-paper">'
            info_html += f'<div class="related-paper-title">{paper.title}</div>'
            if paper.meta:
                info_html += f'<div class="related-paper-meta">{paper.meta}</div>'
            if paper.description:
                info_html += f'<div class="related-paper-desc">{paper.description}</div>'
            if paper.relation:
                info_html += f'<div class="related-paper-relation"><strong>Relation to this paper:</strong> {paper.relation}</div>'
            if paper.doi_url:
                info_html += f'<a href="{paper.doi_url}" target="_blank" style="font-size: 12px;">{paper.doi_url}</a>'
            info_html += '</div>'
        info_html += '</div>'

    # Page 2: Key questions & contributions
    qna_html = ""
    if research_questions:
        qna_html += '<div class="card">'
        qna_html += '<div class="card-header"><div class="card-icon">🎯</div><div>'
        qna_html += '<div class="card-title">Research Problem</div>'
        qna_html += '<div class="card-subtitle">What is this paper about?</div>'
        qna_html += '</div></div>'
        for q in research_questions:
            qna_html += f'<div class="answer-box"><p style="font-size: 15px; line-height: 1.8; color: var(--text);">{q}</p></div>'
        qna_html += '</div>'

    if core_methods:
        qna_html += '<div class="card">'
        qna_html += '<div class="card-header"><div class="card-icon">💡</div><div>'
        qna_html += '<div class="card-title">Core Methods</div>'
        qna_html += '<div class="card-subtitle">Technical Approach</div>'
        qna_html += '</div></div>'
        for m in core_methods:
            qna_html += f'<div class="answer-box"><p style="font-size: 15px; line-height: 1.8; color: var(--text);">{m}</p></div>'
        qna_html += '</div>'

    if contributions:
        qna_html += '<div class="card">'
        qna_html += '<div class="card-header"><div class="card-icon">🏆</div><div>'
        qna_html += '<div class="card-title">Main Contributions</div>'
        qna_html += '<div class="card-subtitle">Key Innovations</div>'
        qna_html += '</div></div>'
        for c in contributions:
            qna_html += f'<div class="contribution-item"><span class="contribution-number">{c.number}</span>'
            qna_html += f'<div class="contribution-text"><strong>{c.title}</strong><br/>{c.description}</div></div>'
        qna_html += '</div>'

    if validation_results:
        qna_html += '<div class="card">'
        qna_html += '<div class="card-header"><div class="card-icon">📊</div><div>'
        qna_html += '<div class="card-title">Validation Results</div>'
        qna_html += '<div class="card-subtitle">Experimental Findings</div>'
        qna_html += '</div></div>'
        for v in validation_results:
            qna_html += f'<div class="answer-box"><p style="font-size: 15px; line-height: 1.8; color: var(--text);">{v}</p></div>'
        qna_html += '</div>'

    if keywords:
        qna_html += '<div class="card">'
        qna_html += '<div class="card-header"><div class="card-icon">🔖</div><div>'
        qna_html += '<div class="card-title">Keywords</div></div></div>'
        qna_html += '<div style="margin-top: 16px;">'
        qna_html += "".join(f'<span class="keyword-tag">{k}</span>' for k in keywords)
        qna_html += '</div></div>'

    # Page 3: Original abstract + translation
    original_html = ""
    if abstract_original:
        original_html += '<div class="card">'
        original_html += '<div class="card-header"><div class="card-icon">📝</div><div>'
        original_html += '<div class="card-title">Full Abstract (Original)</div></div></div>'
        original_html += f'<div style="background: var(--bg-secondary); border-radius: 12px; padding: 20px; margin-top: 12px;">'
        original_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text);">{abstract_original}</p></div>'
        original_html += '</div>'

    if abstract_translation:
        original_html += '<div class="card">'
        original_html += '<div class="card-header"><div class="card-icon">🌐</div><div>'
        original_html += '<div class="card-title">Abstract (Translation)</div></div></div>'
        original_html += f'<div style="background: var(--bg-secondary); border-radius: 12px; padding: 20px; margin-top: 12px;">'
        original_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text);">{abstract_translation}</p></div>'
        original_html += '</div>'

    pages = []
    if info_html:
        pages.append({"id": "info", "title": "📄 Paper Info", "subtitle": "Basic Information", "content": info_html})
    if qna_html:
        pages.append({"id": "qna", "title": "💬 Abstract Analysis", "subtitle": "Key Insights", "content": qna_html})
    if original_html:
        pages.append({"id": "original", "title": "📝 Full Text", "subtitle": "Abstract Text", "content": original_html})

    if not pages:
        pages.append({"id": "empty", "title": "📋 Abstract", "subtitle": "No content",
                      "content": '<div class="card"><div class="card-header"><div class="card-icon">📋</div><div><div class="card-title">No Data</div></div></div><p style="font-size: 15px; line-height: 1.8; color: var(--text-secondary);">Provide data to generate the abstract report.</p></div>'})

    html = generator.build_html(pages, "📋 Abstract")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Abstract report generated: {output_path}")
    return html


# ============================================================================
# Report 2: Full Paper Overview (全文总述)
# ============================================================================

def create_full_paper_report(
    paper_title: str,
    overview_paragraphs: List[str] = None,
    stats: List[Dict[str, str]] = None,
    chapters: List[ChapterOverview] = None,
    workflow: List[Dict[str, str]] = None,
    impact: str = "",
    references: List[Dict[str, str]] = None,
    output_path: str = "full_paper.html"
) -> str:
    """Create full paper overview report"""
    generator = HTMLReportGenerator(paper_title)
    overview_paragraphs = overview_paragraphs or []
    stats = stats or []
    chapters = chapters or []
    workflow = workflow or []
    references = references or []

    # Page 1: Overview
    overview_html = ""
    if overview_paragraphs:
        overview_html += '<div class="card">'
        overview_html += '<div class="card-header"><div class="card-icon">📖</div><div>'
        overview_html += '<div class="card-title">Paper Overview</div>'
        overview_html += '<div class="card-subtitle">Overall Summary</div>'
        overview_html += '</div></div>'
        for p in overview_paragraphs:
            overview_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{p}</p>'
        overview_html += '</div>'

    if stats:
        overview_html += '<div class="stats-grid">'
        for s in stats:
            overview_html += (
                f'<div class="stat-card"><div class="stat-number">{s.get("value", "")}</div>'
                f'<div class="stat-label">{s.get("label", "")}</div></div>'
            )
        overview_html += '</div>'

    # Page 2: Chapter structure
    chapter_html = ""
    if chapters:
        chapter_html += '<div class="card">'
        chapter_html += '<div class="card-header"><div class="card-icon">📑</div><div>'
        chapter_html += '<div class="card-title">Chapter Structure</div>'
        chapter_html += '<div class="card-subtitle">Paper Organization</div>'
        chapter_html += '</div></div>'
        for ch in chapters:
            chapter_html += (
                f'<div class="chapter-card"><div class="chapter-number">{ch.number}</div>'
                f'<div class="chapter-content"><div class="chapter-title">{ch.title}</div>'
                f'<div class="chapter-desc">{ch.description}</div></div></div>'
            )
        chapter_html += '</div>'

    # Page 3: Workflow
    workflow_html = ""
    if workflow:
        workflow_html += '<div class="card">'
        workflow_html += '<div class="card-header"><div class="card-icon">🔄</div><div>'
        workflow_html += '<div class="card-title">Work Flow</div>'
        workflow_html += '<div class="card-subtitle">How the Method Works</div>'
        workflow_html += '</div></div>'
        workflow_html += '<div class="flow-chart">'
        for i, step in enumerate(workflow):
            workflow_html += (
                f'<div class="flow-step"><div class="flow-node">'
                f'<span class="flow-node-number">{i + 1}</span>'
                f'<span class="flow-node-title">{step.get("title", "")}</span><br/>'
                f'<span class="flow-node-desc">{step.get("desc", "")}</span></div>'
            )
            if i < len(workflow) - 1:
                workflow_html += '<div class="flow-arrow">↓</div>'
            workflow_html += '</div>'
        workflow_html += '</div></div>'

    # Page 4: Impact & significance
    impact_html = ""
    if impact:
        impact_html += '<div class="impact-box">'
        impact_html += '<div class="impact-icon">💡</div>'
        impact_html += f'<div class="impact-content"><h4>Impact & Significance</h4><p>{impact}</p></div>'
        impact_html += '</div>'

    # Page 5: References
    refs_html = ""
    if references:
        refs_html += '<div class="card">'
        refs_html += '<div class="card-header"><div class="card-icon">📚</div><div>'
        refs_html += '<div class="card-title">Key References</div>'
        refs_html += '<div class="card-subtitle">Important Citations</div>'
        refs_html += '</div></div>'
        for ref in references:
            refs_html += (
                f'<div style="padding: 16px; background: var(--bg-secondary); border-radius: 10px; margin-bottom: 12px; border-left: 4px solid var(--primary);">'
                f'<div style="font-size: 13px; font-weight: 600; color: var(--primary); margin-bottom: 6px;">[{ref.get("id", "")}] {ref.get("title", "")}</div>'
                f'<div style="font-size: 12px; color: var(--text-secondary); margin-bottom: 6px;">{ref.get("meta", "")}</div>'
                f'<div style="font-size: 12px; color: var(--text-secondary);">{ref.get("desc", "")}</div>'
                f'</div>'
            )
        refs_html += '</div>'

    pages = []
    if overview_html:
        pages.append({"id": "overview", "title": "📖 Overview", "subtitle": "Paper Summary", "content": overview_html})
    if chapter_html:
        pages.append({"id": "chapters", "title": "📑 Chapters", "subtitle": "Structure", "content": chapter_html})
    if workflow_html:
        pages.append({"id": "workflow", "title": "🔄 Workflow", "subtitle": "Process", "content": workflow_html})
    if impact_html:
        pages.append({"id": "impact", "title": "💡 Impact", "subtitle": "Significance", "content": impact_html})
    if refs_html:
        pages.append({"id": "references", "title": "📚 References", "subtitle": "Citations", "content": refs_html})

    if not pages:
        pages.append({"id": "empty", "title": "📖 Overview", "subtitle": "No content",
                      "content": '<div class="card"><div class="card-header"><div class="card-icon">📖</div><div><div class="card-title">No Data</div></div></div><p style="font-size: 15px; color: var(--text-secondary);">Provide data to generate the overview report.</p></div>'})

    html = generator.build_html(pages, "📖 Full Paper")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Full paper report generated: {output_path}")
    return html


# ============================================================================
# Report 3: Introduction (引言报告)
# ============================================================================

def create_introduction_report(
    paper_title: str,
    background: List[str] = None,
    motivation: List[str] = None,
    problem_solution_pairs: List[ProblemSolutionPair] = None,
    roadmap: List[RoadmapItem] = None,
    output_path: str = "introduction.html"
) -> str:
    """Create introduction analysis report"""
    generator = HTMLReportGenerator(paper_title)
    background = background or []
    motivation = motivation or []
    problem_solution_pairs = problem_solution_pairs or []
    roadmap = roadmap or []

    # Page 1: Background
    bg_html = ""
    if background:
        bg_html += '<div class="card">'
        bg_html += '<div class="card-header"><div class="card-icon">🎯</div><div>'
        bg_html += '<div class="card-title">Research Background</div>'
        bg_html += '<div class="card-subtitle">Context & Motivation</div>'
        bg_html += '</div></div>'
        for p in background:
            bg_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{p}</p>'
        bg_html += '</div>'

    if motivation:
        bg_html += '<div class="card">'
        bg_html += '<div class="card-header"><div class="card-icon">💡</div><div>'
        bg_html += '<div class="card-title">Why This Work Matters</div>'
        bg_html += '<div class="card-subtitle">Our Approach</div>'
        bg_html += '</div></div>'
        for p in motivation:
            bg_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{p}</p>'
        bg_html += '</div>'

    # Page 2: Problem-solution pairs
    ps_html = ""
    if problem_solution_pairs:
        for pair in problem_solution_pairs:
            ps_html += '<div class="compare-row" style="margin-bottom: 24px;">'
            ps_html += f'<div class="compare-box problem"><span class="compare-label">Problem</span>'
            ps_html += f'<div style="font-size: 15px; font-weight: 600; margin-bottom: 10px; color: var(--danger);">{pair.problem_title}</div>'
            ps_html += f'<div class="compare-text">{pair.problem_desc}</div></div>'
            ps_html += f'<div class="compare-box solution"><span class="compare-label">Solution</span>'
            ps_html += f'<div style="font-size: 15px; font-weight: 600; margin-bottom: 10px; color: var(--success);">{pair.solution_title}</div>'
            ps_html += f'<div class="compare-text">{pair.solution_desc}</div></div>'
            ps_html += '</div>'

    # Page 3: Roadmap
    roadmap_html = ""
    if roadmap:
        roadmap_html += '<div class="card">'
        roadmap_html += '<div class="card-header"><div class="card-icon">🗺️</div><div>'
        roadmap_html += '<div class="card-title">Paper Roadmap</div>'
        roadmap_html += '<div class="card-subtitle">Organization of the Paper</div>'
        roadmap_html += '</div></div>'
        roadmap_html += '<div class="roadmap-container">'
        for item in roadmap:
            roadmap_html += (
                f'<div class="roadmap-item"><div class="roadmap-header" onclick="toggleRoadmap(this)">'
                f'<span class="roadmap-number">{item.number}</span><div style="flex:1;">'
                f'<div class="roadmap-title">{item.title}</div>'
                f'{f"<div class=&quot;roadmap-desc&quot;>{item.description}</div>" if item.description else ""}'
                f'</div>{f"<span class=&quot;roadmap-toggle&quot;>+</span>" if item.children else ""}</div>'
            )
            if item.children:
                roadmap_html += '<div class="roadmap-children">'
                for child in item.children:
                    roadmap_html += (
                        f'<div class="roadmap-child"><span class="roadmap-child-number">{child.number}</span>{child.title}</div>'
                    )
                roadmap_html += '</div>'
            roadmap_html += '</div>'
        roadmap_html += '</div></div>'

    pages = []
    if bg_html:
        pages.append({"id": "background", "title": "🎯 Background", "subtitle": "Context", "content": bg_html})
    if ps_html:
        pages.append({"id": "problems", "title": "⚡ Problem-Solution", "subtitle": "Key Insights", "content": ps_html})
    if roadmap_html:
        pages.append({"id": "roadmap", "title": "🗺️ Roadmap", "subtitle": "Paper Structure", "content": roadmap_html})

    if not pages:
        pages.append({"id": "empty", "title": "📝 Introduction", "subtitle": "No content",
                      "content": '<div class="card"><p style="font-size: 15px; color: var(--text-secondary);">Provide data to generate the introduction report.</p></div>'})

    html = generator.build_html(pages, "📝 Introduction")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Introduction report generated: {output_path}")
    return html


# ============================================================================
# Report 4: Related Work (相关工作报告)
# ============================================================================

def create_related_work_report(
    paper_title: str,
    positioning_paragraphs: List[str] = None,
    positioning_items: List[Dict[str, str]] = None,
    category_tags: List[Dict[str, str]] = None,
    compare_table_headers: List[str] = None,
    compare_table_rows: List[List[str]] = None,
    related_papers_grouped: List[Dict[str, List[RelatedPaperItem]]] = None,
    research_timeline: List[Dict[str, str]] = None,
    key_insights: List[str] = None,
    output_path: str = "related_work.html"
) -> str:
    """Create related work analysis report"""
    generator = HTMLReportGenerator(paper_title)
    positioning_paragraphs = positioning_paragraphs or []
    positioning_items = positioning_items or []
    category_tags = category_tags or []
    compare_table_headers = compare_table_headers or []
    compare_table_rows = compare_table_rows or []
    related_papers_grouped = related_papers_grouped or []
    research_timeline = research_timeline or []
    key_insights = key_insights or []

    # Page 1: Positioning & categories
    overview_html = ""
    if positioning_paragraphs:
        overview_html += '<div class="card positioning-card">'
        overview_html += '<div class="card-header"><div class="card-icon">🎯</div><div>'
        overview_html += '<div class="card-title">Research Positioning</div>'
        overview_html += '<div class="card-subtitle">How This Paper Fits In</div>'
        overview_html += '</div></div>'
        for p in positioning_paragraphs:
            overview_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{p}</p>'
        overview_html += '</div>'

    if positioning_items:
        overview_html += '<div class="positioning-grid">'
        for item in positioning_items:
            overview_html += (
                f'<div class="positioning-item"><div style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">'
                f'<strong style="color: var(--primary);">{item.get("label", "")}</strong></div>'
                f'<div style="font-size: 14px; color: var(--text); line-height: 1.6;">{item.get("content", "")}</div></div>'
            )
        overview_html += '</div>'

    if category_tags:
        overview_html += '<div class="card">'
        overview_html += '<div class="card-header"><div class="card-icon">🏷️</div><div>'
        overview_html += '<div class="card-title">Research Categories</div>'
        overview_html += '<div class="card-subtitle">Key Themes</div>'
        overview_html += '</div></div><div>'
        for tag in category_tags:
            color = tag.get("color", "blue")
            overview_html += f'<span class="category-tag {color}">{tag.get("label", "")}</span>'
        overview_html += '</div></div>'

    # Page 2: Comparison table
    compare_html = ""
    if compare_table_headers and compare_table_rows:
        compare_html += '<div class="card">'
        compare_html += '<div class="card-header"><div class="card-icon">📊</div><div>'
        compare_html += '<div class="card-title">Method Comparison</div>'
        compare_html += '<div class="card-subtitle">How This Work Differs</div>'
        compare_html += '</div></div>'
        compare_html += '<div class="compare-table-wrapper"><table class="compare-table"><thead><tr>'
        for col in compare_table_headers:
            compare_html += f'<th>{col}</th>'
        compare_html += '</tr></thead><tbody>'
        for row in compare_table_rows:
            compare_html += '<tr>'
            for i, cell in enumerate(row):
                if i == 0:
                    compare_html += f'<td class="table-paper">{cell}</td>'
                else:
                    compare_html += f'<td>{cell}</td>'
            compare_html += '</tr>'
        compare_html += '</tbody></table></div></div>'

    # Page 3: Related papers
    papers_html = ""
    if related_papers_grouped:
        for group in related_papers_grouped:
            group_title = group.get("group_title", "")
            group_icon = group.get("group_icon", "📄")
            group_color = group.get("group_color", "blue")
            papers = group.get("papers", [])
            if papers:
                papers_html += '<div class="card">'
                papers_html += (
                    f'<div class="group-header"><div class="group-icon {group_color}">{group_icon}</div>'
                    f'<div class="group-title">{group_title}</div></div>'
                )
                for paper in papers:
                    papers_html += f'<div class="related-paper">'
                    papers_html += f'<div class="related-paper-title">{paper.title}</div>'
                    if paper.meta:
                        papers_html += f'<div class="related-paper-meta">{paper.meta}</div>'
                    if paper.description:
                        papers_html += f'<div class="related-paper-desc">{paper.description}</div>'
                    if paper.relation:
                        papers_html += f'<div class="related-paper-relation">{paper.relation}</div>'
                    if paper.doi_url:
                        papers_html += f'<a href="{paper.doi_url}" target="_blank" style="font-size: 12px;">{paper.doi_url}</a>'
                    papers_html += '</div>'
                papers_html += '</div>'

    # Page 4: Research timeline
    timeline_html = ""
    if research_timeline:
        timeline_html += '<div class="card">'
        timeline_html += '<div class="card-header"><div class="card-icon">📅</div><div>'
        timeline_html += '<div class="card-title">Research Timeline</div>'
        timeline_html += '<div class="card-subtitle">Historical Development</div>'
        timeline_html += '</div></div>'
        timeline_html += '<div class="timeline">'
        for item in research_timeline:
            timeline_html += (
                f'<div class="timeline-item"><div class="timeline-step">{item.get("year", "")}</div>'
                f'<div class="timeline-title">{item.get("title", "")}</div>'
                f'<div class="timeline-desc">{item.get("desc", "")}</div></div>'
            )
        timeline_html += '</div></div>'

    # Page 5: Key insights
    insights_html = ""
    if key_insights:
        insights_html += '<div class="card">'
        insights_html += '<div class="card-header"><div class="card-icon">💡</div><div>'
        insights_html += '<div class="card-title">Key Insights</div>'
        insights_html += '<div class="card-subtitle">Takeaways from Related Work</div>'
        insights_html += '</div></div>'
        for insight in key_insights:
            insights_html += f'<div class="answer-box" style="margin-top: 12px;"><p style="font-size: 15px; line-height: 1.8; color: var(--text);">{insight}</p></div>'
        insights_html += '</div>'

    pages = []
    if overview_html:
        pages.append({"id": "positioning", "title": "🎯 Positioning", "subtitle": "Research Scope", "content": overview_html})
    if compare_html:
        pages.append({"id": "comparison", "title": "📊 Method Comparison", "subtitle": "Differences", "content": compare_html})
    if papers_html:
        pages.append({"id": "papers", "title": "📄 Related Papers", "subtitle": "Literature", "content": papers_html})
    if timeline_html:
        pages.append({"id": "timeline", "title": "📅 Timeline", "subtitle": "Chronology", "content": timeline_html})
    if insights_html:
        pages.append({"id": "insights", "title": "💡 Key Insights", "subtitle": "Findings", "content": insights_html})

    if not pages:
        pages.append({"id": "empty", "title": "🔎 Related Work", "subtitle": "No content",
                      "content": '<div class="card"><p style="font-size: 15px; color: var(--text-secondary);">Provide data to generate the related work report.</p></div>'})

    html = generator.build_html(pages, "🔎 Related Work")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Related work report generated: {output_path}")
    return html


# ============================================================================
# Report 5: Method (方法报告)
# ============================================================================

def create_method_report(
    paper_title: str,
    core_idea: List[str] = None,
    prerequisites: List[Dict[str, str]] = None,
    algorithm_steps: List[Dict[str, str]] = None,
    key_techniques: List[KeyTechCard] = None,
    parameters: List[Dict[str, str]] = None,
    overall_flow: List[Dict[str, str]] = None,
    output_path: str = "method.html"
) -> str:
    """Create method analysis report"""
    generator = HTMLReportGenerator(paper_title)
    core_idea = core_idea or []
    prerequisites = prerequisites or []
    algorithm_steps = algorithm_steps or []
    key_techniques = key_techniques or []
    parameters = parameters or []
    overall_flow = overall_flow or []

    # Page 1: Core idea
    idea_html = ""
    if core_idea:
        idea_html += '<div class="card">'
        idea_html += '<div class="card-header"><div class="card-icon">💡</div><div>'
        idea_html += '<div class="card-title">Core Idea</div>'
        idea_html += '<div class="card-subtitle">Method Overview</div>'
        idea_html += '</div></div>'
        for p in core_idea:
            idea_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{p}</p>'
        idea_html += '</div>'

    if prerequisites:
        idea_html += '<div class="card">'
        idea_html += '<div class="card-header"><div class="card-icon">📚</div><div>'
        idea_html += '<div class="card-title">Prerequisites</div>'
        idea_html += '<div class="card-subtitle">Background Knowledge</div>'
        idea_html += '</div></div>'
        for prereq in prerequisites:
            title = prereq.get("title", "")
            desc = prereq.get("desc", "")
            idea_html += f'<div class="concept-card"><div class="concept-title">{title}</div><div class="concept-desc">{desc}</div></div>'
        idea_html += '</div>'

    # Page 2: Algorithm
    algo_html = ""
    if algorithm_steps:
        algo_html += '<div class="card">'
        algo_html += '<div class="card-header"><div class="card-icon">🧮</div><div>'
        algo_html += '<div class="card-title">Algorithm Steps</div>'
        algo_html += '<div class="card-subtitle">Step-by-Step Procedure</div>'
        algo_html += '</div></div>'
        for step in algorithm_steps:
            title = step.get("title", "")
            desc = step.get("desc", "")
            num = step.get("num", "")
            algo_html += f'<div class="algo-card"><div class="algo-title"><span class="algo-number">{num}</span>{title}</div><div class="algo-content">{desc}</div></div>'
        algo_html += '</div>'

    # Page 3: Key techniques
    tech_html = ""
    if key_techniques:
        tech_html += '<div class="card">'
        tech_html += '<div class="card-header"><div class="card-icon">🔧</div><div>'
        tech_html += '<div class="card-title">Key Techniques</div>'
        tech_html += '<div class="card-subtitle">Technical Details</div>'
        tech_html += '</div></div>'
        tech_html += '<div class="key-tech-grid">'
        for tech in key_techniques:
            tech_html += (
                f'<div class="key-tech-card"><div class="key-tech-icon">{tech.icon}</div>'
                f'<div class="key-tech-title">{tech.title}</div>'
                f'<div class="key-tech-desc">{tech.description}</div></div>'
            )
        tech_html += '</div></div>'

    # Page 4: Parameters
    param_html = ""
    if parameters:
        param_html += '<div class="card">'
        param_html += '<div class="card-header"><div class="card-icon">⚙️</div><div>'
        param_html += '<div class="card-title">Parameters</div>'
        param_html += '<div class="card-subtitle">Settings and Hyperparameters</div>'
        param_html += '</div></div>'
        param_html += '<div class="param-table-wrapper" style="overflow-x: auto;"><table class="param-table"><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody>'
        for param in parameters:
            name = param.get("name", "")
            desc = param.get("desc", "")
            param_html += f'<tr><td class="param-name">{name}</td><td>{desc}</td></tr>'
        param_html += '</tbody></table></div></div>'

    # Page 5: Overall flow
    flow_html = ""
    if overall_flow:
        flow_html += '<div class="card">'
        flow_html += '<div class="card-header"><div class="card-icon">🔄</div><div>'
        flow_html += '<div class="card-title">Overall Flow</div>'
        flow_html += '<div class="card-subtitle">End-to-End Process</div>'
        flow_html += '</div></div>'
        flow_html += '<div class="flow-chart">'
        for i, step in enumerate(overall_flow):
            flow_html += (
                f'<div class="flow-step"><div class="flow-node">'
                f'<span class="flow-node-number">{i + 1}</span>'
                f'<span class="flow-node-title">{step.get("title", "")}</span><br/>'
                f'<span class="flow-node-desc">{step.get("desc", "")}</span></div>'
            )
            if i < len(overall_flow) - 1:
                flow_html += '<div class="flow-arrow">↓</div>'
            flow_html += '</div>'
        flow_html += '</div></div>'

    pages = []
    if idea_html:
        pages.append({"id": "coreidea", "title": "💡 Core Idea", "subtitle": "Overview", "content": idea_html})
    if algo_html:
        pages.append({"id": "algorithm", "title": "🧮 Algorithm", "subtitle": "Steps", "content": algo_html})
    if tech_html:
        pages.append({"id": "techniques", "title": "🔧 Key Techniques", "subtitle": "Details", "content": tech_html})
    if param_html:
        pages.append({"id": "params", "title": "⚙️ Parameters", "subtitle": "Settings", "content": param_html})
    if flow_html:
        pages.append({"id": "flow", "title": "🔄 Overall Flow", "subtitle": "Process", "content": flow_html})

    if not pages:
        pages.append({"id": "empty", "title": "📐 Method", "subtitle": "No content",
                      "content": '<div class="card"><p style="font-size: 15px; color: var(--text-secondary);">Provide data to generate the method report.</p></div>'})

    html = generator.build_html(pages, "📐 Method")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Method report generated: {output_path}")
    return html


# ============================================================================
# Report 6: Experiments (实验报告)
# ============================================================================

def create_experiments_report(
    paper_title: str,
    experiment_overview: List[str] = None,
    samples: List[SampleCard] = None,
    metrics: List[MetricCard] = None,
    error_analysis: List[Dict[str, str]] = None,
    comparisons: List[Dict[str, str]] = None,
    progress_items: List[ProgressCard] = None,
    output_path: str = "experiments.html"
) -> str:
    """Create experiments analysis report"""
    generator = HTMLReportGenerator(paper_title)
    experiment_overview = experiment_overview or []
    samples = samples or []
    metrics = metrics or []
    error_analysis = error_analysis or []
    comparisons = comparisons or []
    progress_items = progress_items or []

    # Page 1: Overview
    exp_html = ""
    if experiment_overview:
        exp_html += '<div class="card">'
        exp_html += '<div class="card-header"><div class="card-icon">🎯</div><div>'
        exp_html += '<div class="card-title">Experiment Overview</div>'
        exp_html += '<div class="card-subtitle">Setup & Goals</div>'
        exp_html += '</div></div>'
        for p in experiment_overview:
            exp_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{p}</p>'
        exp_html += '</div>'

    if metrics:
        exp_html += '<div class="stats-grid">'
        for m in metrics:
            exp_html += (
                f'<div class="metric-card"><div class="metric-icon">{m.icon}</div>'
                f'<div class="metric-value">{m.value}</div>'
                f'<div class="metric-label">{m.label}</div></div>'
            )
        exp_html += '</div>'

    # Page 2: Samples / Datasets
    sample_html = ""
    if samples:
        sample_html += '<div class="card">'
        sample_html += '<div class="card-header"><div class="card-icon">📦</div><div>'
        sample_html += '<div class="card-title">Samples & Datasets</div>'
        sample_html += '<div class="card-subtitle">Test Cases</div>'
        sample_html += '</div></div>'
        sample_html += '<div class="sample-grid">'
        for s in samples:
            sample_html += f'<div class="sample-card">'
            sample_html += f'<div class="sample-image">{s.icon}</div>'
            sample_html += f'<div class="sample-info"><div class="sample-title">{s.title}</div>'
            sample_html += f'<div class="sample-desc">{s.description}</div>'
            if s.tags:
                for t in s.tags:
                    sample_html += f'<span class="sample-tag">{t}</span>'
            sample_html += '</div></div>'
        sample_html += '</div></div>'

    # Page 3: Error analysis / Results
    err_html = ""
    if error_analysis:
        err_html += '<div class="card">'
        err_html += '<div class="card-header"><div class="card-icon">📏</div><div>'
        err_html += '<div class="card-title">Accuracy & Results</div>'
        err_html += '<div class="card-subtitle">Quantitative Analysis</div>'
        err_html += '</div></div>'
        for item in error_analysis:
            title = item.get("title", "")
            desc = item.get("desc", "")
            err_html += f'<div class="answer-box" style="margin-top: 12px;"><strong style="color: var(--primary);">{title}</strong><p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-top: 8px;">{desc}</p></div>'
        err_html += '</div>'

    # Page 4: Comparisons
    comp_html = ""
    if comparisons:
        comp_html += '<div class="card">'
        comp_html += '<div class="card-header"><div class="card-icon">📊</div><div>'
        comp_html += '<div class="card-title">Comparative Analysis</div>'
        comp_html += '<div class="card-subtitle">Against Baselines</div>'
        comp_html += '</div></div>'
        comp_html += '<div class="key-tech-grid">'
        for c in comparisons:
            title = c.get("title", "")
            desc = c.get("desc", "")
            icon = c.get("icon", "📊")
            comp_html += (
                f'<div class="key-tech-card"><div class="key-tech-icon">{icon}</div>'
                f'<div class="key-tech-title">{title}</div>'
                f'<div class="key-tech-desc">{desc}</div></div>'
            )
        comp_html += '</div></div>'

    # Page 5: Progress / Discussion points
    prog_html = ""
    if progress_items:
        prog_html += '<div class="card">'
        prog_html += '<div class="card-header"><div class="card-icon">💬</div><div>'
        prog_html += '<div class="card-title">Discussion Points</div>'
        prog_html += '<div class="card-subtitle">Insights & Limitations</div>'
        prog_html += '</div></div>'
        for item in progress_items:
            prog_html += (
                f'<div class="progress-card"><div class="progress-header">'
                f'<div class="progress-title">{item.title}</div>'
                f'<div class="progress-value">{item.value}</div></div>'
                f'<div style="font-size: 13px; color: var(--text-secondary); line-height: 1.6; margin-top: 8px;">{item.percentage}</div></div>'
            )
        prog_html += '</div>'

    pages = []
    if exp_html:
        pages.append({"id": "overview", "title": "🎯 Experiment Overview", "subtitle": "Setup", "content": exp_html})
    if sample_html:
        pages.append({"id": "samples", "title": "📦 Samples", "subtitle": "Test Cases", "content": sample_html})
    if err_html:
        pages.append({"id": "results", "title": "📏 Results", "subtitle": "Quantitative", "content": err_html})
    if comp_html:
        pages.append({"id": "comparison", "title": "📊 Comparison", "subtitle": "Comparative", "content": comp_html})
    if prog_html:
        pages.append({"id": "discussion", "title": "💬 Discussion", "subtitle": "Insights", "content": prog_html})

    if not pages:
        pages.append({"id": "empty", "title": "🔬 Experiments", "subtitle": "No content",
                      "content": '<div class="card"><p style="font-size: 15px; color: var(--text-secondary);">Provide data to generate the experiments report.</p></div>'})

    html = generator.build_html(pages, "🔬 Experiments")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Experiments report generated: {output_path}")
    return html


# ============================================================================
# Report 7: Discussion & Conclusion (讨论与结论)
# ============================================================================

def create_discussion_report(
    paper_title: str,
    method_summary: List[str] = None,
    limitations: List[DiscussionCard] = None,
    comparisons: List[Dict[str, str]] = None,
    future_work: List[Dict[str, str]] = None,
    conclusions: List[str] = None,
    output_path: str = "discussion.html"
) -> str:
    """Create discussion & conclusion report"""
    generator = HTMLReportGenerator(paper_title)
    method_summary = method_summary or []
    limitations = limitations or []
    comparisons = comparisons or []
    future_work = future_work or []
    conclusions = conclusions or []

    # Page 1: Method summary
    sum_html = ""
    if method_summary:
        sum_html += '<div class="card">'
        sum_html += '<div class="card-header"><div class="card-icon">📋</div><div>'
        sum_html += '<div class="card-title">Method Summary</div>'
        sum_html += '<div class="card-subtitle">Key Takeaways</div>'
        sum_html += '</div></div>'
        for p in method_summary:
            sum_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{p}</p>'
        sum_html += '</div>'

    # Page 2: Limitations
    lim_html = ""
    if limitations:
        lim_html += '<div class="card">'
        lim_html += '<div class="card-header"><div class="card-icon">⚠️</div><div>'
        lim_html += '<div class="card-title">Limitations</div>'
        lim_html += '<div class="card-subtitle">Method Constraints</div>'
        lim_html += '</div></div>'
        for item in limitations:
            lim_html += (
                f'<div class="discussion-card"><div class="discussion-title">{item.title}</div>'
                f'<div class="discussion-content">{item.description}</div></div>'
            )
        lim_html += '</div>'

    # Page 3: Comparisons with related work
    rel_html = ""
    if comparisons:
        rel_html += '<div class="card">'
        rel_html += '<div class="card-header"><div class="card-icon">📊</div><div>'
        rel_html += '<div class="card-title">Comparison with Related Work</div>'
        rel_html += '<div class="card-subtitle">Relative Strengths</div>'
        rel_html += '</div></div>'
        rel_html += '<div class="compare-table-wrapper"><table class="compare-table"><thead><tr>'
        # Use headers from first dict keys or generic
        headers = comparisons[0].keys() if comparisons else ["Aspect", "This Work", "Others"]
        for h in headers:
            rel_html += f'<th>{h}</th>'
        rel_html += '</tr></thead><tbody>'
        for row in comparisons:
            rel_html += '<tr>'
            for h in headers:
                val = row.get(h, "")
                rel_html += f'<td>{val}</td>'
            rel_html += '</tr>'
        rel_html += '</tbody></table></div></div>'

    # Page 4: Future work
    fut_html = ""
    if future_work:
        fut_html += '<div class="card">'
        fut_html += '<div class="card-header"><div class="card-icon">🚀</div><div>'
        fut_html += '<div class="card-title">Future Work Directions</div>'
        fut_html += '<div class="card-subtitle">Research Roadmap</div>'
        fut_html += '</div></div>'
        for item in future_work:
            title = item.get("title", "")
            desc = item.get("desc", "")
            fut_html += f'<div class="concept-card"><div class="concept-title">{title}</div><div class="concept-desc">{desc}</div></div>'
        fut_html += '</div>'

    # Page 5: Conclusions
    concl_html = ""
    if conclusions:
        concl_html += '<div class="card">'
        concl_html += '<div class="card-header"><div class="card-icon">🎯</div><div>'
        concl_html += '<div class="card-title">Conclusion</div>'
        concl_html += '<div class="card-subtitle">Final Takeaways</div>'
        concl_html += '</div></div>'
        for p in conclusions:
            concl_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{p}</p>'
        concl_html += '</div>'

    pages = []
    if sum_html:
        pages.append({"id": "summary", "title": "📋 Method Summary", "subtitle": "Summary", "content": sum_html})
    if lim_html:
        pages.append({"id": "limitations", "title": "⚠️ Limitations", "subtitle": "Constraints", "content": lim_html})
    if rel_html:
        pages.append({"id": "comparison", "title": "📊 Comparison", "subtitle": "Related Work", "content": rel_html})
    if fut_html:
        pages.append({"id": "future", "title": "🚀 Future Work", "subtitle": "Roadmap", "content": fut_html})
    if concl_html:
        pages.append({"id": "conclusion", "title": "🎯 Conclusion", "subtitle": "Takeaways", "content": concl_html})

    if not pages:
        pages.append({"id": "empty", "title": "💬 Discussion", "subtitle": "No content",
                      "content": '<div class="card"><p style="font-size: 15px; color: var(--text-secondary);">Provide data to generate the discussion report.</p></div>'})

    html = generator.build_html(pages, "💬 Discussion & Conclusion")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Discussion report generated: {output_path}")
    return html


# ============================================================================
# Report 8: Extended Reading (延伸阅读推荐)
# ============================================================================

def create_extended_reading_report(
    paper_title: str,
    classic_papers: List[ExtendedPaper] = None,
    follow_up_papers: List[ExtendedPaper] = None,
    complementary_papers: List[ExtendedPaper] = None,
    application_papers: List[ExtendedPaper] = None,
    reviews_and_tutorials: List[ExtendedPaper] = None,
    output_path: str = "extended_reading.html"
) -> str:
    """Create extended reading recommendations report"""
    generator = HTMLReportGenerator(paper_title)
    classic_papers = classic_papers or []
    follow_up_papers = follow_up_papers or []
    complementary_papers = complementary_papers or []
    application_papers = application_papers or []
    reviews_and_tutorials = reviews_and_tutorials or []

    def render_paper_group(group_title: str, group_icon: str, group_color: str, papers: List[ExtendedPaper]) -> str:
        if not papers:
            return ""
        html_out = '<div class="card">'
        html_out += (
            f'<div class="group-header"><div class="group-icon {group_color}">{group_icon}</div>'
            f'<div class="group-title">{group_title}</div></div>'
        )
        for paper in papers:
            html_out += (
                f'<div style="padding: 16px; background: var(--bg-secondary); border-radius: 10px; margin-bottom: 12px; border-left: 4px solid var(--primary);">'
                f'<div style="font-size: 15px; font-weight: 600; color: var(--text); margin-bottom: 6px;">{paper.title}</div>'
            )
            if paper.meta:
                html_out += f'<div style="font-size: 12px; color: var(--text-secondary); margin-bottom: 8px;">{paper.meta}</div>'
            if paper.description:
                html_out += f'<div style="font-size: 13px; line-height: 1.6; color: var(--text-secondary); margin-bottom: 8px;">{paper.description}</div>'
            if paper.tags:
                for tag in paper.tags:
                    html_out += f'<span class="sample-tag" style="margin-right: 6px;">{tag}</span>'
            if paper.doi_url:
                html_out += f'<div style="margin-top: 10px;"><a href="{paper.doi_url}" target="_blank" style="font-size: 12px; color: var(--primary);">📖 Read: {paper.doi_url}</a></div>'
            html_out += '</div>'
        html_out += '</div>'
        return html_out

    pages = []

    classic_html = render_paper_group("Classic & Foundational Papers", "🏛️", "blue", classic_papers)
    follow_html = render_paper_group("Same Group / Follow-Up Work", "🔗", "green", follow_up_papers)
    comp_html = render_paper_group("Complementary Methods", "🤝", "purple", complementary_papers)
    app_html = render_paper_group("Applications & Use Cases", "🏗️", "orange", application_papers)
    rev_html = render_paper_group("Reviews & Tutorials", "📚", "blue", reviews_and_tutorials)

    if classic_html:
        pages.append({"id": "classic", "title": "🏛️ Classic Papers", "subtitle": "Foundations", "content": classic_html})
    if follow_html:
        pages.append({"id": "followup", "title": "🔗 Follow-Up Work", "subtitle": "Extensions", "content": follow_html})
    if comp_html:
        pages.append({"id": "complementary", "title": "🤝 Complementary", "subtitle": "Other Methods", "content": comp_html})
    if app_html:
        pages.append({"id": "applications", "title": "🏗️ Applications", "subtitle": "Use Cases", "content": app_html})
    if rev_html:
        pages.append({"id": "reviews", "title": "📚 Reviews", "subtitle": "Tutorials", "content": rev_html})

    if not pages:
        pages.append({"id": "empty", "title": "🔍 Extended Reading", "subtitle": "No content",
                      "content": '<div class="card"><p style="font-size: 15px; color: var(--text-secondary);">Provide data to generate the extended reading report.</p></div>'})

    html = generator.build_html(pages, "🔍 Extended Reading")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Extended reading report generated: {output_path}")
    return html


# ============================================================================
# Report 9: Paper Search by Topic (领域论文搜索)
# ============================================================================

@dataclass
class SearchPaper:
    """Search result paper entry"""
    title: str
    authors: str = ""
    year: str = ""
    venue: str = ""
    summary: str = ""
    tags: List[str] = field(default_factory=list)
    doi_url: str = ""


def create_paper_search_report(
    research_topic: str,
    topic_description: str = "",
    category_tags: List[Dict[str, str]] = None,
    paper_groups: List[Dict[str, str]] = None,
    output_path: str = "paper_search.html"
) -> str:
    """Create a paper search & recommendation report based on research topic"""
    generator = HTMLReportGenerator(research_topic)
    category_tags = category_tags or []
    paper_groups = paper_groups or []

    # Page 1: Topic overview
    topic_html = ""
    if research_topic or topic_description:
        topic_html += '<div class="card positioning-card">'
        topic_html += '<div class="card-header"><div class="card-icon">🔍</div><div>'
        topic_html += f'<div class="card-title">{research_topic or "研究主题"}</div>'
        topic_html += '<div class="card-subtitle">主题概述</div>'
        topic_html += '</div></div>'
        if topic_description:
            topic_html += f'<p style="font-size: 15px; line-height: 1.8; color: var(--text); margin-bottom: 16px;">{topic_description}</p>'
        topic_html += '</div>'

    if category_tags:
        topic_html += '<div class="card">'
        topic_html += '<div class="card-header"><div class="card-icon">🏷️</div><div>'
        topic_html += '<div class="card-title">研究范畴标签</div>'
        topic_html += '<div class="card-subtitle">关键主题</div>'
        topic_html += '</div></div><div>'
        for tag in category_tags:
            color = tag.get("color", "blue")
            topic_html += f'<span class="category-tag {color}">{tag.get("label", "")}</span>'
        topic_html += '</div></div>'

    # Page 2-N: Paper groups (each group is a page)
    pages = []
    if topic_html:
        pages.append({"id": "topic", "title": "🔍 主题概览", "subtitle": "研究范围", "content": topic_html})

    for gi, group in enumerate(paper_groups):
        group_title = group.get("group_title", "论文")
        group_icon = group.get("group_icon", "📄")
        group_color = group.get("group_color", "blue")
        group_desc = group.get("group_desc", "")
        papers = group.get("papers", [])

        if not papers:
            continue

        group_html = ""
        if group_desc:
            group_html += '<div class="card">'
            group_html += '<div class="card-header"><div class="card-icon">' + group_icon + '</div><div>'
            group_html += f'<div class="card-title">{group_title}</div>'
            group_html += f'<div class="card-subtitle">{group_desc}</div>'
            group_html += '</div></div></div>'

        group_html += '<div class="card">'
        group_html += (
            f'<div class="group-header"><div class="group-icon {group_color}">{group_icon}</div>'
            f'<div class="group-title">{group_title}</div></div>'
        )

        for paper in papers:
            group_html += (
                f'<div style="padding: 20px; background: var(--bg-secondary); border-radius: 12px; margin-bottom: 16px; border-left: 4px solid var(--primary);">'
            )
            group_html += f'<div style="font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 8px;">{paper.title}</div>'
            meta_parts = []
            if paper.authors:
                meta_parts.append(paper.authors)
            if paper.year:
                meta_parts.append(paper.year)
            if paper.venue:
                meta_parts.append(paper.venue)
            if meta_parts:
                group_html += f'<div style="font-size: 12px; color: var(--text-secondary); margin-bottom: 10px;">{" · ".join(meta_parts)}</div>'
            if paper.summary:
                group_html += f'<div style="font-size: 13px; line-height: 1.7; color: var(--text-secondary); margin-bottom: 10px;">{paper.summary}</div>'
            if paper.tags:
                for tag in paper.tags:
                    group_html += f'<span class="sample-tag" style="margin-right: 6px; margin-bottom: 6px;">{tag}</span>'
            if paper.doi_url:
                group_html += f'<div style="margin-top: 10px;"><a href="{paper.doi_url}" target="_blank" style="font-size: 12px; color: var(--primary);">📖 免费阅读：{paper.doi_url}</a></div>'
            group_html += '</div>'
        group_html += '</div>'

        page_id = f"group{gi}"
        pages.append({"id": page_id, "title": f"{group_icon} {group_title}", "subtitle": "推荐论文", "content": group_html})

    if not pages:
        pages.append({"id": "empty", "title": "🔍 论文搜索", "subtitle": "无内容",
                      "content": '<div class="card"><p style="font-size: 15px; color: var(--text-secondary);">请提供数据以生成论文搜索报告。</p></div>'})

    html = generator.build_html(pages, "📚 论文搜索")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Paper search report generated: {output_path}")
    return html