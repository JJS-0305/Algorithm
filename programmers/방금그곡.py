def transform(melodys):
    melo = []
    for melody in melodys:
        if melody == '#':
            melo[-1] = melo[-1].lower()
        else:
            melo.append(melody)
    return ''.join(melo)

def solution(m, musicinfos):
    answer = []
    m = transform(m)
    time = len(m)
    for music in musicinfos:
        music = list(map(str, music.split(',')))
        music[3] = transform(music[3])
        hour = int(music[1].split(':')[0]) - int(music[0].split(':')[0])
        minute = int(music[1].split(':')[1]) - int(music[0].split(':')[1])
        striming = 60*hour + minute
        if time > striming:
            continue
        music[3] *= striming//len(music[3]) + 1
        music[3] = music[3][:striming]
        if m in music[3] or music[3] in m:
            answer.append((music[2],striming))
    if len(answer) >= 2:
        answer.sort(key=lambda x:-x[1])
        return answer[0][0]
    elif len(answer) == 1:
        return answer[0][0]
    else:
        return "(None)"
