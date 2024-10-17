# 进程是执行中的程序，拥有独立地址空间、内存、数据栈等
# 由操作系统统一管理，派生新进程，进程间通信（IPC）方式共享信息
import _thread
from time import sleep, ctime
import logging
# 日志初始化,日志输出等级INFO，所有info级别的日志都会打印和输出
logging.basicConfig(level=logging.INFO)

def loop0():
    # ctime 导入当前时间
    logging.info("start loop0 at" + ctime())
    sleep(4)
    logging.info("end loop0 at" + ctime())

def loop1():
    logging.info("start loop1 at" + ctime())
    sleep(2)
    logging.info("end loop1 at" + ctime())

# 主函数main，可以分别调用上面两个方法
def main():
    logging.info("start all at" + ctime())
    # loop0()
    # 多线程处理
    _thread.start_new_thread(loop0, ())
    # loop1()
    _thread.start_new_thread(loop1, ())
    # 主线程等待6秒
    sleep(6)
    logging.info("end all at" + ctime())

if __name__ == '__main__':
    main()