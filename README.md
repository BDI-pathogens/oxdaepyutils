# oxdaepyutils
Python utilities from the Oxford University Pandemic Sciences Institute (PSI) Data Analytics &amp; Epidemiology (DAE) research group


## Python modules

There are various utilities and modules you can use. These are briefly described below.

### Data anonymisation

The Anonymiser class takes a Pandas Series or python array and generates anonymised, but consistent, values. This values map is then saved in the specified mappings file. The resultant data can then be kept away from the mappings file to be used as an anonymised dataset. There is no relation between the source data and the anonymous value, so reverse engineering is not possible without the mappings file. An existing mappings file can be used to consistently generate anonymous identifiers over time. E.g. for during a clinical trial.

## Themes

In the `/themes` folder we include themes used with Python libraries for convenience.

### PSI Matplotlib Theme

I created a matplotlib theme based on the Pandemic Science Institutes brand and style guidelines.
This provides a better data output starting point and makes it easier to integrate data to our
publications in future.

- The stylesheet can be found in `/themes/psi.mpltstyle`.
- An example of how it looks is in [/docs/images/psi-theme-example.png](docs/images/psi-theme-example.png)
- An example of its use can be found in [/samples/teststyles.py](samples/teststyles.py)

## License and Copyright

Unless otherwise stated, all code is copyright the original authors and the University of Oxford. The moral rights of the authors have been asserted.

Unless otherwise stated, all code in these repositories is licensed under the Apache-2.0 license, and all documentation and images under the CC-BY-4.0 license.