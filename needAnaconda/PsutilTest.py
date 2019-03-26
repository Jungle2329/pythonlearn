import psutil

# 获取CPU相关
# print(psutil.cpu_count(logical=False))
# while True:
# print(psutil.cpu_percent(interval=2, percpu=True))

# 获取磁盘相关
# print(psutil.disk_usage('c:/'))
# print(psutil.disk_usage('d:/'))
# print(psutil.disk_usage('e:/'))
# print(psutil.disk_usage('f:/'))
# print(psutil.disk_partitions())

# 获取IO相关
# print(psutil.net_connections())
# print(psutil.net_if_addrs())
# print(psutil.net_if_stats())
# print(psutil.net_io_counters())

# 进程相关
# print(psutil.pids())
# print(psutil.pid_exists(1111111))
# p = psutil.Process(892)
# print(p.name())
# print(psutil.test())
while True:
    mPid = input('输入pid: ')
    iPid = int(mPid)
    if psutil.pid_exists(int(iPid)):
        p = psutil.Process(iPid)
        print(p.name())
        print(p.username())
        print(p.cpu_percent())
        print(p.cpu_times())
        print(p.exe())
    else:
        print('没有此进程')


# p = psutil.Process(8188)  # 获取指定进程ID=3776，其实就是当前Python交互环境
# p.name()  # 进程名称
# # 'python3.6'
# p.exe()  # 进程exe路径
# # '/Users/michael/anaconda3/bin/python3.6'
# p.cwd()  # 进程工作目录
# # '/Users/michael'
# p.cmdline()  # 进程启动的命令行
# # ['python3']
# p.ppid()  # 父进程ID
# # 3765
# p.parent()  # 父进程
# # <psutil.Process(pid=3765, name='bash') at 4503144040>
# p.children()  # 子进程列表
# # []
# p.status()  # 进程状态
# # 'running'
# p.username()  # 进程用户名
# # 'michael'
# p.create_time()  # 进程创建时间
# # 1511052731.120333
# # p.terminal()  # 进程终端
# # '/dev/ttys002'
# p.cpu_times()  # 进程使用的CPU时间
# # pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
# p.memory_info()  # 进程使用的内存
# # pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
# p.open_files()  # 进程打开的文件
# # []
# p.connections()  # 进程相关网络连接
# []
# p.num_threads()  # 进程的线程数量
# # 1
# p.threads()  # 所有线程信息
# # [pthread(id=1, user_time=0.090318, system_time=0.062736)]
# p.environ()  # 进程环境变量
# # {'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
# #  p.terminate() # 结束进程
# # Terminated: 15 <-- 自己把自己结束了
