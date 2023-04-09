from lnn import And, Or, Implies, Iff, Propositions, Model

# Rules
A, B, C, D, E = Propositions("A", "B", "C", "D", "E")
IMPLIESe = Implies(A, B)
ANDe = And(C, D)
dIMPLIESe = Iff(ANDe, E)
ANDee = And(IMPLIESe, dIMPLIESe)

# Data
ANDee.add_data((1.0, 1.0))
A.add_data((0.2))
C.add_data((1.0, 1.0))
E.add_data((0.3, 0.7))

model = Model()
model.add_knowledge(ANDee)

# Reasoning
model.infer()
B.print()
D.print()
E.print()

#query
def query_state(node):
    round_off = lambda my_list: [float(f"{_:.1f}") for _ in my_list]
    return f"{node.state().name}: {tuple(round_off(node.get_data().tolist()))}"


query2 = Or(B, D, E)
model2 = Model()
model2.add_knowledge(query2)
model2.infer()
query2.print()

Result=query_state(query2)
print(Result)


