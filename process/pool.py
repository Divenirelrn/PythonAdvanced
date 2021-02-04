import multiprocessing
import time

def func(msg):
    print("msg:", msg)
    time.sleep(2)
    print("end")

def func2(msg1, msg2):
    print("msg1:", msg1, "msg2:", msg2)
    time.sleep(2)
    print("end")

def func3(msg):
    print("msg:", msg)
    time.sleep(4-msg)
    return msg

if __name__ == "__main__":
    pool = multiprocessing.Pool()
    # apply 和 apply_async 一次执行一个任务，但 apply_async 可以异步执行，因而也可以实现并发
    # for i in range(2):
    #     msg = "hello %d" % (i)
    #     # pool.apply(func, (msg,))
    #     pool.apply_async(func, (msg,))

    #map 和 map_async 与 apply 和 apply_async 的区别是可以并发执行任务
    # pool.map(func, range(2)) #阻塞到任务列表中所有任务完成再往下执行
    # pool.map_async(func, range(2)) #异步，任务执行时不阻塞

    #starmap 和 starmap_async 与 map 和 map_async 的区别是，starmap 和 starmap_async 可以传入多个参数
    # msgs = [(1, 1), (2, 2)]
    # pool.starmap(func2, msgs) #阻塞
    # pool.starmap_async(func2, msgs) #异步

    """
    imap 和 imap_unordered 与 map_async 同样是异步，区别是:
        map_async生成子进程时使用的是list，而imap和 imap_unordered则是Iterable，map_async效率略高，而imap和 imap_unordered内存消耗显著的小。
        在处理结果上，imap 和 imap_unordered 可以尽快返回一个Iterable的结果，而map_async则需要等待全部Task执行完毕，返回list。
        而imap 和 imap_unordered 的区别是：imap 和 map_async一样，都按顺序等待Task的执行结果，而imap_unordered则不必。 
        imap_unordered返回的Iterable，会优先迭代到先执行完成的Task。
        
        在获取进程池中的结果时，map_async、imap、imap_unordered三个方法都会阻塞。
        map_async 与 imap、imap_unordered区别是：map_async需要等待所有Task执行结束后返回list，而imap 和 imap_unordered 可以尽快返回一个Iterable的结果。
        imap 和 imap_unordered 的区别是：imap 和 map_async一样，都按顺序等待Task的执行结果，而imap_unordered则不必。 
        imap_unordered返回的Iterable，会优先迭代到先执行完成的Task。
    """
    # results = pool.map_async(func3, range(3)) #list、有序
    # for res in results.get():
    #     print(res)
    # results = pool.imap(func3, range(3)) #iterable、有序
    results = pool.imap_unordered(func3, range(3)) #iterable、无序
    for res in results:
        print(res)


    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()
    print("Sub-process(es) done.")
