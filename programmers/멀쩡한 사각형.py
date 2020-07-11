def solution(w, h):
    mx = max(w, h)
    mn = min(w, h)

    while mn != 0:
        mx, mn = mn, mx % mn
    G = mx

    answer = w * h - ((w // G + h // G - 1) * G)
    return answer