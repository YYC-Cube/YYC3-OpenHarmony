#!/usr/bin/env python3
"""Repository integrity checks for the YYC3-OpenHarmony CI pipeline.

Validates structural and documentation invariants that must hold for a
YYC3-branded Flutter SDK fork: version baselines, workflow syntax, brand
assets, relative documentation links, and residual upstream-only settings.

Exit code 0 means all checks passed; 1 means at least one check failed.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
FAILURES: list[str] = []

REQUIRED_FILES = [
    "README.md",
    "README.en.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    "bin/internal/engine.version",
    "bin/internal/engine.ohos.version",
    "public/yyc3-family.png",
]

JSON_FILES = ["README.OpenSource"]

VERSION_DOCS = ["README.md", "README.en.md"]
VERSION_SOURCES = ["bin/internal/engine.version", "bin/internal/engine.ohos.version"]

# Secrets and repository gates inherited from the upstream flutter/flutter setup
# are inert or broken in this fork and must not come back.
FORBIDDEN_WORKFLOW_SNIPPETS = [
    "FLUTTERACTIONSBOT",
    "FLUTTERMIRRORINGBOT",
    "github.repository == 'flutter/flutter'",
    "github.repository == \"flutter/flutter\"",
]

MARKDOWN_LINK = re.compile(r"\]\(([^)\s]+)\)")
HTML_LINK = re.compile(r"href=\"([^\"]+)\"")


def fail(message: str) -> None:
    FAILURES.append(message)


def check_required_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            fail(f"缺少必需文件: {rel}")


def check_json() -> None:
    for rel in JSON_FILES:
        path = ROOT / rel
        if not path.is_file():
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"JSON 解析失败: {rel}: {exc}")


def check_yaml() -> None:
    for path in sorted((ROOT / ".github").rglob("*.yml")) + sorted(
        (ROOT / ".github").rglob("*.yaml")
    ):
        try:
            yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            fail(f"YAML 解析失败: {path.relative_to(ROOT)}: {exc}")


def check_version_baseline() -> None:
    for source in VERSION_SOURCES:
        path = ROOT / source
        if not path.is_file():
            continue
        revision = path.read_text(encoding="utf-8").strip()
        if not revision:
            fail(f"版本基线为空: {source}")
            continue
        for doc in VERSION_DOCS:
            doc_path = ROOT / doc
            if doc_path.is_file() and revision not in doc_path.read_text(encoding="utf-8"):
                fail(f"{doc} 未同步版本基线 {source}: {revision}")


def check_brand_asset() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "public/yyc3-family.png" not in readme:
        fail("README.md 顶部未引用 public/yyc3-family.png")


def check_relative_links() -> None:
    for doc in VERSION_DOCS:
        doc_path = ROOT / doc
        if not doc_path.is_file():
            continue
        text = doc_path.read_text(encoding="utf-8")
        targets = MARKDOWN_LINK.findall(text) + HTML_LINK.findall(text)
        for target in targets:
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            rel = target.split("#", 1)[0]
            if not rel:
                continue
            candidate = (ROOT / rel.lstrip("/")) if rel.startswith("/") else (
                doc_path.parent / rel
            )
            if not candidate.exists():
                fail(f"{doc} 存在失效相对链接: {target}")


def check_workflows() -> None:
    workflow_dir = ROOT / ".github" / "workflows"
    for path in sorted(workflow_dir.glob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        for snippet in FORBIDDEN_WORKFLOW_SNIPPETS:
            if snippet in text:
                fail(f"{path.name} 残留上游专用配置: {snippet}")


def main() -> int:
    check_required_files()
    check_json()
    check_yaml()
    check_version_baseline()
    check_brand_asset()
    check_relative_links()
    check_workflows()

    if FAILURES:
        print("仓库完整性校验失败:")
        for item in FAILURES:
            print(f"  - {item}")
        return 1

    print(
        "仓库完整性校验通过: 必需文件、JSON/YAML 语法、版本基线、品牌资源、"
        "相对链接、CI 配置均符合 YYC3 规范。"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
