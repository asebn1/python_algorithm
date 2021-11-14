def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(0, len(completion), 1):
        if(completion[i] != participant[i]):
            return participant[i]
    return participant[-1]