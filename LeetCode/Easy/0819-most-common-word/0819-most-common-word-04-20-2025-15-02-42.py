# 가장 흔한 단어 : defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # 정규식에서 \w는 단어 문자(Word Character)를 뜻하며, ^는 not을 의미한다
        # 아래처럼 사용한다면 단어 문자가 아닌 모든 문자를 공백으로 치환(Substitute)하는 역할 
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        # 따라서 단어 문자가 아닌 모든 문자가 공백으로 치환된 paragraph를 소문자로 변경하고, split()한 그 word가 banned에 속한 단어가 아니라면
        # words 안에 집어넣는 리스트 컴프리헨션 문법

        # 개수를 담아두는 변수에 defaultdict(int)를 사용해서 int값 0이 자동으로 부여된다
        cnt = collections.defaultdict(int)
        

        for word in words:
            cnt[word] += 1

        return max(cnt, key=cnt.get)
        # 딕셔너리 변수 cnt에서 가장 값이 큰 키를 가져온다
        