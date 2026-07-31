"""
Validate AGI Architecture Research packet (Bounty #5).

Checks:
- All expected files exist
- CSV is parseable and consistent
- Raw outputs follow expected structure
- README cross-references are valid
"""
import csv
import os
from pathlib import Path


RESEARCH_DIR = Path(__file__).parent.parent / "research" / "ai_generated_agi_architectures"
RAW_OUTPUTS_DIR = RESEARCH_DIR / "raw_outputs"


def test_research_dir_exists():
    """The research directory must exist."""
    assert RESEARCH_DIR.is_dir(), f"Missing: {RESEARCH_DIR}"


def test_readme_exists():
    """README.md is the entry point."""
    assert (RESEARCH_DIR / "README.md").is_file(), "Missing README.md"


def test_prompts_exists():
    """prompts.md documents methodology."""
    assert (RESEARCH_DIR / "prompts.md").is_file(), "Missing prompts.md"


def test_summary_exists():
    """summary.md contains synthesis."""
    assert (RESEARCH_DIR / "summary.md").is_file(), "Missing summary.md"


def test_synthesis_exists():
    """synthesis.md contains combined architecture."""
    assert (RESEARCH_DIR / "synthesis.md").is_file(), "Missing synthesis.md"


def test_sources_exists():
    """sources.md documents provenance."""
    assert (RESEARCH_DIR / "sources.md").is_file(), "Missing sources.md"


def test_comparison_csv_exists():
    """comparison.csv provides structured data."""
    assert (RESEARCH_DIR / "comparison.csv").is_file(), "Missing comparison.csv"


def test_executive_summary_exists():
    """EXECUTIVE_SUMMARY.md for evaluators."""
    assert (RESEARCH_DIR / "EXECUTIVE_SUMMARY.md").is_file(), "Missing EXECUTIVE_SUMMARY.md"


# Wave 1 raw outputs (from ereezyy)
WAVE1_FILES = [
    "deepseek-v4-pro.md",
    "grok-3-mini.md",
    "llama-3.3-70b-versatile.md",
    "llama3.2_1b.md",
    "claude-brain-system.md",
]

# Wave 2 raw outputs (our original)
WAVE2_FILES = [
    "gpt4o.md",
    "claude_sonnet.md",
    "gemini_pro.md",
    "grok2.md",
    "deepseek_v3.md",
    "llama3_405b.md",
    "mistral_large2.md",
    "qwen25.md",
    "perplexity.md",
    "claude_opus.md",
]

ALL_RAW_FILES = WAVE1_FILES + WAVE2_FILES


def test_all_wave1_raw_outputs_exist():
    """All Wave 1 (ereezyy) raw outputs present."""
    for fname in WAVE1_FILES:
        path = RAW_OUTPUTS_DIR / fname
        assert path.is_file(), f"Missing Wave 1 file: {fname}"


def test_all_wave2_raw_outputs_exist():
    """All Wave 2 (our original) raw outputs present."""
    for fname in WAVE2_FILES:
        path = RAW_OUTPUTS_DIR / fname
        assert path.is_file(), f"Missing Wave 2 file: {fname}"


def test_raw_outputs_have_content():
    """Every raw output must have meaningful content (not empty)."""
    for fname in ALL_RAW_FILES:
        path = RAW_OUTPUTS_DIR / fname
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            assert len(content) > 200, f"Too short: {fname} ({len(content)} chars)"


def test_comparison_csv_parseable():
    """CSV must be parseable with correct column counts."""
    csv_path = RESEARCH_DIR / "comparison.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Find Wave 2 section (first non-comment line)
    wave2_start = None
    wave1_start = None
    for i, row in enumerate(rows):
        if row and row[0].startswith("System"):
            wave2_start = i
        if row and row[0].startswith("Dimension"):
            wave1_start = i
        if row and row[0].startswith("Architecture Name"):
            wave1_data_start = i
            break

    assert wave2_start is not None, "Missing Wave 2 CSV header"
    assert wave1_start is not None, "Missing Wave 1 CSV header"

    # Count Wave 2 systems (should be 10)
    wave2_systems = 0
    for i in range(wave2_start + 1, len(rows)):
        row = rows[i]
        if not row or not row[0] or row[0].startswith("#") or row[0].startswith("Dimension"):
            break
        wave2_systems += 1
    assert wave2_systems == 10, f"Expected 10 Wave 2 systems, got {wave2_systems}"

    # Count Wave 1 dimensions (should be ~36)
    wave1_dims = 0
    for i in range(wave1_data_start + 1, len(rows)):
        row = rows[i]
        if not row or not row[0]:
            break
        wave1_dims += 1
    assert wave1_dims >= 29, f"Expected 29+ Wave 1 dimensions, got {wave1_dims}"


def test_readme_cross_references():
    """README links should point to existing files."""
    readme = (RESEARCH_DIR / "README.md").read_text(encoding="utf-8")
    # Check key files are referenced
    assert "prompts.md" in readme.lower()
    assert "summary.md" in readme.lower()
    assert "comparison.csv" in readme.lower()
    assert "synthesis.md" in readme.lower()
    assert "sources.md" in readme.lower()
    assert "executive" in readme.lower()


def test_summary_mentions_15_systems():
    """Summary should mention 15 systems."""
    summary = (RESEARCH_DIR / "summary.md").read_text(encoding="utf-8")
    assert "15" in summary, "Summary should mention 15 systems"


def test_total_raw_outputs_count():
    """Exactly 15 raw output files."""
    raw_files = list(RAW_OUTPUTS_DIR.glob("*.md"))
    assert len(raw_files) == 15, f"Expected 15 raw outputs, got {len(raw_files)}"


def test_no_empty_files():
    """No files in the research dir should be empty."""
    for md_file in RESEARCH_DIR.glob("*.md"):
        size = md_file.stat().st_size
        assert size > 100, f"File too small: {md_file.name} ({size} bytes)"
    for csv_file in RESEARCH_DIR.glob("*.csv"):
        size = csv_file.stat().st_size
        assert size > 100, f"File too small: {csv_file.name} ({size} bytes)"


def test_synthesis_has_architecture_sections():
    """synthesis.md should describe a combined architecture."""
    synthesis = (RESEARCH_DIR / "synthesis.md").read_text(encoding="utf-8")
    key_sections = ["memory", "architecture", "safety", "learning"]
    for section in key_sections:
        assert section in synthesis.lower(), f"synthesis.md missing '{section}' section"
