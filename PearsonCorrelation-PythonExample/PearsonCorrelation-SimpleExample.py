from scipy.stats import pearsonr

age = [43,21,25,42,57,59]
glucoseLevel = [99,65,79,75,87,81]

r,p = pearsonr(age,glucoseLevel)

print("Pearson correlation value:",r)
print("p-value:",p)
