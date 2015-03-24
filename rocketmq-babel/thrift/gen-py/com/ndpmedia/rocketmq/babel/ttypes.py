#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class MessageExt:
  """
  Attributes:
   - topic
   - flag
   - properties
   - data
   - queueId
   - storeSize
   - queueOffset
   - sysFlag
   - bornTimestamp
   - bornHost
   - storeTimestamp
   - storeHost
   - msgId
   - commitLogOffset
   - bodyCRC
   - reconsumeTimes
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'topic', None, None, ), # 1
    (2, TType.I32, 'flag', None, 0, ), # 2
    (3, TType.MAP, 'properties', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.STRING, 'data', None, None, ), # 4
    (5, TType.I32, 'queueId', None, None, ), # 5
    (6, TType.I32, 'storeSize', None, None, ), # 6
    (7, TType.I64, 'queueOffset', None, None, ), # 7
    (8, TType.I32, 'sysFlag', None, None, ), # 8
    (9, TType.I64, 'bornTimestamp', None, None, ), # 9
    (10, TType.STRING, 'bornHost', None, None, ), # 10
    (11, TType.I64, 'storeTimestamp', None, None, ), # 11
    (12, TType.STRING, 'storeHost', None, None, ), # 12
    (13, TType.STRING, 'msgId', None, None, ), # 13
    (14, TType.I64, 'commitLogOffset', None, None, ), # 14
    (15, TType.I64, 'bodyCRC', None, None, ), # 15
    (16, TType.I32, 'reconsumeTimes', None, None, ), # 16
  )

  def __init__(self, topic=None, flag=thrift_spec[2][4], properties=None, data=None, queueId=None, storeSize=None, queueOffset=None, sysFlag=None, bornTimestamp=None, bornHost=None, storeTimestamp=None, storeHost=None, msgId=None, commitLogOffset=None, bodyCRC=None, reconsumeTimes=None,):
    self.topic = topic
    self.flag = flag
    self.properties = properties
    self.data = data
    self.queueId = queueId
    self.storeSize = storeSize
    self.queueOffset = queueOffset
    self.sysFlag = sysFlag
    self.bornTimestamp = bornTimestamp
    self.bornHost = bornHost
    self.storeTimestamp = storeTimestamp
    self.storeHost = storeHost
    self.msgId = msgId
    self.commitLogOffset = commitLogOffset
    self.bodyCRC = bodyCRC
    self.reconsumeTimes = reconsumeTimes

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.topic = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.flag = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.properties = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString();
            _val6 = iprot.readString();
            self.properties[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.data = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.queueId = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.storeSize = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.queueOffset = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.sysFlag = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.bornTimestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.bornHost = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I64:
          self.storeTimestamp = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.STRING:
          self.storeHost = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.STRING:
          self.msgId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.I64:
          self.commitLogOffset = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.I64:
          self.bodyCRC = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.I32:
          self.reconsumeTimes = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MessageExt')
    if self.topic is not None:
      oprot.writeFieldBegin('topic', TType.STRING, 1)
      oprot.writeString(self.topic)
      oprot.writeFieldEnd()
    if self.flag is not None:
      oprot.writeFieldBegin('flag', TType.I32, 2)
      oprot.writeI32(self.flag)
      oprot.writeFieldEnd()
    if self.properties is not None:
      oprot.writeFieldBegin('properties', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.properties))
      for kiter7,viter8 in self.properties.items():
        oprot.writeString(kiter7)
        oprot.writeString(viter8)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.STRING, 4)
      oprot.writeString(self.data)
      oprot.writeFieldEnd()
    if self.queueId is not None:
      oprot.writeFieldBegin('queueId', TType.I32, 5)
      oprot.writeI32(self.queueId)
      oprot.writeFieldEnd()
    if self.storeSize is not None:
      oprot.writeFieldBegin('storeSize', TType.I32, 6)
      oprot.writeI32(self.storeSize)
      oprot.writeFieldEnd()
    if self.queueOffset is not None:
      oprot.writeFieldBegin('queueOffset', TType.I64, 7)
      oprot.writeI64(self.queueOffset)
      oprot.writeFieldEnd()
    if self.sysFlag is not None:
      oprot.writeFieldBegin('sysFlag', TType.I32, 8)
      oprot.writeI32(self.sysFlag)
      oprot.writeFieldEnd()
    if self.bornTimestamp is not None:
      oprot.writeFieldBegin('bornTimestamp', TType.I64, 9)
      oprot.writeI64(self.bornTimestamp)
      oprot.writeFieldEnd()
    if self.bornHost is not None:
      oprot.writeFieldBegin('bornHost', TType.STRING, 10)
      oprot.writeString(self.bornHost)
      oprot.writeFieldEnd()
    if self.storeTimestamp is not None:
      oprot.writeFieldBegin('storeTimestamp', TType.I64, 11)
      oprot.writeI64(self.storeTimestamp)
      oprot.writeFieldEnd()
    if self.storeHost is not None:
      oprot.writeFieldBegin('storeHost', TType.STRING, 12)
      oprot.writeString(self.storeHost)
      oprot.writeFieldEnd()
    if self.msgId is not None:
      oprot.writeFieldBegin('msgId', TType.STRING, 13)
      oprot.writeString(self.msgId)
      oprot.writeFieldEnd()
    if self.commitLogOffset is not None:
      oprot.writeFieldBegin('commitLogOffset', TType.I64, 14)
      oprot.writeI64(self.commitLogOffset)
      oprot.writeFieldEnd()
    if self.bodyCRC is not None:
      oprot.writeFieldBegin('bodyCRC', TType.I64, 15)
      oprot.writeI64(self.bodyCRC)
      oprot.writeFieldEnd()
    if self.reconsumeTimes is not None:
      oprot.writeFieldBegin('reconsumeTimes', TType.I32, 16)
      oprot.writeI32(self.reconsumeTimes)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.topic is None:
      raise TProtocol.TProtocolException(message='Required field topic is unset!')
    if self.data is None:
      raise TProtocol.TProtocolException(message='Required field data is unset!')
    if self.msgId is None:
      raise TProtocol.TProtocolException(message='Required field msgId is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.topic)
    value = (value * 31) ^ hash(self.flag)
    value = (value * 31) ^ hash(self.properties)
    value = (value * 31) ^ hash(self.data)
    value = (value * 31) ^ hash(self.queueId)
    value = (value * 31) ^ hash(self.storeSize)
    value = (value * 31) ^ hash(self.queueOffset)
    value = (value * 31) ^ hash(self.sysFlag)
    value = (value * 31) ^ hash(self.bornTimestamp)
    value = (value * 31) ^ hash(self.bornHost)
    value = (value * 31) ^ hash(self.storeTimestamp)
    value = (value * 31) ^ hash(self.storeHost)
    value = (value * 31) ^ hash(self.msgId)
    value = (value * 31) ^ hash(self.commitLogOffset)
    value = (value * 31) ^ hash(self.bodyCRC)
    value = (value * 31) ^ hash(self.reconsumeTimes)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Message:
  """
  Attributes:
   - topic
   - flag
   - properties
   - data
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'topic', None, None, ), # 1
    (2, TType.I32, 'flag', None, 0, ), # 2
    (3, TType.MAP, 'properties', (TType.STRING,None,TType.STRING,None), None, ), # 3
    (4, TType.STRING, 'data', None, None, ), # 4
  )

  def __init__(self, topic=None, flag=thrift_spec[2][4], properties=None, data=None,):
    self.topic = topic
    self.flag = flag
    self.properties = properties
    self.data = data

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.topic = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.flag = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.properties = {}
          (_ktype10, _vtype11, _size9 ) = iprot.readMapBegin()
          for _i13 in xrange(_size9):
            _key14 = iprot.readString();
            _val15 = iprot.readString();
            self.properties[_key14] = _val15
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.data = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Message')
    if self.topic is not None:
      oprot.writeFieldBegin('topic', TType.STRING, 1)
      oprot.writeString(self.topic)
      oprot.writeFieldEnd()
    if self.flag is not None:
      oprot.writeFieldBegin('flag', TType.I32, 2)
      oprot.writeI32(self.flag)
      oprot.writeFieldEnd()
    if self.properties is not None:
      oprot.writeFieldBegin('properties', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.properties))
      for kiter16,viter17 in self.properties.items():
        oprot.writeString(kiter16)
        oprot.writeString(viter17)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.STRING, 4)
      oprot.writeString(self.data)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.topic is None:
      raise TProtocol.TProtocolException(message='Required field topic is unset!')
    if self.data is None:
      raise TProtocol.TProtocolException(message='Required field data is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.topic)
    value = (value * 31) ^ hash(self.flag)
    value = (value * 31) ^ hash(self.properties)
    value = (value * 31) ^ hash(self.data)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)