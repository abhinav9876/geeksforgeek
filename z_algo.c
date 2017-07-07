#include<stdio.h>
#include<strings.h>

void z_arr(char ss[],int z[])
{
  int l=0,r=0,i=0,k=0;
  int n=strlen(ss);
  z[0]=0;

  for(i=2;i<n;i++)
  {
    if(r<i)
    {
        r=l=i;
        while(r<n && ss[r]==ss[r-l])r++;
        z[i]=r-l;
        r--;
    }
    else
    {
        k=i-l;
        if (z[k] < r-i+1)
            { z[i] = z[k];}
        else
        {
          while (r<n && ss[r-l] == ss[r])
                    r++;
                z[i] = r-l;
                r--;
        }


    }
  }



}

void search(char str[],char pattern[])
{
 char concate[]=pattern+'$'+str;
 int l=strlen(concate),i;
 int z[l];
 z_arr(concate,z);
 for (int i = 0; i < l; ++i)
    {

        if (z[i] == pattern.length())
            printf("Pattern found at index %d \n",i - pattern.length());
    }


}

int main()
{
  char text[] = "GEEKS FOR GEEKS";
    char pattern[] = "GEEK";
      search(text, pattern);
      return 0;



}
