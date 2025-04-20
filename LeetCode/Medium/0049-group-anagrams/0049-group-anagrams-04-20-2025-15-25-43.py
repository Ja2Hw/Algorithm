class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 리스트에 추가
            anagrams[''.join(sorted(word))].append(word)
            # sorted(문자열) -> 문자열이 문자 하나하나로 분해되어 정렬된다!
                # sorted('eat') -> ['a', 'e' 't']
                # 이렇게 정렬한 후 join으로 다시 문자열으로 조립하고, 그걸 anagrams 딕셔너리에 키값 삼아 word를 append함.
                    # defaultdict(list)로 했으니 키가 없을 경우에 자동으로 빈 리스트를 만들어줌

        return list(anagrams.values()) # anagrams 딕셔너리의 값들(이미 각각 리스트로 되어있으므로)만 꺼내서 리스트로 묶어서 리턴함
        