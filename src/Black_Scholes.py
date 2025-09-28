import numpy as np
import math
from scipy.stats import norm

# Pricing model for European Options

def d1(S, K, r, T, sigma):
    """
    Args:
        S : Current stock price
        K : strike price
        T : Time to maturity in years
        r : annualized risk-free interest rate
        sigma: volatility

    Returns:
        d1 parameter
    """
    return (np.log(S/K)+ (r +sigma^2/2)*T/(sigma*np.sqrt(T)))

def d2(S, K, r, T, sigma):
    """
    Calculate d2 parameter for Black-Scholes model.
    
    Args:
        S: Current stock price
        K: Strike price
        T: Time to maturity in years
        r: Risk-free interest rate
        sigma: Volatility
        
    Returns:
        d2 parameter
    """
    return d1(S, K, r, T, sigma)-sigma * np.sqrt(T)

    
 