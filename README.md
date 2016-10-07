# lumi2d

Creates a 2D luminosity uncertainty plot in function of rapidity and invariant mass.

## Download

Clone the master development repository by running the following command:

```Shell
$ git clone https://github.com/scarrazza/lumi2d.git
```

Or download the compressed archive without using git
[here](https://github.com/scarrazza/lumi2d/archive/master.zip).

## Installation

lumi2d requires [ROOT](https://root.cern.ch/) and
[LHAPDF](https://lhapdf.hepforge.org/).

Once all dependencies are satisfied, run:

````Shell
$ python setup.py install
```

Note that the installer script does _not_ check for dependencies. This will
install the `lumi2d` program in the appropiate path.

## Usage

````Shell
usage: lumi2d [-h] [-gev GEV] [-bins BINS] [-format FORMAT] pdfname channel

Creates a 2D mx-y luminosity uncertainty plot.

positional arguments:
  pdfname         the LHAPDF pdf set name.
  channel         the luminosity channel: gg,gq,qq,qqbar,udbar,dubar

optional arguments:
  -h, --help      show this help message and exit
  -gev GEV        the sqrts energy for the luminosity (default 13000).
  -bins BINS      the number of bins in y and mx (default 100).
  -format FORMAT  the plot output format (default png).

```

## Example

By running:
````Shell
$ lumi2d PDF4LHC15_nnlo_mc gg
```
we obtain:

![alt text](https://github.com/scarrazza/lumi2d/raw/master/extra/PDF4LHC15_nnlo_mc_gg_13000.0.png "Logo")

