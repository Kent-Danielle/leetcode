class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m + n - 1;
        int p1 = m - 1;
        int p2 = n - 1;
            
        while (p1 >= 0 && p2 >= 0) {
            if (nums1[p1] > nums2[p2]) {
                nums1[i] = nums1[p1];
                i--;
                p1--;
            } else {
                nums1[i] = nums2[p2];
                i--;
                p2--;
            }
        }
        
        if (p1 >= 0) {
            for (int j = p1; j >= 0; j--){
                nums1[i] = nums1[j];
                i--;
            }
        } else if (p2 >=0 ){
            for (int j = p2; j >= 0; j--) {
                nums1[i] = nums2[j];
                i--;
            }
        }
        
        
        
        /*
        O(n) space
        int[] nums1copy = new int[m];
        System.arraycopy(nums1, 0, nums1copy, 0, m);
        int pointer1 = 0; // pointer for nums1copy
        int pointer2 = 0; // pointer for nums2
        int walk = 0; // pointer for nums

        
        
        while (pointer1 < m && pointer2 < n) {
            if (nums1copy[pointer1] < nums2[pointer2]) {
                nums1[walk] = nums1copy[pointer1];
                walk++;
                pointer1++;
            } else {
                nums1[walk] = nums2[pointer2];
                walk++;
                pointer2++;
            }
        }
        
        if (pointer1 < m) {
            for (int i = pointer1; i < m; i++) {
                nums1[walk] = nums1copy[i];
                walk++;
            }
        } else if (pointer2 < n) {
            for (int i = pointer2; i < n; i++) {
                nums1[walk] = nums2[i];
                walk++;
            }
        }
        */
        
    }
}