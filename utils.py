"""
utils.py
Utility functions for console formatting, tables, dividers, and AI service health checks.
Experiment 4: Personalized Recommendation System
"""

import json
import urllib.request
import urllib.error


def print_header(title: str) -> None:
    """Print a visually distinctive section header."""
    box_width = 65
    print("\n" + "=" * box_width)
    print(f" {title.upper()} ".center(box_width, "="))
    print("=" * box_width + "\n")


def print_section(title: str) -> None:
    """Print a sub-section title."""
    print(f"\n--- {title} ---")


def print_divider() -> None:
    """Print a horizontal divider."""
    print("-" * 65)


def format_table(headers: list, rows: list) -> str:
    """
    Format headers and rows into a clean ASCII table.
    """
    if not rows:
        return "No data available."

    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))

    header_str = " | ".join(f"{str(h):<{col_widths[i]}}" for i, h in enumerate(headers))
    sep_str = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

    row_strs = []
    for row in rows:
        row_strs.append(" | ".join(f"{str(cell):<{col_widths[i]}}" for i, cell in enumerate(row)))

    return f"{header_str}\n{sep_str}\n" + "\n".join(row_strs)


def check_ollama_status(host: str = "http://localhost:11434") -> dict:
    """
    Check if the local Ollama instance is active and retrieve available models.
    """
    try:
        url = f"{host.rstrip('/')}/api/tags"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=2) as response:
            data = json.loads(response.read().decode())
            models = [m.get("name") for m in data.get("models", [])]
            return {"status": "connected", "online": True, "models": models}
    except Exception:
        return {"status": "offline", "online": False, "models": []}
