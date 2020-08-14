# coding=utf8
__author__ = "pamxiuqiang"
__data__ = ' $ TIME'

from ctypes import *
import struct


# BigEndianStructure  LittleEndianStructure
class SSHead(LittleEndianStructure):  # Python与C tcp载荷封包加载器
    _pack_ = 1  # 对齐
    _fields_ = [
        # (字段名, c类型 )
        ('header', c_uint32),  # 包头
        ('cmd_type', c_int16),  # 命令类型
        ('payload_length', c_uint16),  # 载荷长度
    ]

    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)

    def pack(self):
        buffer = struct.pack("!IHH", self.header, self.cmd_type, self.payload_length
                             , self.baord_id, self.channel_id, self.addr_start, self.data_len, self.name, self.yan)
        return buffer

    def unpack(self, data):
        (self.header, self.cmd_type, self.payload_length) = struct.unpack("!IHH", data)


class SSDATA(LittleEndianStructure):  # Python与C tcp载荷封包加载器
    _pack_ = 1  # 对齐
    _fields_ = [
        # (字段名, c类型 )
        ('baord_id', c_uint32),  # 板块ID
        ('channel_id', c_uint32),  # ch ID
        ('addr_start', c_int64),  # 起始地址
        ('data_len', c_uint64),  # 数据长度
        ('name', c_uint64),  #
    ]

    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)

    def pack(self):
        buffer = struct.pack("!IIQQQIIQQQIIQQQIIQQQIIQQQ", self.baord_id, self.channel_id, self.addr_start,
                             self.data_len, self.name)
        return buffer

    def unpack(self, data):
        (self.baord_id, self.channel_id,
         self.addr_start, self.data_len, self.name) = struct.unpack("!IIQQQIIQQQIIQQQIIQQQIIQQQ", data)


class SSEND(LittleEndianStructure):  # Python与C tcp载荷封包加载器 
    _pack_ = 1  # 对齐
    _fields_ = [
        # (字段名, c类型 )
        ('yan', c_uint16)  # 校验
    ]

    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)

    def pack(self):
        buffer = struct.pack("!H", self.yan)
        return buffer

    def unpack(self, data):
        self.yan = struct.unpack("!H", data)


class SSdecode(LittleEndianStructure):  # Python与C tcp载荷封包加载器
    _pack_ = 1  # 对齐
    _fields_ = [
        # (字段名, c类型 )
        ('header', c_uint32),  # 包头i4 2 2 4 4 8 8 8 2
        ('cmd_type', c_int16),  # 命令类型
        ('payload_length', c_uint16),  # 载荷长度
        ('baord_id', c_uint32),  # 板块ID
        ('channel_id', c_uint32),  # ch ID
        ('addr_start', c_int64),  # 起始地址
        ('data_len', c_uint64),  # 数据长度
        ('name', c_uint64),  #
        ('yan', c_uint16)  # 校验
    ]

    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        datas = memmove(addressof(self), data, sizeof(self))
        return datas

    def pack(self):
        buffer = struct.pack("!IHHIIQQQIIQQQIIQQQIIQQQIIQQQH", self.header, self.cmd_type, self.payload_length
                             , self.baord_id, self.channel_id, self.addr_start, self.data_len, self.name, self.yan)
        return buffer

    def unpack(self, data):
        (self.header, self.cmd_type, self.payload_length, self.baord_id, self.channel_id,
         self.addr_start, self.data_len, self.name, self.yan) = struct.unpack("!IHHIIQQQIIQQQIIQQQIIQQQIIQQQH", data)





class SSHtime(LittleEndianStructure):  # Python与C tcp载荷封包加载器
    _pack_ = 1  # 对齐
    _fields_ = [
        # (字段名, c类型 )
        ('header', c_uint32),  # 包头
        ('cmd_type', c_int16),  # 命令类型
        ('payload_length', c_uint16),  # 载荷长度
    ]

    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)

    def pack(self):
        buffer = struct.pack("!IHH", self.header, self.cmd_type, self.payload_length
                             , self.baord_id, self.channel_id, self.addr_start, self.data_len, self.name, self.yan)
        return buffer

    def unpack(self, data):
        (self.header, self.cmd_type, self.payload_length) = struct.unpack("!IHH", data)
#
# class SStime(LittleEndianStructure):  # Python与C tcp载荷封包加载器
#     _pack_ = 1  # 对齐
#     _fields_ = [
#         # (字段名, c类型 )
#         ('year', c_uint),  # 包头i4 2 2 4 4 8 8 8 2
#         ('cmd_type', c_int16),  # 命令类型
#         ('payload_length', c_uint16),  # 载荷长度
#         ('baord_id', c_uint32),  # 板块ID
#         ('channel_id', c_uint32),  # ch ID
#         ('addr_start', c_int64),  # 起始地址
#         ('data_len', c_uint64),  # 数据长度
#         ('name', c_uint64),  #
#         ('yan', c_uint16)  # 校验
#     ]
#

"""
class SSEND(LittleEndianStructure):  # Python与C tcp载荷封包加载器 
    _fields_head_ = [
		('header', c_uint32),  # 包头
        ('cmd_type', c_int32), # 命令类型
        ('payload_length', c_uint16), # 载荷长度
	]
	
    _fields_data_ =[
	  ('baord_id', c_uint32), # 板块ID
        ('channel_id', c_uint32), # ch ID
        ('addr_start', c_int64),  # 起始地址
        ('data_len', c_uint64),  # 数据长度
        ('name', c_uint64),  #
	]
	

    _fields_check_ =[
	   ('check', c_uint16), # 校验 
	]
	
    _pack_ = 1  #对齐
    _pack_msg_ =[
	_fields_head_,
	_fields_data_*5,
	_fields_check_
	]
    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)
		
"""
