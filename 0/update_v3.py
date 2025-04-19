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
    goormlevel_problems = []

    # 첫 번째 패스: 디렉토리 구조 파악 및 goormlevel 문제 수집
    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        directory = os.path.basename(os.path.dirname(root))
        category = os.path.basename(root)
        
        if category == 'images':
            continue
            
        # goormlevel 문제 정보 수집
        if directory == 'goormlevel':
            problem_num = category  # goormlevel/문제번호/
            
            for problem_dir in dirs:
                problem_path = os.path.join(root, problem_dir)
                for problem_file in os.listdir(problem_path):
                    file_path = os.path.join(problem_path, problem_file)
                    if os.path.isfile(file_path):
                        # 문제 번호와 이름 저장
                        goormlevel_problems.append({
                            'num': problem_num,
                            'name': problem_dir,
                            'path': file_path
                        })
                        break

    # 두 번째 패스: README 생성
    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            continue
            
        # 최상위 디렉토리 확인 및 헤더 추가
        if directory not in directories:
            if directory in ["백준", "프로그래머스", "LeetCode", "goormlevel"]:
                content += "## 📚 {}\n".format(directory)
                
                # goormlevel은 별도 처리
                if directory == "goormlevel":
                    content += "| 문제번호 | 문제이름 | 링크 |\n"
                    content += "| ----- | ----- | ----- |\n"
                    
                    # 문제번호 기준으로 정렬
                    sorted_problems = sorted(goormlevel_problems, key=lambda x: x['num'])
                    
                    for problem in sorted_problems:
                        problem_num = problem['num']
                        problem_name = problem['name']
                        problem_path = problem['path']
                        
                        content += "|{}|{}|[링크]({})|\n".format(
                            problem_num, 
                            problem_name, 
                            parse.quote(problem_path)
                        )
                    
                    # goormlevel 처리 완료 후 directories에 추가
                    directories.append(directory)
                    continue
            else:
                content += "### 🚀 {}\n".format(directory)
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)
            
        # goormlevel은 이미 별도 처리했으므로 건너뜀
        if "goormlevel" in root:
            continue

        # 다른 문제 사이트들 처리
        for file in files:
            if category not in solveds:
                content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))
                solveds.append(category)
                print("category : " + category)

    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()