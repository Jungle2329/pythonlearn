import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


async def do_io(time):
    await asyncio.sleep(time)
    print('do something for {} time'.format(time))
    return 'Done after {}s'.format(time)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    tasks = [asyncio.ensure_future(do_io(time)) for time in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
        print(task.result())
    loop.close()

