def test_prime(n):
    if n==2 or n==3 or n==5 or n==7:
        return True

    elif n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
        return True
    else:
        return False