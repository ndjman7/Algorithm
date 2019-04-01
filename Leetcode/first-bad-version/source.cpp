// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        long s=1, e=n, m, ans=1;
        while(true) {
            m = (s+e)/2;
            if(e==s) {
                if(isBadVersion(m))
                    ans = m;
                break;
            }
            if(isBadVersion(m)) {
                ans = m;
                e = m;
            }
            else 
                s = m+1;
        }
        return ans;
    }
};
