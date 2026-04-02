% Graph facts

edge(s, a).

edge(s, b).

edge(a, c).

edge(b, e).

edge(a, e).

edge(e, g).







% b) Is there a path from (s, g)

path(X, Y) :- edge(X, Y).

path(X, Y) :- edge(X, Z), path(Z, Y).


