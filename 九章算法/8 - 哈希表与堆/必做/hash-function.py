class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        result = 0
        for i in range(len(key)):
            result *= 33
            result += ord(key[i]) 
            result %= HASH_SIZE 
        return result