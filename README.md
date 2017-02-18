# ToroExact

ToroExact is a Python program meant to generate exact solutions to Riemann problems for the Euler equations of hydrodynamics, based on the solver of Toro (1999). By default, the seven verification test problems provided by Toro are included. Additionally, user-defined problems may be specified on the command line.

## Installation

```
git clone https://github.com/tahandy/ToroExact.git
````

## Files
**toro_exact.py:** Driver script which parses user input and calls the Riemann solver

**exactRP.py:** File containing *exactRP* class, which encapsulates the Riemann problem data and solution methods

## Usage

```

usage: toro_exact.py [-h] -p {1,2,3,4,5,6,7,all,user} [-g GAMMA]
                     [-d {zonal,nodal}] [-n NPTS] [-b BOUNDS] [-l STATEL]
                     [-r STATER] [-x X0] [-t TIME]

optional arguments:
  -h, --help            show this help message and exit
  -p {1,2,3,4,5,6,7,all,user}, --problem {1,2,3,4,5,6,7,all,user}
                        select which problem to solve
  -g GAMMA, --gamma GAMMA
                        set ideal gas gamma
  -d {zonal,nodal}, --disc {zonal,nodal}
                        set discretization [zonal, nodal]
  -n NPTS, --npts NPTS  set number of evaluation points
  -b BOUNDS, --bounds BOUNDS
                        set domain boundaries

  -l STATEL, --left STATEL
                        set user left state "[dens, vel, pres]"
  -r STATER, --right STATER
                        set user right state "[dens, vel, pres]"
  -x X0, --x0 X0        set user diapgram location
  -t TIME, --time TIME  set user evaluation time
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## Credits

TODO: Write credits

## License

TODO: Write license