% Facts
likes(john, ai).
likes(john, cs).
likes(sara, ai).
not(likes(sara, cs)).

likes(jack, X) :- likes(sara, X).

% Queries
% a) Is Jack like AI?
% ?- likes(jack, ai).

% b) Is Jack like CS?
% ?- likes(jack, cs).

% c) Is John likes CS?
% ?- likes(john, cs).

% d) Is Sara likes CS?
% ?- likes(sara, cs).

% e) IS Jin likes CS?
% ?- likes(Jin, cs).
