# DICOM to MCNP parser

DICOM-MCNP-Parser is a DICOM to MCNP parser written in python. This parser can read a DICOM file section and convert to MCNP file.

This code was developed by Cheng Yi in his graduation thesis under supervision of Ilker Meric and Icaro Valgueiro Malta Moreira.

Supported by Høgskulen på Vestlandet and Tianjin University of Technology.

# Installation

Download the dicom_mcnp_parser.py file and add to your project.

# Usage

Import the package "dicom_mcnp_parser".

```python
import dicom_mcnp_parser
```

Call "parse_dicom()" function, passing the path to the dicom file and the path to the exported imp(mcnp) file.

```python

import dicom_mcnp_parser

parse_dicom("80_dicom_125mm.dcm", "80_dicom_125mm.imp")

```
# Features

 - Parser from MCNP

# Contributors

* Cheng Yi ([ChengYi1997][])
* Icaro Valgueiro Malta Moreira ([ivmmoreira][])

[ChengYi1997]:            https://github.com/ChengYi1997
[ivmmoreira]:  https://github.com/ivmmoreira
