class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_string = ""  # Geçici substring
        sub_string_len = 0  # En uzun substring uzunluğu
        i = 0  # Sağ uç
        while i < len(s):
            if s[i] not in sub_string:
                # Eğer s[i] substring içinde yoksa, substring'e ekle
                sub_string += s[i]
            else:
                # Eğer s[i] zaten var, en uzun substring'i güncelle
                sub_string_len = max(sub_string_len, len(sub_string))
                # Sadece tekrarı silip substring'i kaydırarak devam et
                char_index = sub_string.index(s[i])  # s[i] ilk nerede varsa
                # o karakteri kes ve substringi kaydır
                sub_string = sub_string[char_index + 1:]
                # Yeni karakteri ekle
                sub_string += s[i]

            # İleri git
            i += 1

        # Son olarak, en uzun substring'i döndür
        sub_string_len = max(sub_string_len, len(sub_string))
        return sub_string_len


solution = Solution()
print(solution.lengthOfLongestSubstring(input("girişi ver: \n")))
