tank_capacity = 255
pipes = int(input())

flow = 0

for pipe in range(pipes):
    pipe_flow = int(input())
    flow += pipe_flow
if flow >= tank_capacity:
    print()
