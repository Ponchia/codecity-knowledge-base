The concept of "Code City" (representing software systems as 3D cities) was pioneered by **Richard Wettel** and **Michele Lanza** at **USI (University of the Italian Switzerland)** in Lugano.

Below is a curated list of the seminal research, the original tools, and modern open-source libraries that have evolved from this concept.

### 🏛️ Seminal Research (USI - University of the Italian Switzerland)

The original research that established the metaphor. In this model, **classes are buildings** and **packages are districts**. The height and size of the buildings correspond to metrics like lines of code or complexity.

* **CodeCity Project Homepage**
The original project page by Richard Wettel. Includes the original tool (written in Smalltalk) and screenshots.
* [https://wettel.github.io/codecity.html](https://wettel.github.io/codecity.html)


* **"Visualizing Software Systems as Cities" (2007)**
The foundational paper introducing the metaphor.
* [Read Paper (PDF)](https://www.google.com/search?q=https://www.inf.usi.ch/lanza/Downloads/Wett2007a.pdf)


* **"CodeCity: 3D Visualization of Large-Scale Software" (2008)**
Describes the implementation and the metric mapping (e.g., height = number of methods, base = number of attributes).
* [Read Paper (PDF)](https://www.inf.usi.ch/lanza/Downloads/Wett2008b.pdf)


* **"Software Systems as Cities: A Controlled Experiment" (2011)**
A study validating that the city metaphor statistically improves task correctness and speed in understanding code.
* [Read Paper (PDF)](https://www.inf.usi.ch/lanza/Downloads/Wett2011a.pdf)


* **USI Software Visualization Group**
The research group led by Michele Lanza, which continues to work on software visualization.
* [https://www.inf.usi.ch/lanza/software-visualization.html](https://www.google.com/search?q=https://www.inf.usi.ch/lanza/software-visualization.html)



### 🛠️ Modern Tools & Open Source Implementations

These are modern, ready-to-use tools that apply the USI research concepts to current programming languages using web technologies.

* **CodeCharta**
The most robust modern implementation. It is an open-source tool (web and desktop) that allows you to import analysis from SonarQube or Git and visualize it as a city.
* **Website:** [https://codecharta.com/](https://codecharta.com/)
* **GitHub:** [https://github.com/MaibornWolff/codecharta](https://github.com/MaibornWolff/codecharta)


* **GoCity**
A specific implementation for visualizing **Go (Golang)** projects. It runs entirely in the browser using BabylonJS.
* **Live Tool:** [https://go-city.github.io/](https://go-city.github.io/)
* **GitHub:** [https://github.com/rodrigo-brito/gocity](https://github.com/rodrigo-brito/gocity)


* **JSCity**
An implementation for **JavaScript** codebases, treating functions as buildings.
* **GitHub:** [https://github.com/aserg-ufmg/JSCity](https://github.com/aserg-ufmg/JSCity)
* **Article:** [Visualizing JavaScript Code as 3D Cities](https://medium.com/@aserg.ufmg/visualizing-javascript-code-as-3d-cities-5785867f7d85)



### 📚 Further Reading & Evolutions

Research that expands the metaphor into Virtual Reality (VR) and software evolution (time-travel).

* **"CodeCity: A Comparison of On-Screen and Virtual Reality" (2023)**
A recent study analyzing if navigating Code Cities is more effective in VR headsets.
* [Read Paper (PDF)](https://folia.unifr.ch/documents/329624/files/Minelli_Lanza_2022_Elsevier_IST.pdf)


* **"Visualizing Evolving Software Cities" (2020)**
Research on how to represent the *history* of a codebase (how the city grows/shrinks over time) without confusing the user.
* [Read Paper (PDF)](https://www.inf.usi.ch/lanza/Downloads/Pfah2020a.pdf)