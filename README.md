<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![Documentation Status](https://readthedocs.org/projects/pyevals/badge/?version=latest)](https://pyevals.readthedocs.io/en/latest/?badge=latest)
[![Apache V2 License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/anirudhpnbb/Pyevals/blob/master/imgs/img.png)

A very elegant and simple library to evaluate models. In this version we are only providing the reports,
but soon we will be adding plots too.
### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://python.com)

<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
```sh
git clone https://github.com/anirudhpnbb/Pyevals.git
```

2. Install using pip or pip3
```commandline
pip3 install Pyevals==1.0.1
```



<!-- USAGE EXAMPLES -->
## Usage

```python
import pyevals

# For classification
pyevals.evaluate(actual, predicted, reports=True, method = 'Classification')

# For regression
pyevals.evaluate(actual, predicted, method = 'Regression',reports=True,
                samples_size=None, number_of_independent_columns=None)   
```


<!-- LICENSE -->
## License

Distributed under the APACHE LICENSE, VERSION 2.0. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Anirudh Palaparthi - [@anirudh8889](https://twitter.com/anirudh8889) - aniruddhapnbb@gmail.com

Project Link: [https://github.com/anirudhpnbb/Pyevals](https://github.com/anirudhpnbb/Pyevals)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Readme Template](https://github.com/othneildrew/Best-README-Template)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/badge/contributors-1-blue
[contributors-url]: https://github.com/anirudhpnbb/Pyevals/graphs/contributors
[issues-shield]: https://img.shields.io/badge/Issues-0-green
[issues-url]: https://github.com/anirudhpnbb/Pyevals/issues
[license-shield]: https://img.shields.io/badge/LICENSE-ApacheV2-brightgreen
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/pnbbanirudh
[product-screenshot]: imgs/img.png
