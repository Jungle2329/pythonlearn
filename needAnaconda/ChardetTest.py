import chardet

# 编码测试
print(chardet.detect(b'123k1j23klj1l3'))
print(chardet.detect('天王盖地虎天王盖地虎天王盖地虎'.encode('gbk')))
print(chardet.detect('积分卡的回复接口回调扣几分号地块交话费'.encode('utf-8')))
print(chardet.detect('最新の主要ニュース'.encode('euc-jp')))
