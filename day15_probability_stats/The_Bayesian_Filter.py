#Given Probabilities
P_spam = 0.10                  
P_ham = 0.90                   
P_free_given_spam = 0.90       
P_free_given_ham = 0.05        

# Step 1: Calculate total probability of "Free"
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

# Step 2: Apply Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

# Print Results
print("Total Probability of 'Free':", P_free)
print("Probability Email is Spam given it contains 'Free':", P_spam_given_free)
