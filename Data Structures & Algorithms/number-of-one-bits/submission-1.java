class Solution {
    public int hammingWeight(int n) {
       int counter = 0;

      //add 0 place tp counter
        //bitshit right
        //add 0 place to counter
while(n != 0){
        int result = 1 & n;
        n = n >> 1;
        counter += result;
        }
        return counter;
    }
    
}
