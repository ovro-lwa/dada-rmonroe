#include "SortedDada.h"
#include <iostream>

int
main()
{
	dada::SortedDada d("2014-04-30-01:21:56_0000536774737920.000000.dada");
	d.setLineMappingFromFile("remap-danny2014.04.30.txt");

	std::cout << "nAnt: " << d.header.nAnt() << std::endl;
	std::cout << "cFreq: " << d.header.cFreq() << std::endl;
	std::cout << "nFreq: " << d.header.nFreq() << std::endl;

	for (int i=0; i<d.header.nTime(); ++i) {
		// v is in baseline,frequency,pol order
		std::vector<std::complex<float> > v = d.rNextChunk();
		std::cout << v[10000] << std::endl;
	}

	return 0;
}
