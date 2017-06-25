# [Pars Green Soap Client][docs]

**Easy to work with Pars Green SOAP client**

Full documentation for the project is available at [Pars Green Soap Client PDF][pdf].

---

# Overview



# Requirements

* Python (2.7, 3.2, 3.3, 3.4, 3.5, 3.6)
* suds (0.4.0)

# Installation

Install using `pip`...

    pip install pars-green

# Example

Let's take a look at a quick example of using this package to send SMS:

    from pars_green import ParsGreenSmsServiceClient
    client = ParsGreenSmsServiceClient("YOUR_SIGNATURE")
    print(client.send('SENDER_NUMBER', 'TO_NUMBER', 'TEXT'))

# Documentation & Support

For more information about this package, see [python website][pypi]

For questions and support, contact to [Author's mail][mail].

You may also want to [follow the author on Twitter][twitter].

[pypi]: https://pypi.python.org/pypi/pars-green
[twitter]: https://twitter.com/mhipo1364
[mail]: mailto:mhipo1364@gmail.com
[pdf]: https://github.com/mhipo1364/pars-green/blob/master/docs/pdf/parsgreen.pdf
[docs]: https://github.com/mhipo1364/pars-green/blob/master/README.md