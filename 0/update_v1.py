#!/usr/bin/env python

import os
from urllib import parse

HEADER = """# 
# 백준 문제 풀이 목록
"""

def main():
    content = ""
    content += HEADER

    directories = []
    solveds = []

    for root, dirs, files in os.walk("."):
        dirs.sort()

        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        # 현재 경로 기준 정보 파싱
        category = os.path.basename(root)
        parent = os.path.basename(os.path.dirname(root))

        # images 디렉토리 무시
        if category == 'images':
            continue

        # 루트 바로 아래 디렉토리는 무시
        if parent == '.':
            continue

        # 헤더 추가
        if parent not in directories:
            if parent in ["백준", "프로그래머스", "LeetCode", "goormlevel"]:
                content += f"## 📚 {parent}\n"
            else:
                content += f"### 🚀 {parent}\n"
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(parent)

        # goormlevel은 난이도 폴더가 없으므로 category가 곧 문제번호
        if parent == "goormlevel":
            for file in files:
                file_path = parse.quote(os.path.join(root, file))
                content += f"|{category}|[링크]({file_path})|\n"
        else:
            for file in files:
                if category not in solveds:
                    file_path = parse.quote(os.path.join(root, file))
                    content += f"|{category}|[링크]({file_path})|\n"
                    solveds.append(category)

    with open("README.md", "w", encoding="utf-8") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
