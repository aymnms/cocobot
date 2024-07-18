<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/aymnms/cocobot">
    <img src="images/cocobot.jpg" alt="Logo" width="105" height="120">
  </a>

<h3 align="center">cocobot</h3>

  <p align="center">
    Api of jokes between friends
    <br />
    <a href="https://github.com/aymnms/cocobot/wiki"><strong>Explore the docs</strong></a>
    <br />
    <br />
    <a href="https://github.com/aymnms/cocobot">🔜 <strike>View Demo</strike></a>
    ·
    <a href="https://github.com/aymnms/cocobot/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/aymnms/cocobot/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul><li><a href="#built-with">Built With</a></li></ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Api of jokes between friends

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url] 
* [![Flask][Flask]][Flask-url]
* [![Sqlite][Sqlite]][Sqlite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

You need to install Python and pip

### Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/aymnms/cocobot.git
   ```
2. Install Pip libraries
   ```sh
   $ pip install -r requirements.txt
   ```
3. Database initialization
   ```sh
   $ flask shell
   ```
   Or
   ```sh
   $ python
   >>> from app import app, db
   >>> app.app_context().push()
   >>> db.create_all()
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Execute this command to start the api server
```sh
$ python app.py
```

Then, you can call the api like that

**Ask a random joke**
```sh
$ curl http://127.0.0.1:5000/joke
```

_For more examples, please refer to the [Documentation](https://github.com/aymnms/cocobot/wiki)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] MVP
- [x] Create ios shortcut to use it
- [ ] Search a similar solution for android
- [ ] Improve the project ^^

See the [open issues](https://github.com/aymnms/cocobot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/aymnms/cocobot.svg?style=for-the-badge
[contributors-url]: https://github.com/aymnms/cocobot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/aymnms/cocobot.svg?style=for-the-badge
[forks-url]: https://github.com/aymnms/cocobot/network/members
[stars-shield]: https://img.shields.io/github/stars/aymnms/cocobot.svg?style=for-the-badge
[stars-url]: https://github.com/aymnms/cocobot/stargazers
[issues-shield]: https://img.shields.io/github/issues/aymnms/cocobot.svg?style=for-the-badge
[issues-url]: https://github.com/aymnms/cocobot/issues
[license-shield]: https://img.shields.io/github/license/aymnms/cocobot.svg?style=for-the-badge
[license-url]: https://github.com/aymnms/cocobot/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Sqlite]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[Sqlite-url]: https://www.sqlite.org/
