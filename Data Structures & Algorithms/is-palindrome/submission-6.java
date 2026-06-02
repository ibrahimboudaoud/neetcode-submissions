class Solution {
    public boolean isPalindrome(String s) {
        String temp = "";
        for(int i =0; i < s.length(); i++)
        {
            if(Character.isLetterOrDigit(s.charAt(i)))
            {
                temp += s.charAt(i);
            }
        }
        String temp2 = "";
        for(int i = temp.length()-1; i>=0; i--)
        {
            temp2+= temp.charAt(i);
        }
        return temp2.equalsIgnoreCase(temp);
    }
}
