#!/usr/bin/env python

import os
from urllib import parse

HEADER="""#
# 백준 문제 풀이 목록
"""

def main():
    content = ""
    content += HEADER

    directories = [];
    solveds = [];

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        directory = os.path.basename(os.path.dirname(root))

        if category == 'images':
            continue

        # goormlevel 디렉토리 특별 처리
        if directory == 'goormlevel':
            if directory not in directories:
                content += "## 📚 {}\n".format(directory)
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
                directories.append(directory)
            for file in files:
                problem_number = os.path.splitext(file)[0].split('-')[0] if '-' in os.path.splitext(file)[0] else os.path.splitext(file)[0]
                if (category, file) not in solveds:
                    content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))
                    solveds.append((category, file))
                    print("category (goormlevel): " + category + ", file: " + file)
            continue # goormlevel 내부 파일 처리가 끝났으므로 다음 순회로 이동

        # 일반적인 경우 (난이도 폴더 처리)
        if directory != '.' and directory not in directories:
            if directory in ["백준", "프로그래머스", "LeetCode", "goormlevel"]:
                content += "## 📚 {}\n".format(directory)
            else:
                content += "### 🚀 {}\n".format(directory)
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)

        if directory != '.':
            for file in files:
                problem_number = os.path.splitext(file)[0].split('-')[0] if '-' in os.path.splitext(file)[0] else os.path.splitext(file)[0]
                if (category, file) not in solveds:
                    content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))
                    solveds.append((category, file))
                    print("category (normal): " + category + ", file: " + file)

    with open("README.md", "w") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()