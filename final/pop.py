from graphviz import Digraph

pop= Digraph("pop")
pop.attr(rankdir='LR')

p = list(range(4))
with pop.subgraph() as c:
#    c.attr(rank='same')
    for i in p:
        c.node(f"Age {i}")

for i in p:
    if i+1 in p:
        pop.edge(f"Age {i}",f"Age {i+1}",f"s{i}")
    pop.edge(f"Age {i}","Age 0",f"f{i}")
    
pop.format='png'
pop.render()
