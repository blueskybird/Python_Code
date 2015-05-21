package javaTest;

public class Primes {

    /**
     * @param args
     */
    public static void main(String[] args) {
        int N = 1000000000;
        int i = 0, j = 0 , count = 0;
        int prime[] = new int[N + 1];

        //初始化数据
        for (i = 2; i <= N; i++) {
            prime[i] = 1;
        }
        //循环1(N 开方 次)
        for (i = 2; i * i <= N; i++) {
            if (prime[i] == 0) {
                count++;
                continue;
            }
            //循环2(N/i 次)  筛选被i整除的数 
            for (j = i * i; j <= N; j = j + i) {
                prime[j] = 0;
                count++;
            }
        }

        System.out.println("Times of calculation : " + count);
        j=0;
        for (i = 2; i <= N; i++) {
            if (prime[i] == 1) {
                System.out.print("\t");
                System.out.print(i);
                j++;
                if(j % 10 == 0){
                    System.out.println();
                }
            }

        }

    }

}