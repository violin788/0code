exec(open('util.py').read())
#def vol(inp):

def set_volume(self, volume):
    """Set volume for this sink."""
    self.volume = volume
    cvolume = cvolume_from_volume(volume, self.channels)
    self.pa_mgr.set_sink_volume(self.idx, cvolume) 


inp = []
vol(inp)