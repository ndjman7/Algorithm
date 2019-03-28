class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // 주어진 n값 0-n 이므로 n+1로 초기화
        vector<bool> answer(nums.size()+1, false);
        for(int i = 0; i < nums.size(); ++i)
            answer[nums[i]] = true;
        for(int i = 0; i < answer.size(); ++i)
            if(answer[i] == false)
                return i;
        return -1;
    }
};
