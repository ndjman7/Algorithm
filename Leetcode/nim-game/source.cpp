class Solution {
public:
    bool canWinNim(int n) {
        // 4의 배수라면 내가 1,2,3을 제거해도 이길 수 없다.
        if(n%4==0)
            return false;
        // 내가 제외한 후 상대가 3의 배수 + 1이 혹은 0이 되어야지만 이길 수 있다.
        for(int i = 1; i <= 3; ++i)
            if((n-i)%3 == 1 or (n-i) == 0)
                return true;
        return false;
    }
};
