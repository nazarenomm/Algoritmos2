def todos_con_todos(l1: list[int], l2: list[int]) -> list[tuple[int,int]]:
    if len(l1) == 0 or len(l2) == 0:
        return []
    else:
        return[(l1[0], i) for i in l2] + todos_con_todos(l2,l1[1:])
        
        
if __name__ == "__main__":
    xs = [1,2,3]
    ys = [10,20,30]
    print(todos_con_todos(xs,ys))
