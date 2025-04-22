#!/usr/bin/env python

import os
from urllib import parse

HEADER = """# 
# 알고리즘 문제 풀이 목록
"""

def main():
    content = ""
    content += HEADER
    
    directories = []
    solveds = []
    goormlevel_problems = []

    # 첫 번째 패스: goormlevel 문제 수집
    for root, dirs, files in os.walk("./goormlevel"):
        dirs.sort()
        
        # goormlevel의 직접 하위 디렉토리(문제번호)만 처리
        if root == './goormlevel':
            for problem_num_dir in dirs:
                problem_num_path = os.path.join(root, problem_num_dir)
                
                # 각 문제번호 폴더 아래의 문제이름 폴더를 찾기
                for problem_name_dir in os.listdir(problem_num_path):
                    problem_name_path = os.path.join(problem_num_path, problem_name_dir)
                    
                    if os.path.isdir(problem_name_path):
                        # 해당 디렉토리 내의 파일 찾기
                        for file in os.listdir(problem_name_path):
                            file_path = os.path.join(problem_name_path, file)
                            if os.path.isfile(file_path):
                                # 문제 정보 저장
                                goormlevel_problems.append({
                                    'num': problem_num_dir,
                                    'name': problem_name_dir,
                                    'path': file_path
                                })
                                break  # 첫 번째 파일만 사용

    # 두 번째 패스: 다른 알고리즘 사이트 처리
    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            # 숨김 디렉토리와 처리 완료된 디렉토리 제외
            for dir in ('.git', '.github', 'goormlevel'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        # 이미지 폴더 건너뛰기
        if os.path.basename(root) == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        category = os.path.basename(root)
        
        # 최상위 디렉토리가 아닌 경우 건너뛰기
        if directory == '.':
            continue
            
        # 새로운 최상위 디렉토리 발견
        if directory not in directories:
            # 주요 알고리즘 사이트 헤더 추가
            if directory in ["백준", "프로그래머스", "LeetCode"]:
                content += "## 📚 {}\n".format(directory)
            else:
                # 난이도 헤더 추가
                content += "### 🚀 {}\n".format(directory)
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)

        # 문제 추가
        for file in files:
            if category not in solveds:
                content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))
                solveds.append(category)
                print("category : " + category)

    # goormlevel 문제 처리 - 마지막에 별도로 추가
    if goormlevel_problems:
        content += "## 📚 goormlevel\n"
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

    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
