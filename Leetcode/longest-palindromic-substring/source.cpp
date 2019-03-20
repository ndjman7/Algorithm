class Solution {
public:
    string longestPalindrome(string s) {
        string ans;
        // "a"도 가능하니 -1로 설정 해두어야한다.
        int maxArea = -1;
        // 홀수개와 짝수개를 구분해서 계산한다.
        for(int i = 0; i < s.length(); ++i) {

            // 홀수
            int area = 0;
            while(true) {
                // 기준점에서 떨어져 있는 좌우
                int left = i-area;
                int right = i+area;

                // 좌우가 index를 벗어난 경우
                if(left < 0 || right >= s.length())
                    break;

                // 좌우가 다른 경우
                if(s[left] != s[right])
                    break;
                // 확장
                area++;
            }
            // 마지막 area는 검증되지않은 값으로 1감소 시켜야한다.
            area--;

            if(area > maxArea) {
                maxArea = area;
                // 왼쪽에서 끝까지
                ans = s.substr(i-area, 2*area + 1);
            }

            // 짝수
            area = 0;

            if(s[i] != s[i+1])
                continue;

            while(true) {
                // 기준점에서 떨어져 있는 좌우
                int left = i-area;
                int right = i+area+1;

                // 좌우가 index를 벗어난 경우
                if(left < 0 || right >= s.length())
                    break;

                // 좌우가 다른 경우
                if(s[left] != s[right])
                    break;
                // 확장
                area++;
            }
            area--;

            // 홀수에서 maxArea를 뽑아냈다고 하더라도 다르다
            if(area >= maxArea) {
                maxArea = area;
                // 왼쪽에서 끝까지
                ans = s.substr(i-area, 2*area + 2);
            }
        }
        return ans;
    }
};
