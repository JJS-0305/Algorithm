# Palindrome(회문)

>  Palindrome(회문)이란?
>
> 문자열을 거꾸로 해도 원래의 문자열과 같은 문자열인 특징을 가지고 있는 문자열을 가리키는 말입니다.
>
> 예시 : 토마토, abcba, 123454321



1. 가장 큰 팰린드롬 찾기

```python
def solution(s:str):
    # 팰린드롬 크기 확장
    def expand(left:int, right:int):
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left+1:right-1]
    
    # 확장 알고리즘 필요 x
    if len(s) < 2 or s == s[::-1]:
        return s
    
    result = ""
    for i in range(len(s)-1):
        result = max(result, expand(i,i+1), expand(i,i+2), key=len)
        
    return result
```

