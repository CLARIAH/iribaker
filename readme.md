## IRI Baker ##

Simple library for baking RFC3987 compliant IRIs from IRI-like strings.

#### Installation

Run `python setup.py install`

#### Usage

* Import the package (`import iribaker`)
* Call `iribaker.to_iri(string)` with the string you want to check (utf-8 and unicode supported)
* For example: `iri = iribaker.to_iri('http://example.com/€eéf')`
* The function returns:
  * The same (unicode) string, if it is a valid IRI
  * A string where each invalid character is replaced with an underscore (`_`). This means no roundtripping!
  * A quoted version of the string (using the standard `urllib.quote`)

#### License

This software is made available under the MIT license (see LICENSE for details)
