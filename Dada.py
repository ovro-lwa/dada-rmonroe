import cDada

class SortedDada(cDada.SortedDada):
	def __len__(self):
		return self.header.nTime()

	def _reshape(self, arr):
		return arr.reshape((self.header.nBaseline(), self.header.nFreq(), self.header.nCorr()))

	def rGetChunk(self, i):
		return self._reshape(cDada.SortedDada.rGetChunk(self, i))

	def rNextChunk(self):
		return self._reshape(cDada.SortedDada.rNextChunk(self))

	def applyGains(self, gains, gainFlags):
		return cDada.SortedDada.applyGains(self, gains, gainFlags.astype('int8'))

	def currentVisFlags(self):
		return self._reshape(self.rCurrentVisFlags()).astype('bool')

	def __getitem__(self, i):
		if i < len(self):
			return self.rGetChunk(i).copy()
		else:
			raise IndexError

	def __iter__(self):
		self.rewind()
		return self

	def next(self):
		if self.prevChunkIndex() < len(self) - 1:
			return self.rNextChunk()
		else:
			raise StopIteration
	
	def __str__(self):
		return '<Dada.SortedDada("%s")>' % self.filename()
