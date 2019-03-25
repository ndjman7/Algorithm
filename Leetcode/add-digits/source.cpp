class Solution {
public:
    int addDigits(int num) {
        int ret = 0;
        while(true) {
            // 한 자리 수라면 빠져나오기
            if(num/10 == 0)
                break;
            int val = num;
            while(true) {
                // 한 자리 수라면 빠져나오기
                if(val==0) {
                    ret += val%10;
                    num = ret;
                    ret = 0;
                    break;
                }
                ret += val%10;
                val /= 10;
            }
        }
        return num;
    }
};
