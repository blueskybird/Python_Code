package code.words;

public class MonitorThread extends Thread{

    // 共享数据
    private AllCountModel acm;
    
    public MonitorThread(AllCountModel acm){
        this.acm = acm;
    }
    
    public void run() {
        while(true){
            try {
                // 隔段时间检查一次
                sleep(500); 
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            // 线程全部工作完毕
            if(0 >= acm.getThreadCount()){
                // 打印出结果
                WordsAnalysis.show(acm);
                return;
            }
        }
    }
}