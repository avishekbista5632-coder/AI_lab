% Define the base cases for Fibonacci

fibonacci(0, 0).

fibonacci(1, 1).

% Define the recursive case for Fibonacci

fibonacci(N, Result) :-

    N > 1,

    N1 is N - 1,

    N2 is N - 2,

    fibonacci(N1, R1),

    fibonacci(N2, R2),

    Result is R1 + R2.

% To display the Fibonacci series up to N terms

fibonacci_series(0, [0]).

fibonacci_series(N, Series) :-

    N > 0,

    findall(F, (between(0, N, I), fibonacci(I, F)), Series).

% Example query: fibonacci_series(10, Series).