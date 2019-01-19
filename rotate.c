#include<stdio.h>

int rotate(int, int);

int main()
{
	int no, nor;
	
	printf("Enter a Number : ");
	scanf("%d", &no);
	printf("Enter Number of Rotations : ");
	scanf("%d", &nor);
	
	
	printf("Rotated Number : %d\n", rotate(no,nor));
}

int rotate(int no, int temp_rot)  //temp_rot contains number of roatations to be made 
{

	int rev[10];  //stores digits of the number in reverse order
	int ori[10];  //stores digits of the number as they were originally
	int rot[10];  //stores digits of rotated number
	int count;	  //stores count of the digits in the number
	int temp_no, temp;
	int i,j;
	int nor;//no. of rotations after wrap around (6 rotations for a 6 digit no. is equivalent to 0 rotations)
	int res;	  //result 
	
	
	//Separate the digits od the number (in reverse order)
	temp_no = no;
	count=0;
	while(temp_no > 0)
	{
		temp = temp_no%10;
		rev[count] = temp;
		temp_no = temp_no / 10;
		count++;
	}
	
	nor = temp_rot % count; // wrapping around
	
	//arrange the digits as they were originally
	for(j=0,i=count-1; i>=0; i--, j++)
	{
		ori[j] = rev[i];
	}

	//Rotate the Number	(in array form)
	for(i=nor, j=0; i<count; i++, j++)
	{
		rot[j] = ori[i];	
	}
	for(i=0;i<nor; i++,j++)
	{
		rot[j] = ori[i];
	}

	//genetate	final number
	res = 0;
	for(i=0; i<count; i++)
	{
		res = (res*10) + rot[i];
	}
	
	return res;

}
