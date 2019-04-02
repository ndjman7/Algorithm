class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int size = nums.size();
        int cnt = 1;
        // 맨 뒤부터 0을 만날 시 0 위치를 당기고 맨 뒤에 0을 넣어줌
        for(int i = size-1; i >= 0; i--) {
            if(nums[i] == 0) {
                for(int j = i; j < nums.size()-1; j++) {
                    nums[j] = nums[j+1];
                }
                nums[size-cnt] = 0;
                cnt++;
            }
        }
    }
};
