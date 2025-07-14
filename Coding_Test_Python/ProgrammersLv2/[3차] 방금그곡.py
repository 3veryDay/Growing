from collections import deque
def solution(m, musicinfos):
    
    def change(m) :
        m = m.replace("C#", "c")
        m = m.replace("D#",  "d")
        m = m.replace("F#", "f")
        m = m.replace("G#", "g")
        m = m.replace("A#", "a")
        m = m.replace("B#", "b")
        return m
    m = change(m)
    answer = [0,'']
    for info in musicinfos :
        start = 60* int(info[:2]) + int(info[3:5])
        end = 60* int(info[6:8]) + int(info[9:11])
        name, chord = info[12:].split(",")
        c = change(chord)
        played = c*((end-start+1)//len(c)) + c[:((end-start+1)%len(c)) ]
        print(played)
        if m in played :
            if answer[0] < end-start + 1 :
                answer = [end-start+1, name]
    if answer[0] != 0 :
            return answer[1]
    return '(None)'
                
