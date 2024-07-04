def pattern_count(text,pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]== pattern:
            count= count+1
    return count
text= "abcdeabsab"
pattern="ab"
print(pattern_count(text, pattern))
