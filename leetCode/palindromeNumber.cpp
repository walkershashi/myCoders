class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        else{
            long int rev_x = 0;
            long int org_x = x;
            while(x>0){
                rev_x = rev_x *10 + x%10;
                x /= 10;
            }
            if (rev_x - org_x == 0){
                return true;
            }
            else{
                return false;
            }
        }
    }
};
