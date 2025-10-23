"""
Day11 10.22
1. 装饰器： @wrapper
        定义：一个函数，接收另一个函数作为参数，返回一个新的函数，这个新的函数通常会对原函数进行动态修改或增强，且不修改原函数代码
            def wrapper(func):  # 装饰器函数wrapper
                def inner():
                    print(f"函数{func}启用前")
                    func()      # 被装饰函数func
                    print(f"函数{func}启用后")
                return inner
        调用：
            1. 直接调用装饰器，需在要使用装饰器的函数前调用装饰器@wrapper（装饰器名是自定义的函数名）
            2. 通过闭包原理调用装饰器，即将funa传入定义的装饰器函数并返回一个新函数funb，然后每次需要使用funa时就直接调用funb函数以实现装饰器效果。
        装饰器传参：
            当被装饰函数需要接收参数时，需要在装饰器中同样接受参数，以便在装饰器内部调用函数时可以传入需要的参数
            传参格式：可在装饰器中使用(*args, **kwargs)形式接收任意类型的参数，并传入被装饰函数
            如： def wrapper(func):
                    def inner(*args, **kwargs):
                        print(f"函数{func}启用前")
                        func(*args, **kwargs)
                        print(f"函数{func}启用后")
                    return inner

        特点：装饰器的本质是闭包，必须有返回值，且返回值类型为函数
             使用装饰器，可以让函数执行时自动调用另一个函数（该函数仅作为装饰器使用）
        优点：
            1. 装饰器可以实现对原函数的增强，而不需要修改原函数的代码
            2. 装饰器可以实现对原函数的重复利用
        缺点：
            1. 装饰器会增加代码的复杂度、执行时间
            2. 装饰器不能用于类中
            3. 装饰器不能用于嵌套函数
        应用场景：
            1. 日志记录
            2. 性能测试
            3. 安全验证
            4. 缓存
            5. 事务处理
2. 模块和包（补充）
    随机模块：random
        导入：import random
        常用方法：
            1. random.random()：生成0到1之间的随机浮点数
            2. random.randint(start, end)：生成指定范围内的整数
            3. random.randrange(start, stop[, step])：生成指定范围内的整数，start和end是起始和结束的整数，step是步长，默认为1
            4. random.uniform(start, end)：生成指定范围内的浮点数
            5. random.choice(seq)：从序列中随机选择一个元素
            6. random.shuffle(list)：将列表中的元素顺序打乱(洗牌)
            7. random.sample(seq, k)：从序列中随机选择k个元素
            8. random.seed(value)：设置随机种子
            9. random.getstate()：获取当前随机状态
            10.random.setstate(state)：设置当前随机状态
            11.random.randbytes(n)：生成n个随机字节
    时间模块：time
        导入：import time
        常用方法：
            1. time.time()：返回当前时间的时间戳,即从1970年1月1日0时0分0秒到现在的秒数
            2. time.localtime()：返回本地时间的struct_time对象,包含年月日时分秒等信息
            3. time.strftime(format[, t])：将时间转换为指定的格式,format是格式化字符串,t是struct_time对象
            4. time.sleep(seconds)：暂停程序运行一段时间
3. 高阶函数
    filter(function, iterable)：对可迭代对象中的每一个元素都执行function操作，返回一个新的可迭代对象
            对可迭代对象中的每个元素用function进行筛选,function返回值必须为Bool值，筛选选中的元素保存在一个fileter对象中返回。
    map(function, iterable)：对可迭代对象中的每一个元素都执行function操作，返回一个新的可迭代对象（map对象）
            function可以返回任意值
    reduce(function, iterable)：对可迭代对象中的元素进行累积计算，初始值为第一个元素，每次计算结果作为下一次计算的初始值

4. 多线程、多进程
    并发：多个任务交替执行（同一时间只有一个任务在运行，由于快速切换造成‘同时执行’的错觉）
    并行：多个任务同时执行（需多核CPU支持）
    多线程（并发）：多个线程同时执行，每个线程都有自己的任务和执行顺序，可以提高程序的执行效率
        线程：进程内的一个执行单元。一个进程可包含多个线程，线程共享进程的内存资源。线程是轻量级的，创建和切换成本低，但受Python全局解释器锁(GIL)限制。
            1. 创建线程：threading.Thread(target=函数名, args=(参数列表))
            2. 启动线程：thread.start()
            3. 等待线程结束：thread.join()
            4. 终止线程：thread.terminate()
            5. 判断线程是否活着：thread.is_alive()
            6. 获取线程ID：thread.ident
            7. 获取线程名字：thread.getName()
            8. 设置线程名字：thread.setName(name)
            9. 获取线程对象：thread.getObject()
            10. 获取线程状态：thread.isAlive()
    多进程（并行）：多个进程同时执行，每个进程都有自己的任务和执行顺序，可以提高程序的执行效率
                多进程必须在main模块中启动
            1. 创建进程：multiprocessing.Process(target=函数名, args=(参数列表))
            2. 启动进程：process.start()
            3. 等待进程结束：process.join()
            4. 终止进程：process.terminate()
            5. 判断进程是否活着：process.is_alive()
            6. 获取进程ID：process.pid
            7. 获取进程名字：process.name
            8. 设置进程名字：process.name = name
            9. 获取进程对象：process.getObject()
            10. 获取进程状态：process.isAlive()

5.
    isInstance(obj, classinfo)：判断对象是否是某个类的实例
    issubclass(cls, classinfo)：判断类是否是某个类的子类
"""



# 定义装饰器：接受一个函数做参数
def wrapper(func):
    def inner(*args, **kwargs):
        print(f"函数{func}启用前")
        func(*args, **kwargs)
        print(f"函数{func}启用后")
    return inner

# 使用装饰器
@wrapper
def fun1():
    print("正在执行fun1")

# 需要参数的被装饰函数
@wrapper
def fun2(name, age, gender):
    print(f"fun2:{name}, {age}, {gender}")

# 多线程
def threads():
    import threading
    import time
    def task(name, delay):
        for i in range(5):
            print(f"{name}执行第{i+1}次")
            time.sleep(delay)       # 线程暂时休眠，释放GIL供其他线程使用，达到交替执行效果
    t1 = threading.Thread(target=task, args=('线程1', 3))
    t2 = threading.Thread(target=task, args=('线程2', 5))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("主线程执行完毕")
    return None
# 多进程
import multiprocessing
import time
def task(name, delay):
    for i in range(5):
        print(f"{name}执行第{i + 1}次")
        time.sleep(delay)
if __name__ == '__main__':
    # 1. 装饰器
    #   1.直接调用装饰器，需在fun1函数前调用装饰器@wrapper
    # fun1()
    #   2.通过闭包原理调用装饰器
    # wrap = wrapper(fun1)
    # wrap()
    #   3.装饰器传参
    # fun2('张三', 20, '男')
    pass
    # 4. 多线程
    # threads()
    # 4. 多进程
    p1 = multiprocessing.Process(target=task, args=("进程1", 2))
    p2 = multiprocessing.Process(target=task, args=("进程2", 5))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("主进程执行完毕")