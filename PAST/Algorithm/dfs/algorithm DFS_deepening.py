class Tree(object):
    def __init__(self, x, l=None, r=None):
        self.x = x
        self.l = l
        self.r = r
T = Tree(4, Tree(5, Tree(4, Tree(5))), Tree(6, Tree(1), Tree(6)))


def solution(T):
    distinct = {1: set([])} # 딕셔너리
    stack = [(T, set([T.x]))] # 말 그대로 스택,
    i = 1  # number of path, 얘는 그냥 초기설정
    while stack:  # DFS
        node, value = stack.pop() # stack is stored as list format containing set. => stack = list(set(T, set(list())))
        # 여기서 value 를 그냥 튜플 형태인 set(T.x)로 저장할 수도 있는데 굳이 리스트를 씌운 이유는, ---

        if (node.l == None) and (node.r == None):  # leaf node
            # 이 조건은, 자식 노드가 없을 때 (주석을 달 때도 간결하게)
            # print('i: ', i, 'value: ', value)
            distinct[i] = value  # value 는 set 으로(중복 값 x) 이 특성을 이용하여, 하나의 가지에서 가질 수 있는 모든 노드값을 중복없디 저장한다
            # distinct 는 딕셔너리로, 해당 키에 맞는 값을 갖는다.
            i += 1 # 즉, dfs 에서 하나의 깊이를 다 팠으니, 다른 깊이(가지)로 넘어간다는 뜻
            # distinct dictionary 의 키 값은 하나의 가지(브랜치)를 의미하게 된다

        else: # 자식노드가 하나라도 존재할 때
            if node.r != None: # 왜 이렇게 쓰지, node.r == True 하면 왜 결과가 달라져??
                stack.append((node.r, value | set([node.r.x]))) # append to stack, containing right node, value with new set

            # 아래 조건이, elif 나 else 가 아닌 이유는 곧, 위의 조건문과 상관없다는 뜻
            if node.l != None:
                stack.append((node.l, value | set([node.l.x])))

    answer = 1
    for key in distinct.keys():
        temp = len(distinct[key])
        if temp > answer:
            answer = temp
    print('distinct: ', distinct)
    return answer

print(solution(T))

# # stack=[(1,3,4)]
# # print(type(stack[0])) # this is Tuple, 이 스택은 튜플을 저장한다. 그 튜플에는 node, path, value가 포함돼있다.
# ref: https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html
