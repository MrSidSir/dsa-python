#Problem: Given a list of products, return up to 3 lexicographically smallest products for each prefix of search word.
#Real world use:
#Google search, Amazon product search bar.

def suggestedProducts(products, searchWord):  # Fixed: searchWord not searchWorld
    products.sort()  # Fixed: products not product
    res = []
    prefix = ""
    
    for c in searchWord:  # Fixed: searchWord not searchWorld
        prefix += c
        matches = [p for p in products if p.startswith(prefix)]  # Fixed: startswith not startswitch
        res.append(matches[:3])
    
    return res  # Fixed: proper indentation

#Example
print(suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
#[['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']]

#Logic:
#Sort products.
#For each prefix, filter candidates, keep first 3.