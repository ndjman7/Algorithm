class Solution {
public:
    int reverse(int x) {
        long int ret = 0;
        int mul = 1;
        bool booho;
        if(x > INT_MAX)
            x = 0;
        else if(x > 0)
            booho = true;
        else if (x <= INT_MIN)
            x = 0;
        else {
            booho = false;
            x = -x;
        }

        while(true) {
            if (x <= 0)
                break;
            ret *= mul;
            mul = 10;
            ret += x % 10;
            x /= 10;

            if (INT_MAX < ret) {
                ret = 0;
                break;
            }
        }
