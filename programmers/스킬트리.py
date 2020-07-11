def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        cnt = 0
        s_tree = ""
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                cnt += 1
                s_tree += skill_tree[i]
        if skill[:cnt] == s_tree:
            answer += 1
    return answer