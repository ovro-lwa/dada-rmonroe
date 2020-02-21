# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cDada', [dirname(__file__)])
        except ImportError:
            import _cDada
            return _cDada
        if fp is not None:
            try:
                _mod = imp.load_module('_cDada', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cDada = swig_import_helper()
    del swig_import_helper
else:
    import _cDada
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class DadaHeader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DadaHeader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DadaHeader, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cDada.new_DadaHeader(*args)
        try: self.this.append(this)
        except: self.this = this
    def nAnt(self): return _cDada.DadaHeader_nAnt(self)
    def nTime(self): return _cDada.DadaHeader_nTime(self)
    def nFreq(self): return _cDada.DadaHeader_nFreq(self)
    def nPol(self): return _cDada.DadaHeader_nPol(self)
    def nCorr(self): return _cDada.DadaHeader_nCorr(self)
    def intTime(self): return _cDada.DadaHeader_intTime(self)
    def cFreq(self): return _cDada.DadaHeader_cFreq(self)
    def bandwidth(self): return _cDada.DadaHeader_bandwidth(self)
    def channelBandwidth(self): return _cDada.DadaHeader_channelBandwidth(self)
    def channelFreq(self, *args): return _cDada.DadaHeader_channelFreq(self, *args)
    def startTime(self): return _cDada.DadaHeader_startTime(self)
    def finishTime(self): return _cDada.DadaHeader_finishTime(self)
    def startTimeMJD(self): return _cDada.DadaHeader_startTimeMJD(self)
    def finishTimeMJD(self): return _cDada.DadaHeader_finishTimeMJD(self)
    def nBaseline(self): return _cDada.DadaHeader_nBaseline(self)
    def headerSize(self): return _cDada.DadaHeader_headerSize(self)
    def rawValues(self): return _cDada.DadaHeader_rawValues(self)
    __swig_getmethods__["str2epoch"] = lambda x: _cDada.DadaHeader_str2epoch
    if _newclass:str2epoch = staticmethod(_cDada.DadaHeader_str2epoch)
    __swig_getmethods__["unix2mjd"] = lambda x: _cDada.DadaHeader_unix2mjd
    if _newclass:unix2mjd = staticmethod(_cDada.DadaHeader_unix2mjd)
    __swig_destroy__ = _cDada.delete_DadaHeader
    __del__ = lambda self : None;
DadaHeader_swigregister = _cDada.DadaHeader_swigregister
DadaHeader_swigregister(DadaHeader)

def DadaHeader_str2epoch(*args):
  return _cDada.DadaHeader_str2epoch(*args)
DadaHeader_str2epoch = _cDada.DadaHeader_str2epoch

def DadaHeader_unix2mjd(*args):
  return _cDada.DadaHeader_unix2mjd(*args)
DadaHeader_unix2mjd = _cDada.DadaHeader_unix2mjd

class SortedDada(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SortedDada, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SortedDada, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _cDada.new_SortedDada(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_getmethods__["header"] = _cDada.SortedDada_header_get
    if _newclass:header = _swig_property(_cDada.SortedDada_header_get)
    def inputSize(self): return _cDada.SortedDada_inputSize(self)
    def outputSize(self): return _cDada.SortedDada_outputSize(self)
    def setLineMapping(self, *args): return _cDada.SortedDada_setLineMapping(self, *args)
    def setLineMappingFromFile(self, *args): return _cDada.SortedDada_setLineMappingFromFile(self, *args)
    def applyGains(self, *args): return _cDada.SortedDada_applyGains(self, *args)
    def resetGains(self): return _cDada.SortedDada_resetGains(self)
    def rRawChunk(self, *args): return _cDada.SortedDada_rRawChunk(self, *args)
    def rGetChunk(self, *args): return _cDada.SortedDada_rGetChunk(self, *args)
    def rNextChunk(self): return _cDada.SortedDada_rNextChunk(self)
    def rCurrentVisFlags(self): return _cDada.SortedDada_rCurrentVisFlags(self)
    def prevChunkIndex(self): return _cDada.SortedDada_prevChunkIndex(self)
    def filename(self): return _cDada.SortedDada_filename(self)
    def rewind(self): return _cDada.SortedDada_rewind(self)
    __swig_destroy__ = _cDada.delete_SortedDada
    __del__ = lambda self : None;
SortedDada_swigregister = _cDada.SortedDada_swigregister
SortedDada_swigregister(SortedDada)



