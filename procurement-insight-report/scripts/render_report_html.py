#!/usr/bin/env python3
"""Render a Procurement MCP report JSON payload into an HTML report."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


BG = "#f7f4ee"
PANEL = "#fffdf8"
INK = "#1f2933"
MUTED = "#5b6773"
LINE = "#e2d9cc"
ACCENT = "#0f766e"
ACCENT_SOFT = "#dff5f2"
CONFIDENCE_STYLES = {
    "high": ("#dcfce7", "#166534"),
    "mixed": ("#fef3c7", "#b45309"),
    "low": ("#fee2e2", "#b91c1c"),
}


def load_report(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def esc(value: object) -> str:
    return html.escape("" if value is None else str(value))


def render_list(items: list[str]) -> str:
    if not items:
        return "<p>No items provided.</p>"
    return "<ul>" + "".join(f"<li>{esc(item)}</li>" for item in items) + "</ul>"


def render_kpis(kpis: list[dict]) -> str:
    cards = []
    for item in kpis:
        cards.append(
            "<div class='card'>"
            f"<div class='label'>{esc(item.get('label', 'Metric'))}</div>"
            f"<div class='value'>{esc(item.get('value', ''))}</div>"
            "</div>"
        )
    return "<section class='grid'>" + "".join(cards) + "</section>" if cards else ""


def bar_chart_svg(series: list[dict], width: int = 720, height: int = 280) -> str:
    if not series:
        return "<div class='chart-empty'>No chart data.</div>"
    max_value = max(float(item.get("value", 0) or 0) for item in series) or 1.0
    left_pad = 140
    right_pad = 24
    top_pad = 20
    row_gap = 16
    bar_height = 18
    usable_width = width - left_pad - right_pad
    total_height = top_pad + len(series) * (bar_height + row_gap) + 20
    svg_height = max(height, total_height)
    rows = []
    for index, item in enumerate(series):
        label = esc(item.get("label", ""))
        value = float(item.get("value", 0) or 0)
        y = top_pad + index * (bar_height + row_gap)
        bar_width = usable_width * (value / max_value)
        rows.append(
            f"<text x='0' y='{y + 14}' fill='{MUTED}' font-size='13'>{label}</text>"
            f"<rect x='{left_pad}' y='{y}' width='{usable_width}' height='{bar_height}' rx='8' fill='{ACCENT_SOFT}' />"
            f"<rect x='{left_pad}' y='{y}' width='{bar_width:.2f}' height='{bar_height}' rx='8' fill='{ACCENT}' />"
            f"<text x='{left_pad + bar_width + 8:.2f}' y='{y + 14}' fill='{INK}' font-size='13'>{int(value) if value.is_integer() else value}</text>"
        )
    return (
        f"<svg viewBox='0 0 {width} {svg_height}' class='chart-svg' role='img' aria-label='Bar chart'>"
        + "".join(rows)
        + "</svg>"
    )


def line_chart_svg(series: list[dict], width: int = 720, height: int = 280) -> str:
    if not series:
        return "<div class='chart-empty'>No chart data.</div>"
    values = [float(item.get("value", 0) or 0) for item in series]
    max_value = max(values) or 1.0
    min_value = min(values)
    left_pad, right_pad, top_pad, bottom_pad = 40, 20, 20, 40
    usable_width = width - left_pad - right_pad
    usable_height = height - top_pad - bottom_pad
    step_x = usable_width if len(series) == 1 else usable_width / (len(series) - 1)
    points = []
    labels = []
    for index, item in enumerate(series):
        value = values[index]
        label = esc(item.get("label", ""))
        norm = 0 if max_value == min_value else (value - min_value) / (max_value - min_value)
        x = left_pad + index * step_x
        y = top_pad + usable_height - norm * usable_height
        points.append(f"{x:.2f},{y:.2f}")
        labels.append(f"<text x='{x:.2f}' y='{height - 14}' text-anchor='middle' fill='{MUTED}' font-size='12'>{label}</text>")
        labels.append(f"<circle cx='{x:.2f}' cy='{y:.2f}' r='4' fill='{ACCENT}' />")
        labels.append(f"<text x='{x:.2f}' y='{y - 10:.2f}' text-anchor='middle' fill='{INK}' font-size='12'>{int(value) if value.is_integer() else value}</text>")
    return (
        f"<svg viewBox='0 0 {width} {height}' class='chart-svg' role='img' aria-label='Line chart'>"
        f"<line x1='{left_pad}' y1='{height - bottom_pad}' x2='{width - right_pad}' y2='{height - bottom_pad}' stroke='{LINE}' stroke-width='1' />"
        f"<line x1='{left_pad}' y1='{top_pad}' x2='{left_pad}' y2='{height - bottom_pad}' stroke='{LINE}' stroke-width='1' />"
        f"<polyline fill='none' stroke='{ACCENT}' stroke-width='3' points='{' '.join(points)}' />"
        + "".join(labels)
        + "</svg>"
    )


def render_chart(chart: dict) -> str:
    title = esc(chart.get("title", "Chart"))
    chart_type = chart.get("type", "bar")
    series = chart.get("series", [])
    graphic = line_chart_svg(series) if chart_type == "line" else bar_chart_svg(series)
    return f"<section class='panel'><h2>{title}</h2>{graphic}</section>"


def build_html(report: dict) -> str:
    confidence = str(report.get("confidence", "mixed")).lower()
    confidence_bg, confidence_fg = CONFIDENCE_STYLES.get(confidence, CONFIDENCE_STYLES["mixed"])
    title = esc(report.get("title", "Procurement Report"))
    subtitle = esc(report.get("subtitle", ""))
    reporting_window = esc(report.get("reporting_window", ""))
    charts = report.get("charts", [])
    chart_html = "".join(render_chart(chart) for chart in charts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <style>
    :root {{
      --bg: {BG};
      --panel: {PANEL};
      --ink: {INK};
      --muted: {MUTED};
      --line: {LINE};
      --accent: {ACCENT};
      --accent-soft: {ACCENT_SOFT};
      --confidence-bg: {confidence_bg};
      --confidence-fg: {confidence_fg};
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: "Segoe UI", Arial, sans-serif; background: linear-gradient(180deg, #faf7f1 0%, #f3ede2 100%); color: var(--ink); }}
    .wrap {{ max-width: 1180px; margin: 0 auto; padding: 32px 20px 48px; }}
    .hero, .panel {{ background: var(--panel); border: 1px solid var(--line); border-radius: 18px; box-shadow: 0 10px 30px rgba(31, 41, 51, 0.05); }}
    .hero {{ padding: 28px; margin-bottom: 20px; }}
    .eyebrow {{ display: inline-block; padding: 6px 10px; border-radius: 999px; background: var(--accent-soft); color: var(--accent); font-size: 12px; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; }}
    .confidence {{ display: inline-block; padding: 6px 10px; border-radius: 999px; background: var(--confidence-bg); color: var(--confidence-fg); font-size: 12px; font-weight: 700; text-transform: capitalize; }}
    h1, h2, h3 {{ margin: 0 0 10px; }}
    p {{ margin: 0 0 10px; color: var(--muted); line-height: 1.5; }}
    .grid {{ display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); margin: 20px 0; }}
    .card, .panel {{ padding: 18px; }}
    .card {{ border: 1px solid var(--line); border-radius: 16px; background: #fff; }}
    .label {{ font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--muted); margin-bottom: 8px; }}
    .value {{ font-size: 32px; font-weight: 700; color: var(--ink); }}
    .layout {{ display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }}
    .chart-svg {{ width: 100%; height: auto; display: block; }}
    ul {{ margin: 0; padding-left: 18px; color: var(--ink); }}
    li {{ margin-bottom: 10px; line-height: 1.5; }}
    .section-stack {{ display: grid; gap: 20px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <span class="eyebrow">Procurement Report</span>
      <h1>{title}</h1>
      {f"<p>{subtitle}</p>" if subtitle else ""}
      <p><strong>Reporting window:</strong> {reporting_window}</p>
      <p><strong>Confidence:</strong> <span class="confidence">{esc(confidence)}</span></p>
      {render_list(report.get("summary", []))}
    </section>
    {render_kpis(report.get("kpis", []))}
    <section class="layout">
      <div class="section-stack">
        {chart_html}
        <section class="panel"><h2>Facts</h2>{render_list(report.get("facts", []))}</section>
      </div>
      <div class="section-stack">
        <section class="panel"><h2>Insights</h2>{render_list(report.get("insights", []))}</section>
        <section class="panel"><h2>Recommended Actions</h2>{render_list(report.get("recommended_actions", []))}</section>
        <section class="panel"><h2>Confidence and Caveats</h2>{render_list(report.get("caveats", []))}</section>
      </div>
    </section>
  </div>
</body>
</html>
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path, help="Path to the normalized report JSON file.")
    parser.add_argument("output_html", type=Path, help="Path to write the rendered HTML report.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = load_report(args.input_json)
    args.output_html.write_text(build_html(report), encoding="utf-8")
    print(f"Rendered HTML report to {args.output_html}")


if __name__ == "__main__":
    main()
