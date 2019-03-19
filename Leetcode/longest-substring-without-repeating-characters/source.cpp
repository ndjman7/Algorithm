class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxCount = 0;
        // Ascii code를 표현하기 위한 범위
        bool character[128];

        for(int i = 0; i < s.length(); ++i) {
            for(int i = 0; i < 128; ++i)
                character[i] = false;
            // ""도 가능하니 count는 1부터가 아닌 0부터임.
            int count = 0;

            // " "도 input이 가능하니, s.length() - 1은 No.
            for(int j = i; j < s.length(); ++j) {
                if (character[s[j]] == true)
                    break;
                character[s[j]] = true;
                count++;
            }
            maxCount = max(maxCount, count);
        }
        return maxCount;
    }
};
