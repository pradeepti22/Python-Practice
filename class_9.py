import LocklearStats as genepy

def muSigma2Sigma(L):
    mu = genepy.avgList(L)
    sigma2 = genepy.varianceList(L)
    sigma = genepy.standardDeviationList(L)
    return (mu, sigma2, sigma)

def main():
    A = [1,2,3,4,5]
    print(muSigma2Sigma(A))
    
    
main()
    
    
