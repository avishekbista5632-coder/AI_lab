% Facts: Representing family relationships
parent(john, mary).
parent(mary, lisa).
parent(john, mike).
parent(mike, sam).
parent(sam, ana).

% Rules: Defining relationships based on facts
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

% Queries you can test:
% ?- grandparent(john, lisa).
% ?- ancestor(john, ana).
% ?- sibling(mary, mike).

% List Operations

% Membership check
member(X, [X|_]).  % X is the head of the list
member(X, [_|T]) :- member(X, T).  % Recursively check the tail

% Length of a list
list_length([], 0).
list_length([_|T], N) :- list_length(T, N1), N is N1 + 1.

% Concatenation of two lists
concatenate([], L, L).
concatenate([H|T], L, [H|R]) :- concatenate(T, L, R).

% Insert an element at the beginning
insert(X, L, [X|L]).

% Delete an element from a list
delete(_, [], []).  
delete(X, [X|T], T).  
delete(X, [H|T], [H|R]) :- delete(X, T, R).

% Append an element at the end
append([], X, [X]).
append([H|T], X, [H|R]) :- append(T, X, R).

% Sample queries to run:
% ?- member(3, [1,2,3,4,5]).
% ?- list_length([a,b,c,d], N).
% ?- concatenate([1,2], [3,4], R).
% ?- insert(x, [a,b,c], R).
% ?- delete(b, [a,b,c,d], R).
% ?- append([1,2,3], 4, R).