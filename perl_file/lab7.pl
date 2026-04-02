
% Facts

studies(radha).

studies(rakesh).

studies(anish).



not(studies(rekha)).

not(studies(bibek)).



% Rules

passes(X) :- studies(X).

happy(X) :- passes(X).



% Queries

% i. Did Anish pass?

% ?- passes(anish).



% ii. List all the students that passed.

% ?- passes(X).



% iii. Did Rekha study?

% ?- studies(rekha).



% iv. List all the students that did not study.

% ?- not(studies(X)).

