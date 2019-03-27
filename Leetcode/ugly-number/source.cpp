class Solution {
public:
    // prime factor로 나눠주는 함수
    int returnNum(int num, int val) {
        while(true) {
            if(num % val == 0 && num / val != 0)
                num /= val;
            else
                break;
        }
        return num;
    }
    bool isUgly(int num) {
        num = returnNum(num, 2);
        num = returnNum(num, 3);
        num = returnNum(num, 5);
        // positive numbers 가 아니면 false
        if (num <= 0)
            return false;
        // 유일한 한 자리수 prime factor
        if (num >= 7 && num % 7 == 0)
            return false;
        // 두 자리수 이상이라면 prime factor가 존재하는 것으로 판단
        if (num / 10 > 0)
            return false;
        return true;
    }
};
