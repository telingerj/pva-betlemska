from utils.prace_se_seznamy import swap

def get_max_pos(l, start, end):
    max_pos = 0
    for i in range(start,  end + 1):
        if l[max_pos] < l[i]:
            max_pos = i
    return max_pos

def select_sort(l):
    for i in range(0, len(l)):
        max_pos = get_max_pos(l, 0, len(l) - 1 - i)
        swap(l, max_pos, len(l) - 1 - i)
