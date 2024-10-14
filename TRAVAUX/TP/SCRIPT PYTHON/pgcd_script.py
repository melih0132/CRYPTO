def extended_euclid_gcd(a, b, debug=False):
    """
    Returns 3 results:
    - gcd(a, b)
    - Coefficients of Bézout's identity: x and y such that ax + by = gcd(a, b)
    """
    # Initial values
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    
    if debug:
        print(f"Initial values: a = {a}, b = {b}")
    
    while r != 0:
        quotient = old_r // r  # In Python, // performs integer division
        
        # Debug information for current iteration
        if debug:
            print(f"\nBefore iteration: old_r = {old_r}, old_s = {old_s}, old_t = {old_t}, r = {r}, quotient = {quotient}")
        
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
        
        # Debug information after updates
        if debug:
            print(f"After iteration: old_r = {old_r}, old_s = {old_s}, old_t = {old_t}, r = {r}")

    # The gcd is stored in old_r, and the coefficients are old_s and old_t
    if debug:
        print(f"\nFinal result: gcd = {old_r}, x = {old_s}, y = {old_t}")
        
    return old_r, old_s, old_t

    if debug:
        print(f"Final GCD: {d}")
    return d