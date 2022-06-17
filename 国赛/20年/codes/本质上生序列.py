s = "tocyjkdzcieoiodfpbgcncsrjbhmugdnojjddhllnofawllbhfiadgdcdjstemphmnjihecoapdjjrprrqnhgccevdarufmliqijgihhfgdcmxvicfauachlifhafpdccfseflcdgjncadfclvfmadvrnaaahahndsikzssoywakgnfjjaihtniptwoulxbaeqkqhfwl"
n = len(s)
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if s[i] > s[j]:
            dp[i] += dp[j]
        elif s[i] == s[j]:
            dp[i] -= dp[j]
print(sum(dp))
