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
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            continue
            
        if directory not in directories:
            if directory in ["백준", "프로그래머스", "LeetCode", "goormlevel"]:
                content += "## 📚 {}\n".format(directory)
            else:
                content += "### 🚀 {}\n".format(directory)
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)

        # goormlevel 디렉토리의 경우, 하위 디렉토리가 없으므로 직접 파일을 탐색
        if directory == "goormlevel":
            for file in files:
                problem_number = os.path.splitext(file)[0]
                file_path = parse.quote(os.path.join(root, file))
                content += f"|{problem_number}|[링크]({file_path})|\n"
                print(f"category : {problem_number}")
        else:
            for file in files:
                if category not in solveds:
                    content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))
                    solveds.append(category)
                    print("category : " + category)

    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
