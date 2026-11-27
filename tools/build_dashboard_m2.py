"""Collect the facts of milestone 2 and write them into the M2 dashboard.

The dashboard (docs/dashboard/neo_helper_M2.html) has two parts:
- texts written by hand, in Italian, English and Spanish (what each module is
  for, findings, decisions);
- facts collected by this script from the code, the tests, the data folder and
  git: modules, functions, links between modules, commands, test results,
  data on disk, counts.

The facts are replaced inside the HTML file, between the FACTS markers, so the
dashboard always shows the code as it is. Run it after every work package:

    UV_PROJECT_ENVIRONMENT="$HOME/.venvs/neo-helper-ml" \\
        uv run --project ml python tools/build_dashboard_m2.py

It runs the whole test suite (about 10 seconds) and reads the data folder.
Paths in the home folder are written as "~/..." so no personal path is stored.
"""

from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree

import pandas as pd
from neo import paths
from neo.data import artifacts, registry, split

ROOT = Path(__file__).resolve().parents[1]
ML = ROOT / "ml"
DASHBOARD = ROOT / "docs" / "dashboard" / "neo_helper_M2.html"
START = "/*FACTS-START*/"
END = "/*FACTS-END*/"
HOME = str(Path.home())


def tilde(path: Path | str) -> str:
    """Write a path inside the home folder as ~/..., never with the user name."""
    text = str(path)
    return "~" + text[len(HOME) :] if text.startswith(HOME) else text


def first_paragraph(docstring: str | None) -> str:
    if not docstring:
        return ""
    return " ".join(docstring.strip().split("\n\n")[0].split())


def module_name(path: Path) -> str:
    parts = path.relative_to(ML).with_suffix("").parts
    return ".".join(p for p in parts if p != "__init__")


def neo_imports(tree: ast.AST, known: set[str]) -> list[str]:
    """Names of the neo modules imported anywhere in ``tree``."""
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module and node.module.startswith("neo"):
            for alias in node.names:
                candidate = f"{node.module}.{alias.name}"
                found.add(candidate if candidate in known else node.module)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.startswith("neo"):
                    found.add(alias.name)
    return sorted(m for m in found if m in known and m != "neo")


def describe_functions(tree: ast.Module) -> list[dict]:
    items = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef | ast.ClassDef):
            if isinstance(node, ast.FunctionDef):
                signature = f"{node.name}({ast.unparse(node.args)})"
                kind = "function"
            else:
                signature = node.name
                kind = "class"
            items.append(
                {
                    "name": node.name,
                    "kind": kind,
                    "signature": signature,
                    "doc": first_paragraph(ast.get_docstring(node)),
                    "line": node.lineno,
                    "private": node.name.startswith("_"),
                }
            )
    return items


def cli_commands(tree: ast.Module) -> list[dict]:
    commands = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "add_parser"
            and node.args
            and isinstance(node.args[0], ast.Constant)
        ):
            help_text = next((k.value.value for k in node.keywords if k.arg == "help"), "")
            commands.append({"name": node.args[0].value, "help": help_text})
    return commands


def collect_code() -> dict:
    files = sorted((ML / "neo").rglob("*.py"))
    known = {module_name(f) for f in files}
    modules = []
    for path in files:
        source = path.read_text()
        tree = ast.parse(source)
        lines = [line for line in source.splitlines() if line.strip()]
        modules.append(
            {
                "name": module_name(path),
                "file": path.relative_to(ROOT).as_posix(),
                "lines": len(lines),
                "doc": first_paragraph(ast.get_docstring(tree)),
                "functions": describe_functions(tree),
                "imports": neo_imports(tree, known),
                "commands": cli_commands(tree) if path.name == "cli.py" else [],
            }
        )
    scripts = {}
    pyproject = (ML / "pyproject.toml").read_text()
    block = pyproject.split("[project.scripts]")[1].split("\n[")[0]
    for name, target in re.findall(r'^([\w-]+)\s*=\s*"([^"]+)"', block, re.MULTILINE):
        scripts[name] = target
    notebooks = []
    for path in sorted((ML / "notebooks").glob("*.ipynb")):
        cells = json.loads(path.read_text())["cells"]
        code = "\n".join("".join(c["source"]) for c in cells if c["cell_type"] == "code")
        clean = "\n".join(line for line in code.splitlines() if not line.startswith(("%", "!")))
        notebooks.append(
            {
                "file": path.relative_to(ROOT).as_posix(),
                "cells": len(cells),
                "imports": neo_imports(ast.parse(clean), known),
            }
        )
    return {"modules": modules, "scripts": scripts, "notebooks": notebooks, "known": sorted(known)}


def collect_tests(known: set[str]) -> dict:
    files = {}
    for path in sorted((ML / "tests").glob("test_*.py")):
        tree = ast.parse(path.read_text())
        files[path.name] = {
            "file": path.relative_to(ROOT).as_posix(),
            "doc": first_paragraph(ast.get_docstring(tree)),
            "imports": neo_imports(tree, known),
            "tests": [],
        }
    with tempfile.TemporaryDirectory() as folder:
        report = Path(folder) / "report.xml"
        run = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "ml/tests",
                f"--junitxml={report}",
                "-q",
                "-p",
                "no:cacheprovider",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            env={**os.environ, "MPLBACKEND": "Agg"},
        )
        root = ElementTree.parse(report).getroot()
    suite = root if root.tag == "testsuite" else root.find("testsuite")
    for case in suite.iter("testcase"):
        file_name = case.get("classname", "").split(".")[-1] + ".py"
        status = "passed"
        message = ""
        for tag in ("failure", "error", "skipped"):
            element = case.find(tag)
            if element is not None:
                status = "failed" if tag in ("failure", "error") else "skipped"
                message = (element.get("message") or "").split("\n")[0][:200]
        files.setdefault(file_name, {"file": "", "doc": "", "imports": [], "tests": []})
        files[file_name]["tests"].append(
            {
                "name": case.get("name"),
                "status": status,
                "seconds": round(float(case.get("time", 0)), 3),
                "message": message,
            }
        )
    totals = {
        s: sum(t["status"] == s for f in files.values() for t in f["tests"])
        for s in ("passed", "failed", "skipped")
    }
    return {
        "files": files,
        "totals": totals,
        "seconds": round(float(suite.get("time", 0)), 1),
        "exit_code": run.returncode,
    }


def folder_size(path: Path) -> tuple[int, int]:
    total, count = 0, 0
    for directory, _, names in os.walk(path):
        for name in names:
            total += (Path(directory) / name).stat().st_size
            count += 1
    return total, count


def collect_data() -> dict:
    root = paths.data_dir()
    places = []
    for group in ("raw", "weights", "registry", "embeddings"):
        base = root / group
        if not base.exists():
            continue
        for item in sorted(base.iterdir()):
            if item.name.startswith("."):
                continue
            size, count = folder_size(item) if item.is_dir() else (item.stat().st_size, 1)
            places.append(
                {"path": f"{group}/{item.name}", "bytes": size, "files": count, "dir": item.is_dir()}
            )
    total, _ = folder_size(root) if root.exists() else (0, 0)
    facts = {"root": tilde(root), "total_bytes": total, "places": places}

    frame = registry.load("ham10000")
    facts["ham10000"] = {
        "images": len(frame),
        "lesions": int(frame["lesion_id"].nunique()),
        "malignant": int(frame["malignant"].sum()),
        "classes": frame["diagnosis"].value_counts().to_dict(),
        "centres": frame["centre"].value_counts().to_dict(),
        "label_source": frame["label_source"].value_counts().to_dict(),
        "images_per_lesion": {
            str(k): int(v) for k, v in frame.groupby("lesion_id").size().value_counts().sort_index().items()
        },
        "columns": len(frame.columns),
    }
    parts = split.load("ham10000").merge(frame[["uid", "diagnosis", "malignant"]], on="uid")
    facts["split"] = {
        "file": split.split_path("ham10000").relative_to(ROOT).as_posix(),
        "images": parts["split"].value_counts().to_dict(),
        "lesions": parts.groupby("split")["lesion_id"].nunique().to_dict(),
        "malignant_share": parts.groupby("split")["malignant"].mean().round(4).to_dict(),
        "by_class": pd.crosstab(parts["diagnosis"], parts["split"]).to_dict(orient="index"),
    }
    duplicates_file = paths.subdir("registry") / "ham10000_duplicates.csv"
    if duplicates_file.is_file():
        pairs = pd.read_csv(duplicates_file)
        facts["duplicates"] = {
            "pairs": len(pairs),
            "exact": int(pairs["exact"].sum()),
            "across_lesions": int((~pairs["same_lesion"]).sum()),
        }
    scores_file = paths.subdir("registry") / "ham10000_artifact_scores.csv"
    if scores_file.is_file():
        audit = frame.merge(pd.read_csv(scores_file), on="uid")
        audit["dark"] = audit["dark_corners_pixels"] > artifacts.DEFAULT_THRESHOLD
        audit["hairy"] = audit["hair"] >= 0.7
        facts["artifacts"] = {
            "threshold": artifacts.DEFAULT_THRESHOLD,
            "dark_total": int(audit["dark"].sum()),
            "dark_by_class": audit.groupby("diagnosis")["dark"].mean().round(4).to_dict(),
            "dark_by_centre": audit.groupby("centre")["dark"].mean().round(4).to_dict(),
            "dark_by_malignant": {
                str(k): v for k, v in audit.groupby("malignant")["dark"].mean().round(4).items()
            },
            "hair_by_malignant": {
                str(k): v for k, v in audit.groupby("malignant")["hairy"].mean().round(4).items()
            },
        }
    return facts


def collect_git() -> dict:
    remote = subprocess.run(
        ["git", "remote", "get-url", "origin"], check=False, cwd=ROOT, capture_output=True, text=True
    ).stdout.strip()
    remote = re.sub(r"\.git$", "", remote.replace("git@github.com:", "https://github.com/"))
    log = subprocess.run(
        ["git", "log", "--date=short", "--pretty=format:%h|%ad|%s"],
        check=False,
        cwd=ROOT,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    commits = [dict(zip(("hash", "date", "subject"), line.split("|", 2), strict=True)) for line in log]
    unpushed = subprocess.run(
        ["git", "log", "--pretty=format:%h", "@{u}..HEAD"],
        check=False,
        cwd=ROOT,
        capture_output=True,
        text=True,
    ).stdout.split()
    return {
        "remote": remote,
        "commits": [c for c in commits if c["subject"].startswith("M2")],
        "unpushed": unpushed,
    }


def main() -> int:
    code = collect_code()
    facts = {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "code": code,
        "tests": collect_tests(set(code["known"])),
        "data": collect_data(),
        "git": collect_git(),
        "figures": sorted(p.name for p in (ROOT / "docs" / "figures").glob("eda_*.png")),
    }
    payload = json.dumps(facts, ensure_ascii=False, separators=(",", ":"), default=str).replace("</", "<\\/")
    html = DASHBOARD.read_text()
    if START not in html or END not in html:
        raise SystemExit(f"Markers {START} and {END} not found in {DASHBOARD}")
    before, rest = html.split(START, 1)
    _, after = rest.split(END, 1)
    DASHBOARD.write_text(f"{before}{START}{payload}{END}{after}")
    totals = facts["tests"]["totals"]
    print(f"Dashboard updated: {DASHBOARD.relative_to(ROOT)}")
    print(f"  modules: {len(code['modules'])}, tests: {totals}, M2 commits: {len(facts['git']['commits'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
