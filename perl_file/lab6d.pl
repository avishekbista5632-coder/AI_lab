% Define the base case for Tower of Hanoi

hanoi(1, Source, Destination, _) :-

    format('Move disk from ~w to ~w~n', [Source, Destination]).

% Define the recursive case for Tower of Hanoi

hanoi(N, Source, Destination, Auxiliary) :-

    N > 1,

    N1 is N - 1,

    hanoi(N1, Source, Auxiliary, Destination),

    hanoi(1, Source, Destination, _),

    hanoi(N1, Auxiliary, Destination, Source).

% Example query: hanoi(3, 'A', 'C', 'B').