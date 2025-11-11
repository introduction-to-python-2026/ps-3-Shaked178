def approximate_pi(n_terms):
    pi_approx = 0
    for n in range(n_terms):
        pi_approx += (-1) ** n / (2 * n + 1)
    return 4 * pi_approx
