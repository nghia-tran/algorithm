import java.util.Scanner;
import java.util.Arrays;

class MergeSort  {
	public static Scanner sc ;
	public static void main(String[] args) {
		sc = new Scanner (System.in); 
		System.out.println("enter length of the array "); 
		int n = sc.nextInt();
		System.out.println("enter the array");
		int array[] = new int[n];
		for (int i = 0 ; i < n ; i++) {
		 	array[i] = sc.nextInt();
		 } 
		System.out.println("the unsorted array is "); 
		System.out.println(Arrays.toString(array));
		mergesort(array);
		System.out.println("the sorted array is :");
		System.out.println(Arrays.toString(array));
		
	}
	static void mergesort(int array[]){
		int n = array.length;
		if (n < 2) {
			return ;
		}
		int mid = n / 2 ;
		int left[] = new int[mid];
		int right[] = new int[n - mid];
		for (int i = 0 ; i < mid ; i++) {
			left[i] = array[i];
			
		}
		for (int i = mid; i < n ; i++) {
			right[i - mid] = array[i];
			
		}
		mergesort(left);
		mergesort(right);
		merge(array,left,right);

	}
	public static void merge(int array[], int left[], int right[]){
		int nL = left.length;
		int nR = right.length;
		int i = 0, j = 0, k = 0; 

		while (i < nL && j < nR) {
			if (left[i] <= right[j]) {
				array[k] = left[i];
				i++;
				
			} else {
				array[k] = right[j];
				j++;
			}
			k++;
		}
		while (i < nL){
			array[k] = left[i];
			k++;
			i++;
		}
		while (j < nR) {
			array[k] = right[j];
			k++;
			j++;
			
		}

	}
}