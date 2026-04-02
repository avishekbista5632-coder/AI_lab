% Define the base case for factorial

factorial(0, 1).

% Define the recursive case for factorial

factorial(N, Result) :-

    N > 0,

    N1 is N - 1,

    factorial(N1, R1),

    Result is N * R1.

% Example query: factorial(5, Result).