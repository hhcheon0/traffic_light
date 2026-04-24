def solution(signals): # 신호등의 상태를 나타내는 2차원 리스트인 signals를 입력으로 받는 함수
    n = len(signals) # 신호등의 개수 계산
    
    # 각 신호등의 노란불 시작 시점들을 모듈로 연산으로 표현
    # t ≡ a (mod cycle) 형태로, a는 [g+1, g+y] 범위
    
    from math import gcd # 최대 공약수 계산을 위한 gcd 함수
    from functools import reduce # 최소 공배수 계산을 위한 reduce 함수  
    
    def lcm(a, b): # 최소 공배수 계산 함수
        return a * b // gcd(a, b) # 최소 공배수 계산 함수
    
    cycles = [sum(signal) for signal in signals] # 각 신호등의 전체 주기 계산
    max_cycle = reduce(lcm, cycles) # 모든 신호등의 주기의 최소 공배수 계산
    max_time = min(max_cycle, 1000000) # 최대 시간은 모든 신호등의 주기의 최소 공배수로 설정, 너무 큰 경우 1,000,000으로 제한
    
    # 각 신호등이 노란불인지 확인
    def is_yellow(signal_idx, time): # 신호등이 노란불인지 확인
        g, y, r = signals[signal_idx] # 신호등의 초록, 노랑, 빨강 시간
        cycle = g + y + r # 신호등의 전체 주기
        t_in_cycle = ((time - 1) % cycle) + 1 # 현재 시간이 신호등의 주기 내에서 어디에 위치하는지 계산
        return g + 1 <= t_in_cycle <= g + y # 노란불 범위에 있는지 확인
    
    # 모든 시간 확인
    for t in range(1, max_time + 1): # 1부터 max_time까지 모든 시간에 대해 확인
        if all(is_yellow(i, t) for i in range(n)): # 모든 신호등이 노란불인지 확인
            return t # 모든 신호등이 노란불인 첫 번째 시간을 반환
    
    return -1 # 모든 시간에서 모든 신호등이 노란불이 되는 경우가 없으면 -1 반환
