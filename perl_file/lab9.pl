% Family tree facts
parent(james_I, charles_I).
parent(james_I, elizabeth).
parent(charles_I, catherine).
parent(charles_I, charles_II).
parent(charles_I, james_II).
parent(elizabeth, sophia).
parent(sophia, george_I).

% Queries
% a) Is George I the parent of Charles I?
?- parent(george_I, charles_I).

% b) Is Charles I parent of Catherine?
?- parent(charles_I, catherine).

% c) Is George I child of Charles I?
?- parent(charles_I, george_I).

% d) Show the relation for Sister_of, Brother_of, Sibling_of
sister_of(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y, female(X).
brother_of(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y, male(X).
sibling_of(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
